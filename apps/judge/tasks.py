from celery import shared_task
from django.utils import timezone
from apps.submissions.models import Submission
from apps.problems.models import Problem
from .evaluator import CodeEvaluator


@shared_task(bind=True, max_retries=3)
def evaluate_submission(self, submission_id):
    try:
        submission = Submission.objects.select_related('problem', 'user').get(id=submission_id)

        submission.status = 'running'
        submission.save(update_fields=['status'])

        evaluator = CodeEvaluator(submission)

        result = evaluator.evaluate()

        submission.status = result['status']
        submission.test_results = result['test_results']
        submission.execution_time = result.get('execution_time')
        submission.memory_used = result.get('memory_used')
        submission.error_message = result.get('error_message', '')
        submission.evaluated_at = timezone.now()
        submission.save()

        is_accepted = result['status'] == 'accepted'
        submission.problem.increment_submissions(accepted=is_accepted)

        if is_accepted:
            submission.award_points()

        return result

    except Submission.DoesNotExist:
        return {
            'status': 'internal_error',
            'error': f'Submission {submission_id} not found'
        }
    except Exception as e:
        if self.request.retries < self.max_retries:
            raise self.retry(exc=e, countdown=5)
        try:
            submission = Submission.objects.get(id=submission_id)
            submission.status = 'internal_error'
            submission.error_message = f'Evaluation failed: {str(e)}'
            submission.evaluated_at = timezone.now()
            submission.save()
        except:
            pass

        return {
            'status': 'internal_error',
            'error': str(e)
        }


@shared_task
def cleanup_old_containers():
    import docker

    try:
        client = docker.from_env()

        containers = client.containers.list(
            all=True,
            filters={'name': 'code-train-sandbox'}
        )

        removed_count = 0
        for container in containers:
            if container.status == 'exited':
                container.remove()
                removed_count += 1

        return f'Cleaned up {removed_count} containers'
    except Exception as e:
        return f'Cleanup failed: {str(e)}'

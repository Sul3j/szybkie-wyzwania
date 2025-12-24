from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    experience_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default="Beginner")
    bio = models.TextField(blank=True, null=True, max_length=500)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-experience_points']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.user.username}'s Profile (Level {self.level})"
    
    def add_experience(self, points):
        self.experience_points += points
        self._update_level()
        self._update_rank()
        self.save()

    def _update_level(self):
        for level, treshold in sorted(
            settings.LEVEL_TRESHOLDS.items(),
            reverse=True
        ):
            if self.experience_points >= treshold:
                self.level = level
                break
    
    def _update_rank(self):
        for treshold, rank in sorted(
            settings.RANKS.items(),
            reverse=True
        ):
            if self.experience_points >= treshold:
                self.rank = rank
                break

    @property
    def solved_count(self):
        return self.user.submission_set.filter(
            status='accepted'
        ).values('problem').distinct().count()
    
    @property
    def total_submissions(self):
        return self.user.submission_set.count()
    
    @property
    def acceptance_rate(self):
        if self.total_submissions == 0:
            return 0
        accepted = self.user.submission_set.filter(status='accepted').count()
        return round((accepted / self.total_submissions) * 100, 2)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
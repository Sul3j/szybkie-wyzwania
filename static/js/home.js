document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll to features
    const learnMoreBtn = document.getElementById('learnMoreBtn');
    if (learnMoreBtn) {
        learnMoreBtn.addEventListener('click', () => {
            document.querySelector('.features-section').scrollIntoView({
                behavior: 'smooth'
            });
        });
    }

    // CTA button
    const ctaStartBtn = document.getElementById('ctaStartBtn');
    if (ctaStartBtn) {
        ctaStartBtn.addEventListener('click', () => {
            const loginBtn = document.getElementById('loginBtn');
            if (loginBtn) {
                loginBtn.click();
            }
        });
    }

    // Scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all animated elements
    const animatedElements = document.querySelectorAll(
        '.feature-card-modern, .step-card, .rank-card, .cta-content, .section-header-center'
    );

    animatedElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
        observer.observe(el);
    });

    // Test Animation
    function animateTests() {
        const testItems = document.querySelectorAll('.test-case-item');
        const summary = document.querySelector('.test-summary');
        const summaryContent = document.querySelector('.summary-content');

        // Reset all tests
        testItems.forEach(item => {
            item.classList.remove('testing', 'passed');
            const icon = item.querySelector('.test-icon');
            const status = item.querySelector('.test-status');

            icon.className = 'test-icon test-pending';
            icon.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';
            status.textContent = 'Oczekuje...';
        });

        summary.classList.remove('success');
        summaryContent.innerHTML = '<i class="fas fa-hourglass-half"></i><span>Sprawdzanie...</span>';

        // Animate each test sequentially
        let delay = 1500; // Start after 1.5s

        testItems.forEach((item, index) => {
            const icon = item.querySelector('.test-icon');
            const status = item.querySelector('.test-status');

            // Start testing
            setTimeout(() => {
                item.classList.add('testing');
                icon.className = 'test-icon test-running';
                icon.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                status.textContent = 'Sprawdzanie...';
            }, delay);

            // Mark as passed
            setTimeout(() => {
                item.classList.remove('testing');
                item.classList.add('passed');
                icon.className = 'test-icon test-passed';
                icon.innerHTML = '<i class="fas fa-check"></i>';
                status.textContent = 'Zaliczony';
            }, delay + 1000);

            delay += 1200; // Next test starts 1.2s later
        });

        // Show success summary
        setTimeout(() => {
            summary.classList.add('success');
            summaryContent.innerHTML = '<i class="fas fa-check-circle"></i><span>Wszystkie testy zaliczone!</span>';
        }, delay);

        // Restart animation after completion
        setTimeout(() => {
            animateTests();
        }, delay + 4000);
    }

    // Start animation after page load
    setTimeout(() => {
        animateTests();
    }, 1000);
});

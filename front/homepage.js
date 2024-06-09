document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.list');
    const navLinks = document.querySelectorAll('.menu-link');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.6 // 섹션의 60%가 보일 때 트리거
    };

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href').substring(1) === entry.target.id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
});


/*let lastScrollTop = 0;
        const navbar = document.querySelector('.navbar');
        const navbarHeight = navbar.offsetHeight;
        window.addEventListener("scroll", function() {
            let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
            if (currentScroll > lastScrollTop && currentScroll > navbarHeight) {
                // Scrolling Down
                navbar.classList.add('navbar-hidden');
            } else {
                // Scrolling Up
                navbar.classList.remove('navbar-hidden');
            }
            lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
        }, false);
        document.addEventListener("DOMContentLoaded", function() {
    
        var observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('is-visible');
            } else {
                entry.target.classList.remove('is-visible');
            }
            });
        });

        document.querySelectorAll('.card-hover-text').forEach(item => {
            observer.observe(item);
        });
    });*/


const navLinks = document.querySelectorAll('.nav-link');
const windowPath = window.location.pathname;

navLinks.forEach(navLink => {
    if (navLink.href === window.location.href) {
        navLink.classList.add('active');
    }
});
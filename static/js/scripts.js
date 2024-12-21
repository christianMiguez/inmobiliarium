document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.navbar-burger').addEventListener('click', function () {
        document.querySelector('.navbar-menu').classList.toggle('is-active');
    }
    );
});
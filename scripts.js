document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll("figure img");

    images.forEach(img => {
        img.addEventListener("click", () => {
            img.classList.toggle("highlight");
        });
    });

    window.addEventListener("scroll", function () {
        const header = document.querySelector("header");
        if (window.scrollY > 50) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });
});

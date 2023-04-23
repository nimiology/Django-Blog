const floatMenu = document.querySelector(".navbar-menu-sub");
const floatMenuButton = document.querySelector("#navbar-menu-button");

floatMenuButton.addEventListener("mouseenter", () => {
    floatMenu.style.display = "initial";
});

floatMenuButton.addEventListener("mouseleave", () => {
    floatMenu.style.display = "none";
});

floatMenu.addEventListener("mouseenter", () => {
    floatMenu.style.display = "initial";
});

floatMenu.addEventListener("mouseleave", () => {
    floatMenu.style.display = "none";
});

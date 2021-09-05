// Function and codes to Check device is mobile
var navbarMenu = document.getElementsByClassName("navbar-menu")[0];
var navbarMenuM = document.getElementsByClassName("navbar-menu-mobile")[0];
var navbarMenuMButton = document.getElementsByClassName(
  "navbar-menu-mobile-hamburger-menu"
)[0];

var navbarMenuMWrapper = document.getElementsByClassName(
  "navbar-menu-mobile-wrapper"
)[0];

navbarMenuMButton.addEventListener("click", function () {
  if (
    !navbarMenuMWrapper.classList.contains("navbar-menu-mobile-wrapper-active")
  ) {
    lockScroll();
    navbarMenuMWrapper.classList.add("navbar-menu-mobile-wrapper-active");
  } else {
    unLockScroll();
    navbarMenuMWrapper.classList.remove("navbar-menu-mobile-wrapper-active");
  }
});

function setMobileHeader() {
  if (deviceIsMobile()) {
    navbarMenu.style.display = "none";
    navbarMenuM.style.display = "flex";
  } else {
    navbarMenu.style.display = "flex";
    navbarMenuM.style.display = "none";
  }
}

docReady(function () {
  // Run navbar animation
  var headerEl = document.getElementsByTagName("header")[0];

  if (WITH_DELAY) {
    setTimeout(function () {
      headerEl.classList.add("header-faded-in");
    }, DELAY_LENGTH);
  } else {
    headerEl.classList.add("header-faded-in");
  }

  // Check device is mobile ?
  setMobileHeader();
  window.addEventListener("resize", function () {
    setMobileHeader();
  });

  var searchBtns = document.querySelectorAll(".navbar-search-btn");
  var searchBoxModal = document.getElementsByClassName("search-box-modal")[0];

  var searchBoxModalInputBtn = document.getElementsByClassName(
    "search-box-modal-input"
  )[0].children[1];
  var searchBoxModalContainer = document.getElementsByClassName(
    "search-box-modal-container"
  )[0];
  var searchBoxModalInputLine = document.getElementsByClassName(
    "search-box-modal-line"
  )[0];

  searchBtns.forEach((el) => {
    el.addEventListener("click", function () {
      if (el.classList.contains("navbar-search-btn-active")) {
        searchBtns.forEach((el) => {
          el.children[0].classList.replace("bi-x-lg", "bi-search");
          el.classList.toggle("navbar-search-btn-active");
        });
        searchBoxModalContainer.style.opacity = "0";
        searchBoxModalInputLine.style.width = "0";
        navbarMenuMButton.style.zIndex = "90";
        Object.assign(searchBoxModalInputBtn.style, {
          opacity: "0",
          bottom: "-20px",
        });
      } else {
        searchBtns.forEach((el) => {
          el.children[0].classList.replace("bi-search", "bi-x-lg");
          el.classList.toggle("navbar-search-btn-active");
        });
        navbarMenuMButton.style.zIndex = "30";
        setTimeout(function () {
          searchBoxModalContainer.style.opacity = "1";
          searchBoxModalInputLine.style.width = "100%";
        }, 750);
        setTimeout(function () {
          Object.assign(searchBoxModalInputBtn.style, {
            opacity: "1",
            bottom: "0",
          });
        }, 1250);
      }

      searchBoxModal.classList.toggle("search-box-modal-active");
    });
  });
});

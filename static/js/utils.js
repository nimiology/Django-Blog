function docReady(fn) {
  // see if DOM is already available
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    // call on next available tick
    setTimeout(fn, 1);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

function deviceIsMobile() {
  if (window.innerWidth <= 700) {
    return true;
  } else {
    return false;
  }
}

function lockScroll() {
  document.getElementsByTagName("body")[0].style.overflow = "hidden";
}

function unLockScroll() {
  document.getElementsByTagName("body")[0].style.overflow = "scroll";
}

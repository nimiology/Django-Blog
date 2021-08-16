docReady(function () {

    // Run navbar animation
    var headerEl = document.getElementsByTagName('header')[0];

    if (WITH_DELAY) {
        setTimeout(function () {
            headerEl.classList.add('header-faded-in');
        }, 1000);
    } else {
        headerEl.classList.add('header-faded-in');
    }


    var searchBtn = document.getElementsByClassName('navbar-search-btn')[0];
    var searchBoxModal = document.getElementsByClassName('search-box-modal')[0];

    var searchBoxModalInputBtn = document.getElementsByClassName('search-box-modal-input')[0].children[1];
    var searchBoxModalContainer = document.getElementsByClassName('search-box-modal-container')[0];
    var searchBoxModalInputLine = document.getElementsByClassName('search-box-modal-line')[0];

    searchBtn.addEventListener('click', function () {

        if (searchBtn.classList.contains('navbar-search-btn-active')) {
            searchBtn.children[0].classList.replace('bi-x-lg', 'bi-search');
            searchBtn.classList.toggle('navbar-search-btn-active');
            searchBoxModalContainer.style.opacity = '0';
            searchBoxModalInputLine.style.width = '0';
            Object.assign(searchBoxModalInputBtn.style, {opacity: '0', bottom: '-20px'});
        } else {
            searchBtn.children[0].classList.replace('bi-search', 'bi-x-lg');
            searchBtn.classList.toggle('navbar-search-btn-active');
            setTimeout(function () {
                searchBoxModalContainer.style.opacity = '1';
                searchBoxModalInputLine.style.width = '100%';
            }, 750);
            setTimeout(function () {
                Object.assign(searchBoxModalInputBtn.style, {opacity: '1', bottom: '0'});
            }, 1250)
        }

        searchBoxModal.classList.toggle('search-box-modal-active');
    });
});
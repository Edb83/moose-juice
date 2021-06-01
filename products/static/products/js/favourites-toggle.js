// get HTML to inject into container
const heartFull = `<i class="fas fa-heart fa-lg"></i>`;
const heartEmpty = `<i class="far fa-heart fa-lg"></i>`;
const heartBroken = `<i class="fas fa-heart-broken fa-lg"></i>`;

// listen for click on container and read data attributes to know route to follow
$(".product-heart-container").click(function () {
    const iconSpan = $(this).children('span');
    const toggleUrl = this.dataset.url;
    const redirectUrl = this.dataset.redirect;

    // setup AJAX call for backend data
    $.ajax({
        url: toggleUrl,
        dataType: 'json',
        success: function (data) {
            // check user has profile
            if (data.is_authenticated) {
                // if user on favourites page and already favourited
                if (data.is_favourite && window.location.pathname == "/products/favourites/") {
                    iconSpan.children('i').replaceWith(heartBroken);
                }
                // if elsewhere and a favourite
                else if (data.is_favourite) {
                    iconSpan.children('i').replaceWith(heartEmpty);
                // if not yet a favourite
                } else {
                    iconSpan.children('i').replaceWith(heartFull);
                }
            // otherwise redirect to login
            } else {
                window.location.assign(redirectUrl);
            }
        }
    });
});
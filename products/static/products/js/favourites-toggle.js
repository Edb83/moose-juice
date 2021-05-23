heartFull = `<i class="fas fa-heart fa-lg"></i>`
heartEmpty = `<i class="far fa-heart fa-lg"></i>`
heartBroken = `<i class="fas fa-heart-broken fa-lg"></i>`

$(".product-heart-container").click(function () {
    // const product = this.dataset.product;
    const iconSpan = $(this).children('span');
    const toggleUrl = this.dataset.url;

    $.ajax({
        url: toggleUrl,
        dataType: 'json',
        success: function (data) {
            if (data.is_authenticated) {
                if (data.is_favourite && window.location.pathname == "/products/favourites/") {
                    iconSpan.children('i').replaceWith(heartBroken);
                }
                else if (data.is_favourite) {
                    iconSpan.children('i').replaceWith(heartEmpty);
                } else {
                    iconSpan.children('i').replaceWith(heartFull);
                }
            } else {
                window.location.replace('{% url "account_login" %}')
            }
            
        }
    });
});
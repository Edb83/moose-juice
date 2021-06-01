$('.remove-item').click(function() {

    // As remove button is outside quantity form we need to
    // find an object with matching item_id where the csrf_token
    // has been added to its data-item
    let itemId = $(this).attr('id').split('remove_')[1];
    let nearbyTokenHolder = $(`#id_qty_${itemId}`);
    let csrfToken = nearbyTokenHolder.data('token');
    let url = `/cart/remove/${itemId}/`;
    let data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data).done(function() {
         location.reload();
    });
});
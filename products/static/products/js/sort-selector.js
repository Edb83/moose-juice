$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);

    let selectedVal = selector.val();
    if (selectedVal != "reset") {
        let stringSplit = selectedVal.split("_")
        let direction = stringSplit[(stringSplit.length) - 1];
        stringSplit.pop();
        let sort = stringSplit.join("_");

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})
const productStars = document.querySelectorAll('.product-stars');

productStars.forEach(rating => {
    const ratingValue = parseInt(rating.dataset.value);
    const fullStar = ratingValue;
    let stars = '';

    for (let i = 1; i < 6; i++) {
        if (i <= fullStar) {
            stars += `<i class="fas fa-star"></i>`;
        } else {
            stars += `<i class="far fa-star"></i>`;
        }
    }

    rating.innerHTML = stars;
})
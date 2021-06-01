let colorPicker = $('#id_color');
let colorGradient = document.querySelector('.js-stopColor');
let bottleFill = document.querySelector('.js-bottle');
let chosenColor;

$(colorPicker).on('input',function () {
    chosenColor = this.dataset.currentColor;
    colorGradient.setAttribute('stop-color', chosenColor);
    bottleFill.setAttribute('fill', "url('#gradient-')");
});
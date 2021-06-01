// http://jsfiddle.net/6khr8e2b/

$(function(){
    let nameInput = $('#id_name');
    let nameOutput = $('.card-title');
    function onChange() {
        if (nameInput.val()) {
            nameOutput.text(nameInput.val());
        } else {
            nameOutput.text("?");
        }
    }

    $(nameInput)
        .change(onChange).keyup(onChange);
});
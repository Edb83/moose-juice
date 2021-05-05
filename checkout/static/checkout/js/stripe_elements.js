/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
      base: {
        iconColor: '#000',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    }

let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element

// From Stripe:
  // card.on("change", function (event) {
  //   // Disable the Pay button if there are no card details in the Element
  //   document.querySelector("button").disabled = event.empty;
  //   document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
  // });
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
      payment_method: {
          card: card,
      }
  }).then(function(result) {
      if (result.error) {
          var errorDiv = document.getElementById('card-errors');
          var html = `
              <span class="icon" role="alert">
              <i class="fas fa-times"></i>
              </span>
              <span>${result.error.message}</span>`;
          $(errorDiv).html(html);
          card.update({ 'disabled': false});
          $('#submit-button').attr('disabled', false);
      } else {
          if (result.paymentIntent.status === 'succeeded') {
              form.submit();
          }
      }
  });
});
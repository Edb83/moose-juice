/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
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
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
        fontFamily: 'Karla, sans-serif, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#343a40',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    };

let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
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
  // 1. Prevent form from submitting and disable card element
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);

  // 2. Capture from details not added to PaymentIntent
  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  // 3. Post to cache_data_checkout view
  // 4. View updates PaymentIntent and returns 200 server response
  // 5. Call confirmCardPayment and store billing and shipping details 
  $.post(url, postData).done(function () {
      stripe.confirmCardPayment(clientSecret, {
          payment_method: {
              card: card,
              billing_details: {
                  name: $.trim(form.full_name.value),
                  phone: $.trim(form.phone_number.value),
                  email: $.trim(form.email.value),
                  address:{
                      line1: $.trim(form.street_address1.value),
                      line2: $.trim(form.street_address2.value),
                      city: $.trim(form.town_or_city.value),
                      country: $.trim(form.country.value),
                      state: $.trim(form.county.value),
                  }
              }
          },
          shipping: {
              name: $.trim(form.full_name.value),
              phone: $.trim(form.phone_number.value),
              address: {
                  line1: $.trim(form.street_address1.value),
                  line2: $.trim(form.street_address2.value),
                  city: $.trim(form.town_or_city.value),
                  country: $.trim(form.country.value),
                  postal_code: $.trim(form.postcode.value),
                  state: $.trim(form.county.value),
              }
          },
      }).then(function(result) {
          // 6. Handle any errors
          if (result.error) {
              var errorDiv = document.getElementById('card-errors');
              var html = `
                  <span class="icon" role="alert">
                  <i class="fas fa-times"></i>
                  </span>
                  <span>${result.error.message}</span>`;
              // Display error
              $(errorDiv).html(html);
              // Reenable card element and submit button
              card.update({ 'disabled': false});
              $('#submit-button').attr('disabled', false);
          
          // 7. Submit form
          } else {
              if (result.paymentIntent.status === 'succeeded') {
                  form.submit();
              }
          }
      });

  // 8. If data not posted to view, reload the page and allow any Django error messages
  }).fail(function () {
      location.reload();
  });
});
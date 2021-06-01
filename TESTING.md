<span id="top"></span>

Back to [README](README.md)

## Index

- <a href="#user-stories">User stories - how are they met?</a>
- <a href="#testing-manual">Manual</a>
- <a href="#testing-auto">Automated</a>
- <a href="#testing-responsive">Responsiveness</a>
- <a href="#testing-resolved">Resolved issues</a>
- <a href="#testing-unresolved">Unresolved issues</a>

---

<span id="user-stories"></span>

## User stories - how are they met?

### Overarching user expectations

**Consistency**

The site has been designed to be as consistent as possible, no matter the content:
- The Navbar and Footer remain the same across all pages, including Error pages.
- Headings and icons (form fields and add/edit/delete buttons) are standardised across all pages.
- Cards are a uniform shape and size per page and will never spill into a subsequent row.
- Cards represent a 'zoomed out' view of multiple selection items (Activities/Search Bar page and Categories pages), whereas views of single items (View Activity, input forms) are 'zoomed in' without a card to suggest a boundary.
- Where necessary, text is truncated to preserve the grid layout.

**Easy navigation**

The likely options a user might need at a given moment have been carefully considered to ensure a smooth browsing experience:

- Headings are descriptive of the content displayed even when a search or filter is applied.
- When a search finds no results...
- The title of each page updates in the browser window to indicate where the user is.
- The Footer contains top-level menu options, 

**Intuitive design**


- Familiar icons have been used across the site for commonly expected actions e.g. add, edit, delete, search, back.
- Toasts pop-ups discretely alert the user when they perform meaningful actions i.e. logins and content changes.
- As a user might expect, modals appear to confirm content deletion.

**Responsiveness**

- Pages adapt to a variety of screen sizes thanks to the Bootstrap grid template and extensive testing in Chrome Dev Tools.
- Where readability is compromised, page structure is modified to give more space to the elements (e.g. giving username its own row on the View Activity page).

**Security**

- Allauth provides a robust user account system while Stripe offers secure payments, furthered by use of webhooks to ensure transactions are recorded.

**Appealing visuals**

- SVGs
- Simple, bold colours and use of consistent spacing bring clarity to the content.

### As a X I want...

**To immediately understand what the purpose of the site is and what it can provide**

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-manual"></span>

## Manual testing

The following tests have been carried out without issue:


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-auto"></span>

## Automated testing

[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Lighthouse audit summary for both desktop and mobile:

**Home page**

- Performance: **99%**
- Accessibility: **100%**
- Best Practices: **100%**
- SEO: **100%**


**Product pages**

- Performance: **99%**
- Accessibility: **100%**
- Best Practices: **100%**
- SEO: **100%**

**Categories page**

- Performance: **82 - 99%**
- Accessibility: **97%**
- Best Practices: **100%**
- SEO: **100%**

**Add / Edit pages**

- Performance: **90 - 99%**
- Accessibility: **88%**
- Best Practices: **100%**
- SEO: **98 - 100%**

**Profile page**

- Performance: **73 - 98%**
- Accessibility: **100%**
- Best Practices: **100%**
- SEO: **100%**

[W3C - HTML](https://validator.w3.org/) - 0 errors, 0 warnings - **PASS**

[W3C - CSS](https://jigsaw.w3.org/css-validator/) - 

- Use of unknown vendor extensions

[CSS Lint](http://csslint.net/) - 



[Unicorn revealer - overflow](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln/related) - no evidence of overflow - **PASS**

[JS Hint](https://jshint.com/) - 0 errors, 0 warnings - **PASS**


[PyCodeStyle](https://github.com/PyCQA/pycodestyle) - 0 warnings - **PASS**



<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing-responsive"></span>

## Responsiveness

The site has been designed with a mobile-first philosophy and, supported by [Materialize](https://materializecss.com/), has been thoroughly tested at all stages of development using [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).

In addition to Materialize's breakpoints, various media queries have been used to maximise the legibility of text and provide sufficient spacing for all content. These queries include optimised `margin`, `padding`, `text-align` and adjustments of `display` to accommodate changes in HTML structure. Particular attention has been paid to the appearance of cards and buttons on different devices.

Examples:

- on the View Activity page the 'Back' button has been aligned with the activity details below in keeping with Materialize's breakpoints.
- on the Categories page, the cards' appearance at the breakpoints from 2 to 3 columns was studied to make sure that even in a worst case scenario their content would not be put out of place. Revisions saw the card choice and position of each element tested, including when logged in as admin and the edit and delete buttons are visible.
- the Footer content was separated out on larger screen sizes to make better use of the space.
- the `flow-text` Materialize class has been used for any large text areas to ensure they are as legible as possible depending on device viewed with.


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

### Browsers

Tested on:

- Chrome
- Edge
- Firefox
- Safari (iOS)

### Screen sizes

Tested with Chrome DevTools using profiles for:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

... and also using the responsive profiles of:

- Mobile S (320px)
- Mobile M (375px)
- Mobile L (425px)
- Tablet (768px)
- Laptop (1024px)
- Laptop L (1440px)

Real world testing on:

- iPhone 6S
- iPhone SE
- iPhone 11 Pro
- Asus ZenBook
- Dell XPS 7590


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## Issues and bugs

<span id="testing-resolved"></span>

### Resolved

Bug 1: get_object_or_404 error caused by object id not being found
Solution: find erroneous string iteration pointing to Nicotine (4 items) rather than Size (3 items)

Bug 2: search queries via M2M relationship (Tags model) would return duplicate results
Solution: using .distinct() on the filtered query

Bug 3: line order items can be set to 0 in Admin
Solution: 

<!-- Bug 4: line order items have price tied to the model when it should be set on save
Solution:  -->

Bug 5: custom save method on Review model used to request average_rating calculation on Product model. Rating was calculated before the new rating was saved meaning inaccurate ratings
Solution: use a signal on Review creation/update/delete to call calculate_rating

Bug 6: review save/delete signal would not fire as expected
Solution: import the signal in the product/apps.py

Bug 7: if product is deleted while exists in cart, 404 across all pages
Solution (immediate): set cart contexts to equal 0 across the board and delete session cookies
Solution (long-term): 

Bug 8: signal to check whether user has already reviewed product when awarding points would always return true
Solution: change from post_save to pre_save (as otherwise user will always have reviewed the product post save)

Bug 9: signal to award points on Order post_save cannot retrieve the instance UserProfile
Solution: this was due to 'if created' check only looking at the instance on the initial Order save, before the user's profile relationship was established. Fixed by switching 'if created' to 'if instance.user_profile'

Bug 10: after checking out successfully with discount applied, when adding items to another cart the 'remove discount' toggle still appears despite being set to False on checkout
Solution:

Bug 11: cannot get ::before pseudo class to work with certain font-awesome icons

`.icon-product:hover .far.fa-heart::before {
    content: "\F004";
}`

Solution: adding font-family and font-weight to the pseudo class (https://stackoverflow.com/questions/47712987/font-awesome-5-on-pseudo-elements)

    font-family: 'Font Awesome 5 Free';
    font-weight: 900;

Bug 12: sorting products by rating worked fine in mySQL but not in Postgres, appearing to order by nulls first
Solution: using F function with nulls_last=True as argument in separate conditional for sortkey == 'average_rating'

Bug 13: orders somtimes saved twice and have no grand total attached to them
Solution: caused by webhook not being able to find order due to mismatching grand_total (following discount applied in cart). Solved by checking discount_applied session at point of order_form save and including points_redeemed so that grand_total can be calculated properly

Bug 14: static files not loading
Solution: add STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') to settings.py

Bug 15: when moving inline scripts to respective static folders, one file (`remove-item.js`) could not be accessed.
Solution: changed `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)` to `STATICFILES_DIRS = [BASE_DIR/'static/']`

Bug 16: orders saved in Production would have no cost associated with them
Solution: this was particularly difficult to solve as the issue was only present in the deployed version. Extensive use of print statements showed that after the order was initially saved, the OrderLineItem signal to `update_total()` was not being fired. This (post)[https://stackoverflow.com/questions/66762262/django-signals-not-executed] led to checking the signal function name `update_on_save()` which, when changed, eliminated the error.

Bug 17: rounding error for points earned on a purchase means user will occasionally get 1 point extra
Solution: could not reproduce even with order_total ending £0.50 but set items to end £0.49 or £0.99 to mitigate issue

Bug 18: messages.success includes cart contents no matter the context
Solution: Partially solved by including context on rendered views (e.g. on_profile_page), however context cannot be passed on form submissions etc in the same way. Using a hidden form field is probably the best solution but in the meanwhile switched certain messages over from messages.success to the less cluttered messages.info

Bug 19: deleting a product which has been purchased will obviously delete an order's lineitem and lead to difficulties.
Solution: insufficient time to fix, but likely using `on_delete=models.SET()` and retrieving string versions of the to-be-deleted product, siz, nicotine, price etc would be the way forward
UNSOLVED

Bug 20: deleting a product which has reviews leads to a KeyError
Solution: caused by the signal which updates a product rating on deletion. On product deletion the CASCADE would delete all reviews, which would in turn fire the update_total signal for an instance which no longer existed. Solved initially by changing the signal to pre_delete, but this would have caused problems when updating the rating as it would include the to-be-deleted review too. Solve eventually by changing the ProductReview's on_delete to SET_NULL, storing the to-be-deleted reviews in the product's delete view,  deleting them after the product itself was deleted, and finally including a check that the product instance existed on the post_delete update signal.

### Unresolved

Bug 1: get_object_or_404 error caused by object id not being found
Solution: find erroneous string iteration pointing to Nicotine (4 items) rather than Size (3 items)

Bug 2: search queries via M2M relationship (Tags model) would return duplicate results
Solution: using .distinct() on the filtered query

Bug 3: line order items can be set to 0 in Admin
Solution: due to setting default=0 ?

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
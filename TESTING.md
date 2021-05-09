Bug 1: get_object_or_404 error caused by object id not being found
Solution: find erroneous string iteration pointing to Nicotine (4 items) rather than Size (3 items)

Bug 2: search queries with multiple criteria would return duplicate results
Solution: using .distinct() on the filtered query

Bug 3: line order items can be set to 0 in Admin
Solution: due to setting default=0 ?

<!-- Bug 4: line order items have price tied to the model when it should be set on save
Solution:  -->

Bug 5: custom save method on Review model used to request average_rating calculation on Product model. Rating was calculated before the new rating was saved meaning inaccurate ratings
Solution: use a signal on Review creation/update/delete to call calculate_rating

Bug 6: review save/delete signal would not fire as expected
Solution: import the signal in the product/apps.py

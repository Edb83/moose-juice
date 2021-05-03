Bug 1: get_object_or_404 error caused by object id not being found
Solution: find erroneous string iteration pointing to Nicotine (4 items) rather than Size (3 items)

Bug 2: search queries with multiple criteria would return duplicate results
Solution: using .distinct() on the filtered query


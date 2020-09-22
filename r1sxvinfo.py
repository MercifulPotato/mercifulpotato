# r1sxv.info/LpxTIfl3N4
# ten characters long
# A-Z a-z 0-9

import itertools

import requests

upper_case = [chr(item) for item in range(ord('A'), ord('Z') + 1)]
lower_case = [chr(item) for item in range(ord('A'), ord('Z') + 1)]
numbers = [chr(item) for item in range(ord('0'), ord('9') + 1)]

my_input = upper_case + lower_case + numbers

for my_input in map(''.join, itertools.product(my_input, repeat=10)):
    my_url = f"http://r1sxv.info/{my_input}"
    max_retries = 20
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    comment_data = session.get(
        my_url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache", },
    )
    print(comment_data)

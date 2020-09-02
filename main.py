import requests

from model.Item import get_item_from_data


def recursive(kid):
    comment_url = f"https://hacker-news.firebaseio.com/v0/item/{kid}.json"
    max_retries = 20
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    comment_data = session.get(
        comment_url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache", },
    ).json()
    if comment_data is not None:
        my_item = get_item_from_data(comment_data)
        with open(f"data/{kid}.txt", "w") as comment_file:
            comment_file.write(repr(my_item))
        print(my_item)
        if "kids" in comment_data:
            itemkids = comment_data["kids"]
            for kid in itemkids:
                recursive(kid)


top_stories = requests.get(
    "https://hacker-news.firebaseio.com/v0/topstories.json",
    headers={"Cache-Control": "no-cache", "Pragma": "no-cache"},
).json()
for story in top_stories:
    recursive(story)

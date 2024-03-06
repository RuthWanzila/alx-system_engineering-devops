#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords """
import requests


def count_words(subreddit, word_list, after=None, counts={}):
"""parses the title of all hot articles, 
and prints a sorted count of given keywords"""
 if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;
        x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json()
    articles = data['data']['children']

    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word not in counts:
                counts[word] = 0
            counts[word] += title.count(word)

    next_page = data['data']['after']

    if next_page is not None:
        count_words(subreddit, word_list, after=next_page, counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

from typing import List
from collections import deque
import json


def getLinks(url: str) -> List[str]:
    if url == "https://www.owlmountain.net/":
        return [
            "https://github.com/timowlmtn",
            "https://www.owlmountain.net/post/metal-singing-and-the-voice",
            "https://www.owlmountain.net/post/role-playing-one-shots-based-on-music",
        ]
    elif url == "https://www.owlmountain.net/post/metal-singing-and-the-voice":
        return [
            "https://www.owlmountain.net/post/the-backstory-of-the-icosahedron",
            "https://www.youtube.com/watch?v=9B6dsfGazyI",
        ]
    elif (
        url == "https://www.owlmountain.net/post/role-playing-one-shots-based-on-music"
    ):
        return [
            "https://www.sputnikmusic.com/review/39522/Janelle-Monae-Metropolis-The-Chase-Suite/",
            "https://www.owlmountain.net/post/the-backstory-of-the-icosahedron",
        ]
    elif url == "https://www.owlmountain.net/post/the-backstory-of-the-icosahedron":
        return [
            "https://www.owlmountain.net/post/metal-singing-and-the-voice",
            "https://www.owlmountain.net/post/role-playing-one-shots-based-on-music",
            "https://www.owlmountain.net/post/adding-to-the-mlflow-pipeline-conformal-prediction",
        ]
    else:
        return []


def scrape(url: str):
    """
    This will scape the website using beautiful soup or chrome plugin

    :param url:
    :return:
    """
    print(f"<head>{url}</head><body>...</body>")
    return f"<head>{url}</head><body>...</body>"


def main():
    target = "https://www.owlmountain.net/"

    # Initialize the first target
    target_pages = {target: None}

    queue = deque([target])

    while queue:
        url = queue.popleft()
        target_pages[url] = scrape(url)
        current_target = url
        print(f"***\t {current_target}")
        for webpage in getLinks(current_target):
            print(
                f"\t{webpage}: {webpage.startswith(target)} {webpage not in target_pages}"
            )
            if webpage.startswith(target) and webpage not in target_pages:
                target_pages[webpage] = None
                queue.append(webpage)

    print(f"\n{json.dumps(target_pages, indent=2)}")


if __name__ == "__main__":
    main()

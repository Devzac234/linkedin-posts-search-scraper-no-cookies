thonimport requests
from bs4 import BeautifulSoup

class LinkedInParser:
    def __init__(self, query):
        self.query = query
        self.base_url = "https://www.linkedin.com/search/results/content/?keywords="

    def scrape_posts(self):
        url = f"{self.base_url}{self.query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error: Failed to retrieve data. Status code {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        posts = self._extract_posts(soup)
        return posts

    def _extract_posts(self, soup):
        posts = []
        for post in soup.find_all("div", class_="search-result__info"):
            content = post.find("span", class_="feed-shared-text__text")
            if content:
                posts.append({
                    "post_url": post.find("a")["href"],
                    "content": content.text.strip(),
                    "author": {
                        "name": post.find("span", class_="actor-name").text.strip(),
                        "job_title": post.find("span", class_="actor-title").text.strip(),
                    },
                })
        return posts
import argparse
import requests
from bs4 import BeautifulSoup
from termcolor import colored


def scrape_urls(domain, dork, num_pages=3):
    """Scrape multiple pages of search results from multiple search engines."""
    print(colored(f"Scraping {num_pages} pages of search results for {dork}:{domain}...", "green"))

    urls = set()
    session = requests.Session()

    search_engines = [
        {'name': 'google', 'url': f"https://www.google.com/search?q={dork}:{domain}&start="},
        {'name': 'bing', 'url': f"https://www.bing.com/search?q={dork}+site%3A{domain}&first="},
        # {'name': 'yahoo', 'url': f"https://search.yahoo.com/search?p={dork}+site%3A{domain}&b="},
        # {'name': 'duckduckgo', 'url': f"https://duckduckgo.com/html/?q={dork}+site%3A{domain}&kl=wt-wt&kae=d"}
    ]

    for engine in search_engines:
        print(f"Scraping {engine['name']}...")
        for page in range(num_pages):
            start = page * 10
            url = engine['url'] + str(start)
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all("a")

            for link in links:
                url = link.get("href")

                if url and url.startswith("/url?q="):
                    url = url[7:].split("&")[0]

                    if domain in url:
                        urls.add(url)
                        # print(url)

    return urls


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape search engine results for a domain and dork.')
    parser.add_argument('domain', type=str, help='Domain to search for')
    parser.add_argument('dork', type=str, help='Dork to search for')
    parser.add_argument('--num-pages', type=int, default=3, help='Number of search result pages to scrape')
    args = parser.parse_args()

    urls = scrape_urls(args.domain, args.dork, args.num_pages)

    print(colored(f"Found {len(urls)} unique URLs for {args.domain} with the dork '{args.dork}':", "green"))
    for url in urls:
        print(colored(url, "blue"))

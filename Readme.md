# Search Engine Scraper

This is a command line tool for scraping search engine results for a specific domain and dork. It currently supports Google and Bing.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/search-engine-scraper.git
    ```

2. Navigate to the cloned directory:

    ```
    cd search-engine-scraper
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

The tool takes three arguments:

usage: search_engine_scraper.py [-h] [--num-pages NUM_PAGES] domain dork

Scrape search engine results for a domain and dork.

positional arguments:
    `domain`  Domain to search for
    `dork`    Dork to search for

optional arguments:
    -h, --help show this help message and exit
    --num-pages NUM_PAGES
    Number of search result pages to scrape (default: 3)


To run the tool, enter the following command in the terminal:

`python osint.py example.com "site" --num-pages 5`


This will scrape 5 pages of search results for the domain `example.com` and the dork `site`.

The tool will output a list of unique URLs found in the search results.

## License

This tool is licensed under the [MIT License](https://github.com/Ashutosh-upadhya/search-engine-scraper/blob/master/LICENSE).

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

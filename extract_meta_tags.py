import argparse
import requests
from bs4 import BeautifulSoup


def extract_and_print_meta_tags(url, disable_ssl_check=False):
    try:
        response = requests.get(url, verify=not disable_ssl_check)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        meta_tags = soup.find_all('meta')

        print(f"Meta tags extracted from {url}:")
        for tag in meta_tags:
            tag_line = str(tag)
            print(tag_line)

    except requests.RequestException as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Extract and Print Meta Tags from Web Page')
    parser.add_argument('-u', '--url', metavar='URL', type=str, required=True, help='URL of the web page')
    parser.add_argument('-ds', '--disable-ssl', action='store_true', help='Disable SSL certificate checks')

    args = parser.parse_args()

    extract_and_print_meta_tags(args.url, args.disable_ssl)


if __name__ == "__main__":
    main()

import requests
import argparse


def banner_grabbing(url, disable_ssl_check=False):
    try:
        # Disable SSL certificate verification if the flag is provided
        if disable_ssl_check:
            response = requests.get(url, verify=False)
        else:
            response = requests.get(url)

        print(f"Headers for {url}:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.RequestException as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Banner Grabber Script')
    parser.add_argument('url', metavar='URL', type=str, help='Target URL')
    parser.add_argument('-ds', '--disable-ssl', action='store_true', help='Disable SSL certificate checks')

    args = parser.parse_args()
    banner_grabbing(args.url, args.disable_ssl)


if __name__ == "__main__":
    main()

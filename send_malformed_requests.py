import requests
import argparse


def make_custom_request(url, custom_method, disable_ssl_check=False):
    try:
        # Disable SSL certificate verification if the flag is provided
        if disable_ssl_check:
            response = requests.request(custom_method, url, verify=False)
        else:
            response = requests.request(custom_method, url)

        # Print response status code
        print(f"Response Status Code: {response.status_code}")

        # Print response headers line by line
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.RequestException as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Custom HTTP Request Script')
    parser.add_argument('url', metavar='URL', type=str, help='Target URL')
    parser.add_argument('custom_method', metavar='METHOD', type=str, help='Custom HTTP method')
    parser.add_argument('-ds', '--disable-ssl', action='store_true', help='Disable SSL certificate checks')

    args = parser.parse_args()
    make_custom_request(args.url, args.custom_method, args.disable_ssl)


if __name__ == "__main__":
    main()

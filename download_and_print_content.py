import argparse
import requests

def download_and_print_content(url, filename_list, disable_ssl_check=False):
    for filename in filename_list:
        try:
            full_url = f"{url}/{filename.strip()}"
            response = requests.get(full_url, verify=not disable_ssl_check)
            response.raise_for_status()

            content = response.text
            print(f"Content of '{filename.strip()}' from {full_url}:\n{content}")

        except requests.RequestException as e:
            print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Download and Print File Content Using Python Script')
    parser.add_argument('-u', '--url', metavar='URL', type=str, required=True, help='Base URL for files')
    parser.add_argument('-f', '--txt-file', metavar='TXT_FILE', type=str, default=None,
                        help='Path to text file with filenames')
    parser.add_argument('-ds', '--disable-ssl', action='store_true', help='Disable SSL certificate checks')

    args = parser.parse_args()

    try:
        if args.txt_file:
            with open(args.txt_file, 'r') as file:
                filename_list = [line.strip() for line in file.readlines()]
        else:
            filename_list = [args.url]

        download_and_print_content(args.url, filename_list, args.disable_ssl)
    except FileNotFoundError:
        print(f"Error: Text file '{args.txt_file}' not found.")


if __name__ == "__main__":
    main()

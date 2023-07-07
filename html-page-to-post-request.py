import argparse
import pyfiglet

from utils.Processor import Processor

if __name__ == "__main__":
    print(pyfiglet.figlet_format("html-page-to-post-request", font="slant"))

    parser = argparse.ArgumentParser(description="html-page-to-post-request")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("-d", "--depth", help="Maximum depth to crawl", default=3, type=int)
    parser.add_argument("-t", "--type", help="Type of the input to inject", default="text")
    parser.add_argument("--headers", nargs='*', metavar='HEADER', default=None, help="Add headers")
    parser.add_argument("-p", "--payload", help="Payload to inject", required=True)
    args = parser.parse_args()

    if not args.payload:
        print("You must specify a payload to inject")
        exit()
    
    if not args.type:
        print("Text is the default type of input to inject")

    if not args.depth:
        print("3 is the default depth to crawl")

    headers = {}
    if args.headers:
        for header in args.headers:
            key, value = header.split(':')
            headers[key.strip()] = value.strip()

    processor = Processor(url=args.url, depth=args.depth, headers=headers, input_type=args.type, payload=args.payload, other_function=None)
    processor.process()
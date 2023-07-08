# html-page-to-post-request
![version](https://img.shields.io/badge/version-1.0.0-blue)

HTML to POST Request Converter is a tool designed to transform HTML pages into POST requests using the forms present on those HTML pages. It takes a list of URLs obtained through a crawler and processes them to generate corresponding POST requests.

The tool is useful when you need to interact with web applications programmatically by simulating form submissions. Instead of manually inspecting each HTML page and constructing POST requests, this tool automates the process and saves you time and effort.

## Disclaimer:

This crawler tool has been developed for educational purposes and to assist in personal challenges. It is important to note that I am not responsible for any malicious actions taken with this tool. The intention behind creating this tool is to learn and explore web crawling techniques, not to encourage or support any illegal or unethical activities.

It is crucial to use this tool responsibly and in accordance with applicable laws and regulations. Any misuse or unauthorized access to websites or sensitive information is strictly prohibited. Always obtain proper authorization before conducting any scanning or crawling activities on a website.

I strongly advise against using this tool for any malicious or harmful purposes. It is your responsibility to use this tool ethically and respect the privacy and security of others. By using this tool, you agree to take full responsibility for your actions and any consequences that may arise from them.

## Dependencies
The crawler script requires the following dependencies:
* [Python 3](https://www.python.org/downloads/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests](https://requests.readthedocs.io/en/master/)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [pyfiglet](https://pypi.org/project/pyfiglet/)
...

## Installation
To use the HTML to POST Request Converter, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/coutand-bastien/html-page-to-post-request.git
```
2. Navigate to the project directory:

```bash
cd html-to-post-converter
```

3. Install the required dependencies:
To install the dependencies, run the following command:
```bash
pip3 install -r requirements.txt
```

## Usage
The HTML to POST Request Converter provides a command-line interface with the following options:

```bash
python3 html-page-to-post-request.py [-h] [-d DEPTH] [-t TYPE] [--headers HEADERS] -p PAYLOAD url

positional arguments:
  url                               Base url to use

options:
  -h, --help                        show this help message and exit
  -d DEPTH, --depth DEPTH           Maximum depth to crawl
  -t TYPE, --type TYPE              Type of the input to inject
  --headers HEADERS                 Specify the header value
  -p PAYLOAD, --payload PAYLOAD     Payload to inject
```

## Example
```bash
python3 ./html-page-to-post-request.py --headers='{"Cookie":"mycookie=abcd123"}' http://exemple.com/ -p test
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
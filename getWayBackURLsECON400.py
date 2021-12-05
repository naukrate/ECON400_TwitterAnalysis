import requests as rq
import json
import pandas as pd
import csv

filename = "waybackurls.csv"


def write_urls(url):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([str(url)])


def final_urls(url_list):
    for archive_url in url_list:
        final_url = 'https://web.archive.org/web/' + archive_url
        print(final_url)
        write_urls(final_url)


# def extract_urls:

# import list of URLs for loop later
df = pd.read_excel("twitterurls.xlsx", header=None)
twitterurls = df[0].tolist()

print(twitterurls)

for url in twitterurls:
    # MSNBC Wayback Machine Archive URLS
    url = "http://web.archive.org/cdx/search/cdx?url=" + url + "&collapse=digest&from=202107011&to=20210702&output=json"
    print(url)

    urls = rq.get(url).text
    parse_url = json.loads(urls)  # parses the JSON from urls.

    # Extracts timestamp and original columns from urls and compiles a url list.
    url_list = []
    for i in range(1, len(parse_url)):
        orig_url = parse_url[i][2]
        tstamp = parse_url[i][1]
        waylink = tstamp + '/' + orig_url
        url_list.append(waylink)

    # Compiles final url pattern
    final_urls(url_list)
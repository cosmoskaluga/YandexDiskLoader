# based on https://ru.stackoverflow.com/questions/1088300/%D0%BA%D0%B0%D0%BA-%D1%81%D0%BA%D0%B0%D1%87%D0%B8%D0%B2%D0%B0%D1%82%D1%8C-%D1%84%D0%B0%D0%B9%D0%BB%D1%8B-%D1%81-%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81-%D0%B4%D0%B8%D1%81%D0%BA%D0%B0

import requests
import argparse
import sys
from urllib.parse import urlencode

parser = argparse.ArgumentParser(description = 'yandexDiskLoader: downloading files from Yandex Disk using a shared link', usage = ''' python3 yandexDiskLoader.py <shared link> <filename>''')

parser.add_argument('-l', type = str, help = 'a shared Yandex link to a file')
parser.add_argument('-o', type = str, help = 'a name of the downloaded file')

args = parser.parse_args(sys.argv[1:])

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

final_url = base_url + urlencode(dict(public_key=args.l))
response = requests.get(final_url)
download_url = response.json()['href']
download_response = requests.get(download_url)

with open(args.o, 'wb') as f:   
    f.write(download_response.content)
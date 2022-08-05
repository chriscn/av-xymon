from bs4 import BeautifulSoup

import time
import datetime

NONGREEN_FILE_LOCATION = "/var/lib/xymon/www/nongreen.html"
NONGREEN_SORTED_FILE_LOCATION = "/var/lib/xymon/www/nongreen_sorted.html"

def main():
    logging.basicConfig(level=logging.INFO)

    while True:
        print(f'Writing sorted file at {datetime.datetime.now()}')

        with open(NONGREEN_FILE_LOCATION, 'r') as nongreen_raw:
            nongreen_parsed = BeautifulSoup(nongreen_raw, 'html.parser')

            lines = nongreen_parsed.body.find_all('tr', attrs={'class':'line'})

            lines = sorted(lines, key=lambda x: x.td.font.text)

            table = nongreen_parsed.body.find_all('tbody')[1]

            for line in lines:
              table.append(line)

            with open(NONGREEN_SORTED_FILE_LOCATION, 'w') as nongreen_output:
                nongreen_output.write(nongreen_parsed.prettify())

        time.sleep(60)

if __name__ == '__main__':
    main()

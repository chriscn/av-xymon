from bs4 import BeautifulSoup

with open('nongreen.html', 'r') as nongreen_raw:
    nongreen_parsed = BeautifulSoup(nongreen_raw, 'html.parser')

    lines = nongreen_parsed.body.find_all('tr', attrs={'class':'line'})

    lines = sorted(lines, key=lambda x: x.td.font.text)

    table = nongreen_parsed.body.find_all('tbody')[1]

    for line in lines:
      table.append(line)

    with open('nongreen_sorted.html', 'w') as nongreen_output:
        nongreen_output.write(nongreen_parsed.prettify())

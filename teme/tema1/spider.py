import requests
from bs4 import BeautifulSoup

URL = 'https://www.formula1.com/en/racing/2022.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
stage_table = soup.find_all('div', 'col-12 col-sm-6 col-lg-4 col-xl-3', limit=24)

file = open('data.txt','w')

for stage in stage_table:
    # data_tracking = stage.find('a')['data-tracking']
    text = stage.find('div', 'event-title f1--xxs').text
    legend = stage.find('legend', 'card-title f1-uppercase f1-color--warmRed').text
    start_date = stage.find('span', 'start-date').text
    end_date = stage.find('span', 'end-date').text
    try:
        month = stage.find('span', 'month-wrapper f1-wide--xxs').text
    except AttributeError:
        pass
    try:
        title = stage.find('div', 'event-place').text
    except KeyError:
        title = stage.find('div', 'event-place d-block').text
    file.write(f'The {legend} will begin in {title} between {start_date} and {end_date} in {month}:\n\t{text}')
file.close()
# team_rows = stage_table.find_all('tr', attrs={'echipa_row'})
# for team in team_rows:
#     team_cell = team.find('a')
#     team_name = team_cell.data-tracking.strip()
#     teams.append(team_name)


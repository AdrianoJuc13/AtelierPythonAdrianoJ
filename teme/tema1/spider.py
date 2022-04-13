import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
teams = []
stage_table = soup.find('class = clasament_general white-shadow etape_meciuri')
# team_rows = stage_table.find_all('tr', attrs={'echipa_row'})
# #
# # for team in team_rows:
# #     team_cell = team.find('a')
# #     team_name = team_cell.text.strip()
# #     teams.append(team_name)
# print(team_rows)

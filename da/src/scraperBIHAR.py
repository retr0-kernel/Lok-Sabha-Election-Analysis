import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S04.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
party_seats = []
grid_boxes = soup.find_all("div", class_="grid-box")
for box in grid_boxes:
    party_name = box.find("h4").text
    seats_won = box.find("h2").text
    party_seats.append({"Party": party_name, "Seats": int(seats_won)})
script = soup.find("script", string=lambda text: text and "var xValues" in text).string

x_values_pattern = re.compile(r"var xValues = \[(.*?)\];", re.DOTALL)
y_values_pattern = re.compile(r"var yValues = \[(.*?)\];", re.DOTALL)

x_values_match = x_values_pattern.search(script)
y_values_match = y_values_pattern.search(script)

x_values = x_values_match.group(1).split(',')
y_values = y_values_match.group(1).split(',')

x_values = [x.strip().strip("'").strip('"') for x in x_values]
y_values = [y.strip() for y in y_values]

x_values = [x for x in x_values if x]
y_values = [int(y) for y in y_values if y.isdigit()]

party_vote_share = []
for i in range(len(x_values)):
    party_vote_share.append({"Party": x_values[i], "Votes": y_values[i]})

constituency_results = []
dropdown = soup.find("select", id="ctl00_ContentPlaceHolder1_Result1_ddlState")
for option in dropdown.find_all("option"):
    if option['value']:
        constituency = option.text.split("-")
        constituency_results.append({"Constituency": constituency[0].strip(), "Details": constituency[1].strip()})

df_seats = pd.DataFrame(party_seats)
df_vote_share = pd.DataFrame(party_vote_share)
df_constituencies = pd.DataFrame(constituency_results)

df_seats.plot(kind="bar", x="Party", y="Seats", title="Party-wise Seat Distribution", legend=False)
plt.ylabel("Seats Won")
plt.show()

df_vote_share.plot(kind="pie", y="Votes", labels=df_vote_share["Party"], autopct='%1.1f%%', title="Party-wise Vote Share")
plt.ylabel("")
plt.show()

print("Party-wise Seat Distribution:\n", df_seats)
print("\nParty-wise Vote Share:\n", df_vote_share)
print("\nConstituency-wise Results:\n", df_constituencies)

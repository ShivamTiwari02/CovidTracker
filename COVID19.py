import requests
from bs4 import BeautifulSoup

inp = 0
inp = int(input("\nEnter choice \n1:World\n2:India\n3:United States\n4:Exit\n"))
while inp != 4:

    if inp == 1:
        url = "https://www.worldometers.info/coronavirus/"
    elif inp == 2:
        url = "https://www.worldometers.info/coronavirus/country/india/"
    elif inp == 3:
        url = "https://www.worldometers.info/coronavirus/country/us/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    data = soup.find_all("div", class_="maincounter-number")
    print("Total Cases: ", data[0].text.strip())
    print("Total Deaths: ", data[1].text.strip())
    print("Total Recovered: ", data[2].text.strip())
    inp = int(input("\n\n\nEnter choice \n1:World\n2:India\n3:United States\n4:Exit\n"))
print("THANK YOU")

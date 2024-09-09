import requests
from bs4 import BeautifulSoup
import pandas as np
import re

url = "https://www.ndtv.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")


h1Tags = soup.find_all('h1')
classTag = "crd_ttl8"
headings = soup.find_all(class_=classTag)
allHeadings = []
for heading in headings:
    heading = heading.get_text()
    heading = re.sub(r'[^\w\s]','',heading)
    heading = re.sub(r'\s+', ' ', heading).strip()
    allHeadings.append(heading)
    print(heading)

for heading in h1Tags:
    heading = heading.get_text()
    heading = re.sub(r'[^\w\s]','',heading)
    heading = re.sub(r'\s+', ' ', heading).strip()
    allHeadings.append(heading)
    print(heading)




newDataframe = np.DataFrame(data=allHeadings,columns=['Heading'])
print(newDataframe)

newDataframe.to_excel("Headings.xlsx")
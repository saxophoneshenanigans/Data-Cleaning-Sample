import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

file = open('Sample Data Source.html', 'r')
data = file.read()
S = BeautifulSoup(data, 'lxml')
table = S.tbody
test = []
part = []
tags = [e for e in table.children if e.name is not None and e.text is not None]
for tag in tags:
    part.append(tag.select('td:nth-of-type(1)')[0])
    part.append(tag.select('td:nth-of-type(2)'))
    part.append(tag.select('td:nth-of-type(3)'))
    part.append(tag.select('td:nth-of-type(4)'))
    part.append(tag.select('td:nth-of-type(5)'))
    part.append(tag.select('td:nth-of-type(6)'))
    part.append(tag.select('td:nth-of-type(7)'))
    part.append(tag.select('td:nth-of-type(8)'))
    part.append(tag.select('td:nth-of-type(9)'))
    part.append(tag.select('td:nth-of-type(10)'))
    part.append(tag.select('td:nth-of-type(11)'))
    test.append(part)
    part = []
df = pd.DataFrame(test)
df[0] = [x.text for x in df[0]]
df[1] = [x[0].text if x != [] else np.nan for x in df[1]]
df[2] = [x[0].text if x != [] else np.nan for x in df[2]]
df[3] = [x[0].text if x != [] else np.nan for x in df[3]]
df[4] = [x[0].text if x != [] else np.nan for x in df[4]]
df[5] = [x[0].text if x != [] else np.nan for x in df[5]]
df[6] = [x[0].text if x != [] else np.nan for x in df[6]]
df[7] = [x[0].text if x != [] else np.nan for x in df[7]]
df[8] = [x[0].text if x != [] else np.nan for x in df[8]]
df[9] = [x[0].text if x != [] else np.nan for x in df[9]]
notes = [x for x in df[0]]#[1:]
df[10] = notes#.append(np.nan)
df[10].shift(-1)
df[10] = df[10].shift(-1)
df.columns = ['Item Number', 'Customer-Location Number', 'Requested By', 'Date Received', 'Time Received', 'Date Completed', 'Time Completed', 'Department', 'Location ID', 'Issue', 'Notes']
df = df.iloc[2:]
df.dropna(inplace=True)
df

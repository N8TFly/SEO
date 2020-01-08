import platform
import seoanalyzer
from seoanalyzer import analyze
import requests
import pandas as pd
import json

with open('seo_info.txt', 'r') as file:
    data = file.read()
    data = str(data)
    d2 = eval(data)
    pdata = pd.DataFrame.from_dict(d2['pages'])

print(pdata.keys())
print(pdata['warnings'][0])




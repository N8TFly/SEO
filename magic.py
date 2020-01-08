import platform
import seoanalyzer
from seoanalyzer import analyze
import requests
import pandas as pd

file = open('seo_info.txt', 'w')

output = analyze("https://www.website.nl", "https://www.website.nl/sitemap.xml")
file.write(str(output))
file.close()
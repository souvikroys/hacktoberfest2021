print("============================================================="); 
print("\tSimple-CMD\tC0d3d by : Souvik_Roy");  
print("============================================================="); 
print("\t\tEmail : souvik09243@gmail.com");  
print("=============================================================");
print("\tURL-Parser | Format : 'https://example.com'");
print("=============================================================\n");

import requests
from bs4 import BeautifulSoup as bs

url=input("Enter the URL: ")
try:	
	r=requests.get(url)
	soup=bs(r.content,"html.parser")
	anchor_tag=soup.find_all('a')
	for link in anchor_tag:
    		print(link.get('href'))
except:
	print("Something went Wrong !")

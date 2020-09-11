# Python 3

#Search a string in a webpage query with diferent usert-agent

import requests

Str2find = 'samotik'

with open('usersagents.txt') as myFile:

	for useragent in myFile:

		useragent = useragent.replace('\n', '')

		headers = {"User-Agent": useragent}

		response = requests.get("https://parqueexplora.org", headers=headers)

		if (response.text.find(Str2find) != -1): 

			print (useragent + " ---> Contains given substring") 

			print(response.text)

		else: 
			print (useragent + " ---> Doesn't contains given substring") 



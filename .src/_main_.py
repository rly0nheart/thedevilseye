import os
import sys
import json
import logging
import random
import requests
import argparse
from pprint import pprint
from datetime import datetime
sys.path.append(os.getcwd()+"/.lib/")
sys.path.append(os.getcwd()+"/.src/")
from headers import user_agents
from colors import red, white, green, reset


start = datetime.now()
class thedevilseye:
	def __init__(self,args):
		self.api = f"https://darksearch.io/api/search?query={args.query}&page={int(args.page)}"
		self.headers = {"User-Agent": f"{random.choice(user_agents)}"}
		self.response = requests.get(self.api, headers=self.headers).json()
		
	def on_connection(self):
		count=0
		if args.raw:
			print(red)
			pprint(self.response)
			print(reset)
		else:
			# Loop through the response object
			for result in self.response["data"]:
				count+=1
				data = {"total": self.response['total'],
				             "result#": count,
				             "title": result['title'],
				             ".onion link": result['link'],
				             "description": result['description'],
				}
				print(f"\n{white}{args.query}{reset}")
				for key,value in data.items():
				    print(f"{white}├─ {key}: {red}{value}{reset}")
				
				if args.output:
					self.output(data)
					if args.verbose:
						print(f"{white}[{green}+{white}] Output written to ./{green}{args.output}{reset}")

					
		# Promp user to enter result number once all the iterations complete
		print(f"{white}={reset}"*100)	
		page = input(f"{white}[{green}>{white}] Next page ({green}1-{self.response['total']}{white}) >>  ")
		args.page = page
	
	# Write output to a specified file		
	def output(self,data):
		if args.raw:
			object = json.dumps(self.response, indent=4)
			with open(args.output, "a") as raw:
				raw.write(object)
				raw.close()
				
		else:
			with open(args.output, "a") as file:
				for key,value in data.items():
					file.write(f"├─ {key}: {value}\n")
				file.close()
				
				
# Parse command line arguments
parser = argparse.ArgumentParser(description=f"{red}The Devil's Eye:{white} is a  {red}darkweb{white} OSINT tool, that extracts information (.onion links, descriptions) from the darkweb without requiring a Tor network.  developed by {green}Richard Mwewa {white}| https://github.com/{red}rlyonheart{reset}")
parser.add_argument("query", help=f"{white}search query. {red}Note{white}: if search query contains spaces, put it inside quote ('') symbols{reset}")
parser.add_argument("-p","--page",help=f"{white}page number ({red}default is 1{white}){reset}", metavar=f"{white}[NUMBER]{reset}", dest="page", default=1)
parser.add_argument("-r", "--raw", help=f"{white}return output in raw {red}json{white} format{reset}", dest="raw", action="store_true")
parser.add_argument("-o", "--output", help=f"{white}write output to a specified {red}file{reset}", metavar=f"{white}[FILENAME]{reset}", dest="output")
parser.add_argument("-v", "--verbose", help=f"{white}run thelordseye in {red}verbose{white} mode({red}show network logs, errors and notices{white}){reset}", dest="verbose", action="store_true")
args = parser.parse_args()

# The current (2022) edition of thedevilseye is called Hellfire

import logging
import requests
import argparse
import urllib.request
from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
from lib.colors import red,white,green,reset

class thedevilseye:
    def __init__(self,args,start_time):
        if args.update:
        	self.update()
        elif args.jailbait:
        	self.uri = f'https://ahmia.fi/search/?q=jailbait'
        elif args.i2p:
            self.uri = f'https://ahmia.fi/search/i2p/?q={args.query}'
        elif args.licence:
        	exit(self.licence())
        elif args.query:
            self.uri = f'https://ahmia.fi/search/?q={args.query}'
        else:
            exit(f'{white}eye: use {green}-h{white} or {green}--help{white} to show help message.{reset}')
    
    # Fetching search query results        
    def search(self):
        request = requests.get(self.uri)
        soup = BeautifulSoup(request.text, 'html.parser')
        
        if soup.ol is None:
            if args.verbose:
            	logging.warning(f'{white}No results found for {args.query}. Try a different search.{reset}')
            	exit()
        else:
            a_string = args.query
            if args.verbose:
            	if args.jailbait:
            		a_string = 'JAILBAIT'
            	print(f'\n\t{a_string} — thedevilseye | ',start_time.strftime('%A %d %B %Y, %I:%M:%S%p'))
            print(soup.ol.get_text())
        	
        if args.dump:
            self.dump(soup)
            
   # Dumping output to a specified file 
    def dump(self,soup):
        with open(args.dump, 'w') as file:
            file.write(soup.ol.get_text())
            file.close()
        if args.verbose:
        	logging.info(f'{white}Output dumped to {green}{args.dump}{reset}')
        	
     # Reading LICENSE file  		
    def licence(self):
        with open('LICENSE', 'r') as file:
        	content = file.read()
        	file.close()
        	return content
        	
    # Update program
    def update(self):
    	files_to_fetch = ['src/main.py','eye','lib/banner.py','lib/colors.py','requirements.txt','README.md','LICENSE']
    	for file in tqdm(files_to_fetch,desc=f'{white}* Fetching update(s){reset}'):
    		data = urllib.request.urlopen(f'https://raw.githubusercontent.com/rly0nheart/thedevilseye/master/{file}').read()
    		with open(file, 'wb') as code:
    			code.write(data)
    			code.close()
    				
    	print(f'{white}* {red}thedevilseye{white} updated successfully. Re-run program.{reset}')
    	exit()
    	

start_time = datetime.now()
parser = argparse.ArgumentParser(description=f'{white}Darkweb .onion link(s) extracting tool{reset}',epilog=f'{white}thedevilseye extracts information (.onion links, descriptions) from the {red}darkweb{white} without requiring a Tor network. Developed by Richard Mwewa | https://about.me/{green}rly0nheart{reset}')
parser.add_argument('-q','--query',metavar=f'{white}search-query{reset}', help=f'{white}return results related to the search query{reset}')
parser.add_argument('-i','--i2p',help=f'{white}switch to i2p network search{reset}', action='store_true')
parser.add_argument('--jailbait',help=f'{white}Ahmia.fi self-help program;  {red}The self-help program is primarily intended for people who are worried about their interest, thoughts, feelings or actions concerning children.{reset}',action='store_true')
parser.add_argument('-d','--dump', metavar=f'{white}path/to/file{reset}', help=f'{white}dump output to a specified file{reset}')
parser.add_argument('-u','--update',help=f'{white}update thedevilseye to the newest version{reset}',action='store_true')
parser.add_argument('-v','--verbose',help=f'{white}enable verbosity{reset}',action='store_true')
parser.add_argument('--release-tag',help=f'{white}show program\'s release tag and exit{reset}',version=f'{white}Hellfire#5 Released on 18th February 2022{reset}',action='version')
parser.add_argument('--licence','--license',help=f'show program\'s licen[sc]e and exit',action='store_true')
args = parser.parse_args()
if args.verbose:
	logging.basicConfig(format=f'{white}* %(message)s{reset}',level=logging.DEBUG)

# As of 23rd January 2022, thedevilseye uses Ahmia.fi resources
# The current (2022) edition of thedevilseye is called Hellfire

import logging
import requests
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
from lib.colors import red,white,green,yellow,reset

class thedevilseye:
    def __init__(self,args,start_time):
        if args.i2p:
            self.uri = f'https://ahmia.fi/search/i2p/?q={args.query}'
        else:
        	self.uri = f'https://ahmia.fi/search/?q={args.query}'
            
    def search(self):
        request = requests.get(self.uri)
        soup = BeautifulSoup(request.text, 'html.parser')
        
        if soup.ol is None:
            if args.verbose:
            	exit(f'{white}[{red}-{white}] No results found for {args.query}. Try a different search.{reset}')
        else:
            if args.verbose:
            	print(f'\n\t{white}{args.query} — thedevilseye | ',start_time.strftime('%A %d %Y, %I:%M:%S%p'),reset)
            print(soup.ol.get_text())
        	
        if args.dump:
            self.dump(soup)
            
    
    def dump(self,soup):
        with open(args.dump, 'w') as file:
            file.write(soup.ol.get_text())
            file.close()
        if args.verbose:
        	print(f'{white}[{green}+{white}] Output dumped to {green}{args.dump}{reset}') 	


start_time = datetime.now()
parser = argparse.ArgumentParser(description=f'{white}Darkweb OSINT tool{reset}',epilog=f'{white}thedevilseye extracts information (.onion links, descriptions) from the {red}darkweb{white} without requiring a Tor network. Developed by Richard Mwewa | https://about.me/{green}rly0nheart{reset}')
parser.add_argument('query', help=f'{white}search query{reset}')
parser.add_argument('-i','--i2p', help=f'{white}switch to i2p network search{reset}', action='store_true')
parser.add_argument('-d','--dump', metavar=f'{white}path/to/file{reset}', help=f'{white}dump output to a file{reset}')
parser.add_argument('--version',version=f'{white}2022.1.1.0-hellfire Released on 29rd January 2022{reset}',action='version')
parser.add_argument('-v','--verbose',help=f'{white}enable verbosity{reset}',action='store_true')
args = parser.parse_args()
if args.verbose:
	logging.basicConfig(format=f"{white}[{green}~{white}] %(message)s{reset}",level=logging.DEBUG)

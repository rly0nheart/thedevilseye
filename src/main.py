# The current (2022) edition of thedevilseye is called Hellfire

import logging
import requests
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
from lib.colors import red,white,green,reset

class thedevilseye:
    def __init__(self,args,start_time):
        if args.i2p:
            self.uri = f'https://ahmia.fi/search/i2p/?q={args.query}'
        elif args.licence:
        	exit(self.licence())
        elif args.query:
            self.uri = f'https://ahmia.fi/search/?q={args.query}'
        else:
            exit(f'{white}eye: use {green}-h{white} or {green}--help{white} to view help message.{reset}')
            
    def search(self):
        request = requests.get(self.uri)
        soup = BeautifulSoup(request.text, 'html.parser')
        
        if soup.ol is None:
            if args.verbose:
            	logging.warning(f'{white}No results found for {args.query}. Try a different search.{reset}')
            	exit()
        else:
            if args.verbose:
            	print(f'\n\t{args.query} — thedevilseye | ',start_time.strftime('%A %d %B %Y, %I:%M:%S%p'))
            print(soup.ol.get_text())
        	
        if args.dump:
            self.dump(soup)
            
    
    def dump(self,soup):
        with open(args.dump, 'w') as file:
            file.write(soup.ol.get_text())
            file.close()
        if args.verbose:
        	logging.info(f'{white}Output dumped to {green}{args.dump}{reset}')
        	
        		
    def licence(self):
        with open('LICENSE', 'r') as file:
        	content = file.read()
        	file.close()
        	return content


start_time = datetime.now()
parser = argparse.ArgumentParser(description=f'{white}Darkweb .onion link(s) extracting tool{reset}',epilog=f'{white}thedevilseye extracts information (.onion links, descriptions) from the {red}darkweb{white} without requiring a Tor network. Developed by Richard Mwewa | https://about.me/{green}rly0nheart{reset}')
parser.add_argument('-q','--query',metavar=f'{white}search-query{reset}', help=f'{white}return results related to the search query{reset}')
parser.add_argument('-i','--i2p', help=f'{white}switch to i2p network search{reset}', action='store_true')
parser.add_argument('-d','--dump', metavar=f'{white}path/to/file{reset}', help=f'{white}dump output to a specified file{reset}')
parser.add_argument('-v','--verbose',help=f'{white}enable verbosity{reset}',action='store_true')
parser.add_argument('--version',version=f'{white}2022.1.3.0-hellfire#4 Released on 15th February 2022{reset}',action='version')
parser.add_argument('--licence','--license',help=f'view program\'s licen(sc)e and exit',action='store_true')
args = parser.parse_args()
if args.verbose:
	logging.basicConfig(format=f"{white}* %(message)s{reset}",level=logging.DEBUG)
	

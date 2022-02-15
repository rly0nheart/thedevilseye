#!/usr/bin/env python3

from src.main import *
from datetime import datetime
from lib.colors import red,white,green,reset

print(banner)
if __name__ == '__main__':
    while True:
        try:
        	thedevilseye(args,start_time).search()
        	break
        	
        except KeyboardInterrupt:
        	if args.verbose:
        		logging.info(f'{white}Process interrupted with {red}Ctrl{white}+{red}C{reset}')
        		break
        	break
        	
        except Exception as e:
            if args.verbose:
            	logging.error(f'{white}An error occured: {red}{e}{reset}')
            
            
    if args.verbose:
    	logging.info(f'{white}Finished in {green}{datetime.now()-start_time}{white} seconds.{reset}')
    exit()

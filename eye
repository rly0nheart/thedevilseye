#!/usr/bin/env python3

from src.main import *
from datetime import datetime
from lib.colors import red,white,green,reset

if __name__ == '__main__':
    while True:
        try:
        	thedevilseye(args).search()
        	break
        	
        except KeyboardInterrupt:
        	if args.verbose:
        		print(f'\n{white}[{red}x{white}] Process interrupted with {red}Ctrl{white}+{red}C{reset}')
        		break
        	break
        	
        except Exception as e:
            if args.verbose:
            	print(f'{white}[{red}!{white}] An error occured: {red}{e}{reset}')
            
            
    if args.verbose:
    	exit(f'{white}[{green}-{white}] Finished in {green}{datetime.now()-start_time}{white} seconds.{reset}')
    exit()

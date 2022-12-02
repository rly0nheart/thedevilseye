import time
import argparse
from rich.tree import Tree
from selenium import webdriver
from rich import print as xprint
from selenium.webdriver.common.by import By
 
 
def create_parser():
    parser = argparse.ArgumentParser(description="Darkweb .onion link(s) extracting tool  — by Richard Mwewa | https://about.me/rly0nheart",epilog="thedevilseye scrapes darkweb search engines and gets information (.onion links, descriptions) requiring a Tor network. Developed by Richard Mwewa | https://about.me/rly0nheart")
    parser.add_argument('engine', help='engine', choices=['ahmia.fi', 'tor.link'])
    parser.add_argument('-q', '--query', help='search query')
    parser.add_argument("-d","--dump", metavar="path/to/file", help=argparse.SUPPRESS)
    return parser
 
 
class TheDevilsEye:
 
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
 
    def webdriver_get(self, url, class_name, wait_time=5):
        self.driver.get(url)
        time.sleep(wait_time)
        try:
            results = self.driver.find_elements(By.CLASS_NAME, class_name)
        except Exception as e:
            xprint(f'[[red]ERROR[/]] An error occurred: [red]{e}[/]')
            return []
 
        xprint(f'[[green]POSITIVE[/]] Found [green]{len(results)}[/] results')
        return results
 
    def search_ahmia_fi(self, query):
        url = f"https://ahmia.fi/search/?q={query}"
        results = self.webdriver_get(url, 'result')
        for idx, result in enumerate(results, start=1):
            result_tree = Tree(f'\n{idx} - {query}')
            result_tree.add('Description: ' + result.find_element(By.TAG_NAME, 'p').text)
            result_tree.add('Onion Link: ' + result.find_element(By.TAG_NAME,'cite').text)
            result_tree.add('Last seen: ' + result.find_element(By.TAG_NAME,'span').text)
            xprint(result_tree)
            print('-' * 74)
 
        self.driver.close()
 
    def search_tor_link(self, query):
        url = f"https://tor.link/?q={query}"
        results = self.webdriver_get(url, 'col-md-9', wait_time=15)
        for idx, result in enumerate(results, start=1):
            print(f'\n{idx}:')
            print('Description: ', result.find_element(By.TAG_NAME,'p').text)
            print('Onion Link: ', result.find_element(By.XPATH, f'/html/body/div[3]/div/div/ul/li[1]/div[2]/a').text)
            print('-' * 74)
 
        self.driver.close()

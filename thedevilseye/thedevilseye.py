import time
import argparse
from rich.tree import Tree
from datetime import datetime
from selenium import webdriver
from rich import print as xprint
from selenium.webdriver.common.by import By
 
 
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
 
        xprint(f'[[green]FOUND[/]] Found [green]{len(results)}[/] results')
        return results
 
    def search_ahmia_fi(self, query):
        url = f"https://ahmia.fi/search/?q={query}"
        results = self.webdriver_get(url, 'result')
        for count, result in enumerate(results, start=1):
            result_tree = Tree(f'\n[green]{count}[/]/[green]{len(results)}[/] - {query}')
            result_tree.add('Description: ' + result.find_element(By.TAG_NAME, 'p').text)
            result_tree.add('Onion Link: ' + result.find_element(By.TAG_NAME,'cite').text)
            result_tree.add('Last seen: ' + result.find_element(By.TAG_NAME,'span').text)
            xprint(result_tree)
            xprint('=' * 74)
 
        self.driver.close()

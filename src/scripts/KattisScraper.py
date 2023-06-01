from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

class KattisScraper:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.session = requests.Session()
        self.login_url = "https://open.kattis.com/login/email?"

    def login(self):
        # Get the CSRF token
        login_page = self.session.get(self.login_url)
        soup = BeautifulSoup(login_page.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

        # Login
        login_data = {
            'user': self.username,
            'password': self.password,
            'csrf_token': csrf_token,
        }
        self.session.post(self.login_url, data=login_data)

    def get_problems(self):
        problems_url = 'https://open.kattis.com/problems?show_solved=on&show_partial=off&show_tried=off&show_untried=off&order=difficulty_category'
        problem_rows = []

        while problems_url:
            page = self.session.get(problems_url)
            soup = BeautifulSoup(page.text, 'html.parser')
            rows = soup.find('table', {'class': 'table2'}).find('tbody').find_all('tr')
            problem_rows.extend(rows)
            pagination_div = soup.find('div', {'id': 'problem_list_paginate'})
            next_button = pagination_div.find_all('a')[-1]
            if 'button-basic-disabled' in next_button.get('class'):
                problems_url = None
            else:
                problems_url = 'https://open.kattis.com/problems' + next_button.get('href')
        
        return problem_rows


def extract_id(url: str):
    return url.split('/')[-1]

scraper = KattisScraper()
scraper.login()
problem_rows = scraper.get_problems()

base_dir = 'src/problems/'

for row in problem_rows:
    url = row.find('a').get('href')
    problem_id = extract_id(url)
    problem_dir = os.path.join(base_dir, problem_id)
    os.makedirs(problem_dir, exist_ok=True)
    name = row.find('a').text
    difficulty = row.find('span', {'class': 'difficulty_number'}).text

    metadata_file_path = os.path.join(problem_dir, 'metadata.txt')
    with open(metadata_file_path, 'w') as f:
        f.write(f"ID: {problem_id}\n")
        f.write(f"URL: {url}\n")
        f.write(f"Difficulty: {difficulty}\n")
        f.write(f"Name: {name}\n")
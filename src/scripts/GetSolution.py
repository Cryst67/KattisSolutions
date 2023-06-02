import os
from dotenv import load_dotenv
from KattisScraper import KattisScraper
from bs4 import BeautifulSoup

load_dotenv()
scraper = KattisScraper()
scraper.login()
base_dir = 'src/problems/'
problem_dirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

def has_data_submission_id(tag):
    return tag.has_attr('data-submission-id')

for problem_dir in problem_dirs:
    if os.path.exists(os.path.join(base_dir, problem_dir, 'solutions')): continue
    link = f"https://open.kattis.com/users/{os.getenv('KATTIS_USERNAME')}/submissions/{problem_dir}?status=AC"
    solutions_page = scraper.session.get(link)
    soup = BeautifulSoup(solutions_page.text, 'html.parser')
    table = soup.find('tbody').find_all(has_data_submission_id)
    for row in table:
        a = row.find('a', string='View Details')
        link = "https://open.kattis.com" + a.get('href')
        submission_page = scraper.session.get(link)
        submission_soup = BeautifulSoup(submission_page.text, 'html.parser')
        file_source_content_divs = submission_soup.find_all('div', {'class': 'file_source-content-file'})
        for file_source_content_div in file_source_content_divs:
            file_download_link = file_source_content_div.find('a').get('href')
            file_name = file_source_content_div.find('h3').text
            solutions_dir = os.path.join(base_dir, problem_dir, 'solutions')
            os.makedirs(solutions_dir, exist_ok=True)
            solution_file = scraper.session.get('https://open.kattis.com' + file_download_link, stream=True)
            # Handle potential naming conflicts if multiple solutions have the same file name
            file_name_path = os.path.join(solutions_dir, file_name)
            if os.path.exists(file_name_path):
                base_name, extension = os.path.splitext(file_name)
                i = 1
                while os.path.exists(os.path.join(solutions_dir, f"{base_name}_{i}{extension}")):
                    i += 1
                file_name = f"{base_name}_{i}{extension}"
            with open(os.path.join(solutions_dir, file_name), 'wb') as f:
                for chunk in solution_file.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

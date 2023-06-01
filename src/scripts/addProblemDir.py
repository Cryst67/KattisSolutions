from KattisScraper import KattisScraper
import os

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
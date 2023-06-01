import os
import zipfile
from KattisScraper import KattisScraper
from bs4 import BeautifulSoup

scraper = KattisScraper()
scraper.login()
base_dir = 'src/problems/'
problem_dirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

for problem_dir in problem_dirs:
    dirs = os.listdir(os.path.join(base_dir, problem_dir))
    if 'sample_in' in dirs:
        continue
    print(problem_dir)
    metadata_file_path = os.path.join(base_dir, problem_dir, 'metadata.txt')
    with open(metadata_file_path, 'r') as f:
        lines = f.readlines()
        url = [line.split(": ")[1].strip() for line in lines if "URL" in line][0]
    problem_page_url = 'https://open.kattis.com' + url + '?tab=metadata'
    problem_page = scraper.session.get(problem_page_url)
    soup = BeautifulSoup(problem_page.text, 'html.parser')
    download_link_div = soup.find('div', {'data-name': 'metadata_item-downloads'})
    if not download_link_div: continue
    download_link = download_link_div.find('a').get('href')
    if not download_link.startswith('https://'):
        download_link = 'https://open.kattis.com' + download_link
    os.chdir(os.path.join(base_dir, problem_dir))
    response = scraper.session.get(download_link, stream=True)
    with open('samples.zip', 'wb') as out_file:
        out_file.write(response.content)
    try:
        with zipfile.ZipFile('samples.zip', 'r') as zip_ref:
            zip_ref.extractall('sample_in')
    except zipfile.BadZipFile:
        pass
    os.remove('samples.zip')
    os.chdir('../../../')

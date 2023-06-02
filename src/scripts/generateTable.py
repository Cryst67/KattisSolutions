import os

ext_to_logo = {
    'cpp': 'cpp.png',
    'java': 'java.png',
    'js': 'js.png',
    'py': 'py.png',
    'rb': 'ruby.png'
}

base_dir = 'src/problems/'
problem_dirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

table_rows = []

for problem in problem_dirs:
    with open(os.path.join(base_dir, problem, 'metadata.txt'), 'r') as f:
        lines = f.readlines()
        name = [line.split(": ")[1].strip() for line in lines if "Name" in line][0]
        url = [line.split(": ")[1].strip() for line in lines if "URL" in line][0]
        problem_link = f"[{name}](https://open.kattis.com{url})"
    solution_links = []
    solution_files = os.listdir(os.path.join(base_dir, problem, 'solutions'))
    for solution in solution_files:
        ext = solution.split('.')[-1]
        logo = ext_to_logo.get(ext, 'default.png')
        solution_path = f"{base_dir}/{problem}/solutions/{solution}"
        solution_link = f"<a href='{solution_path}'><img src='assets/logos/{logo}' width='30'></a>"
        solution_links.append(solution_link)
    table_rows.append(f"| {problem_link} | {' '.join(solution_links)} |")

with open('TABLE.md', 'a') as f:
    f.write("\n| Problem | Solutions |\n")
    f.write("| --- | --- |\n")
    for row in table_rows:
        f.write(row + "\n")

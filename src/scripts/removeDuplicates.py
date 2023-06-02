import os
import hashlib

base_dir = 'src/problems/'
problem_dirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

for problem in problem_dirs:
    solutions_dir = os.path.join(base_dir, problem, 'solutions')
    if not os.path.exists(solutions_dir):
        continue
    solution_files = os.listdir(solutions_dir)
    
    # If there is only one solution file, skip the duplication check
    if len(solution_files) == 1:
        continue

    contents_hash_set = set()
    for file in solution_files:
        with open(os.path.join(solutions_dir, file), 'r') as f:
            content = f.read()
            content_hash = hashlib.md5(content.encode()).hexdigest() # Hash the content for quick comparison
            if content_hash in contents_hash_set: # If hash exists, remove the file
                os.remove(os.path.join(solutions_dir, file))
            else:
                contents_hash_set.add(content_hash)

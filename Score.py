import os
SCORES_FILE = 'Scores.txt'
def add_score(difficulty):
    points = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r+') as file:
            current_score = int(file.read())
            file.seek(0)
            file.write(str(current_score + points))
    else:
        with open(SCORES_FILE, 'w') as file:
            file.write(str(points))
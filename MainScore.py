from flask import Flask

app = Flask(__name__)
SCORES_FILE = 'Scores.txt'

def read_score():
    try:
        with open(SCORES_FILE, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 'Score file not found'
    except ValueError:
        return 'Invalid score value'

score = read_score()

@app.route('/')
def score_server():
    color = 'red' if isinstance(score, str) else 'black'
    escaped_score = str(score)

    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score" style="color:{color}">{escaped_score}</div></h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

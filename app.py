from flask import Flask

app = Flask(__name__)

@app.get('/')
def main():
    return 'movie api crud app'

if __name__ == "__main__":
    app.run(debug=True)
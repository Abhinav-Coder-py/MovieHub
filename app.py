from flask import Flask

app = Flask(__name__)

@app.get('/')
def main():
    return 'this is a movie api crud app'

if __name__ == "__main__":
    app.run(debug=True)
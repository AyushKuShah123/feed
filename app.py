from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')  # Change to your HTML file name
    return render_template('try.html')  # Change to your HTML file name

if __name__ == '__main__':
    app.run(debug=True)

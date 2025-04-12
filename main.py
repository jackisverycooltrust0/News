from flask import Flask, render_template, request
from config import API_KEY
import requests

app = Flask(__name__)



@app.route("/")
def index():
    query = request.args.get('query','latest')
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    
    response = requests.get(url)
    news_data = response.json()
    print(news_data)

    articles = news_data.get("articles",[])

    return render_template('index.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)










if __name__ == "__main__":
    app.run(debug=True)
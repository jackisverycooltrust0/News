from flask import Flask, render_template, request
# from config import API_KEY
import requests
import os

app = Flask(__name__)


API_KEY = os.environ.get('API_KEY')
@app.route("/")
def index():
    query = request.args.get('query', 'latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])

    filtered_articles = [
        article for article in articles 
        if 'Yahoo' not in article['source']['name'] and 'removed' not in article['title'].lower()
    ]
    return render_template('index.html', articles=articles)

if __name__ == "__main__":                                                                                                                                  
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
                                                                                                                           

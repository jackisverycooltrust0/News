from flask import Flask, render_template, request
# from config import API_KEY
import requests
import os

app = Flask(__name__)


API_KEY = os.environ.get('API_KEY')
@app.route("/")
def index():
    query = request.args.get('query', 'latest')
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  

        try:
            news_data = response.json()
        except ValueError:
            news_data = {"articles": []}  

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        news_data = {"articles": []} 

    articles = news_data.get("articles", [])

    return render_template('index.html', articles=articles)


       
if __name__ == "__main__":                                                                                                                                  
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))
                                                                                                                           

##############Scraping keywords#########
from flask import Flask, request

from bs4 import BeautifulSoup as bs
import requests

# 커뮤니티 사이트에서 검색된 keyword로 도출된 단어들 crawling
def search(keyword):
    url = f"https://www.inven.co.kr/search/maple/article/{keyword}/1?sort=recency"
    response = requests.get(url)
    maple_page = response.text

    soup = bs(maple_page, "html.parser")

    # 메이플 인벤에서 keyword로 검색된 elements
    elements = soup.find_all(name="a", class_="name")
    keywords = [];

    for element in elements:
        title_words = element.get_text().split()
        for word in title_words:
            if word != keyword:
                keywords.append(word)
    return keywords

# Flask server
app = Flask(__name__, static_folder="./client")

@app.route("/search", methods=["POST"])
def search_keyword():
    search_input = request.json["keyword"]
    if search_input:
        data = search(search_input)
        return {
            "keywords": data
        }
    return "No given input."

@app.route("/")
def hello_world():
    return "Main Page"

if __name__ == '__main__':
    app.run(debug = True)

















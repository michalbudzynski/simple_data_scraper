import requests
from bs4 import BeautifulSoup
import sys

response = requests.get("http://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".question-summary")
sys.stdout = open("filename.txt", "w")

for question in questions:
    print("title: " + question.select_one(".question-hyperlink").getText())
    print("author: " + question.select_one(".user-details > a").getText())
    print("score: " + question.select_one(".vote-count-post").getText())

sys.stdout.close()

from tkinter import *
from PIL import Image, ImageTk
import os, datetime, json, requests


with open("details.txt") as f:
    data = f.read()
    info = data.split("\n")

news = []
def news_teller():
    news_channel = "Hacker-News"
    try:
        url = f"https://newsapi.org/v2/top-headlines?sources={news_channel}&apiKey={info[0]}"
        news = requests.get(url).text
        news_dict = json.loads(news)
        # print(news_dict['articles'])
        arts = news_dict['articles']
        a = len(arts)
        for index, articles in enumerate(arts):
            if index != a - 1:
                print(f"{articles['title']}\nMore-{articles['url']}\n")
                news.append(articles['title'])
            else:
                print(f"{articles['title']}\nMore-{articles['url']}\n")
    except Exception as e:
        print(e)

path = os.getcwd()
today_time = datetime.datetime.now().date()
root = Tk()

root.geometry("1366x768")
root.minsize("1360", "760")
root.maxsize("1366", "768")
root.title("Newspaper")
main_heading = Label(text="Hindustan Times", bg="yellow",
fg="blue", font="arial 45 bold", relief=RAISED, padx=5, pady=5)
date_lable = Label(text=f"{today_time}", font="arial 25 italic")

main_heading.pack(side=TOP, anchor="n", fill=X)
date_lable.pack(fill=X)

root.mainloop()
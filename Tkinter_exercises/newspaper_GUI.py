from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import os, datetime, json, requests, random

# print(os.getcwd())
with open("details.txt") as f:
    data = f.read()
    info = data.split("\n")

news_list_1 = []
def news_teller():
    news_channels = ["Hacker-News", "Ars-Technica", "NHL-News", "Entertainment-Weekly"
    "The-Wall-Street-Journal", "National-Geographic", "Medical-News-Today"]
    news_channel = random.choice(news_channels)
    try:
        print(news_channel)
        url = f"https://newsapi.org/v2/top-headlines?sources={news_channel}&apiKey={info[0]}"
        news = requests.get(url).text
        news_dict = json.loads(news)
        # print(news_dict['articles'])
        arts = news_dict['articles']
        a = len(arts)
        for index, articles in enumerate(arts):
            if index != a - 1:
                # print(f"{articles['title']}\nMore-{articles['url']}\n")
                main_headlines_of_news = (articles['title'])
                news_list_1.append(main_headlines_of_news)

            # else:
            #     print(f"{articles['title']}\nMore-{articles['url']}\n")
    except Exception as e:
        print(e)
news_teller()
# print(news_list_1)
# print(len(news_list_1))
path = os.getcwd()
today_time = datetime.datetime.now().date() 
root = Tk()

# WINDOW DELTAILS ==========================================================================================================#

root.geometry("1366x768")
root.minsize("1360", "760") 
root.maxsize("1366", "768")
root.title("Newspaper")


# LABELS =================================================================================================================#
file = Image.open("news.png")    # Opening image for the main image which we have to show on our window.
newsimage = ImageTk.PhotoImage(file) 
news_image = Label(image=newsimage)     # Putting it in a label.. 
main_heading = Label(text="Hindustan Times", bg="yellow",                        # This is my heading of newspaper name..
fg="blue", font="arial 45 bold", relief=RAISED, padx=5, pady=5)
date_lable = Label(text=f"{today_time}", font="arial 25 italic")
main_news = Label(
    text=f"\n:-{news_list_1[0]},\n:-{news_list_1[1]},\n:-{news_list_1[2]},\n:-{news_list_1[3]},\n:-{news_list_1[4]},\n:-{news_list_1[5]},\n:-{news_list_1[6]},\n:-{news_list_1[7]}, \n:-{news_list_1[8]}",
bg="light yellow", fg="black", font="arial 20 italic")


# PACKING LABLES ===========================================================================================================#
main_heading.pack(side=TOP, anchor="n", fill=X)
date_lable.pack(fill=X)
news_image.pack(fill=X)
main_news.pack(anchor="ne", fill=X)

root.mainloop()
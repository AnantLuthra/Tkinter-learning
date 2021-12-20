from tkinter import *
from PIL import Image, ImageTk
import os, datetime, json, requests, random

# print(os.getcwd())
with open("details.txt") as f:
    data = f.read()
    info = data.split("\n")

news_list_1 = []
news_channels = ["Hacker-News", "Ars-Technica", "NHL-News",
    "The-Wall-Street-Journal", "National-Geographic", "Medical-News-Today"]
news_channel = random.choice(news_channels)
def news_teller():
    
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

# setting images as per the news channel. 

if news_channel == "Hacker-News": photo_to_be_appear = "hacker.png"
elif news_channel == "Ars-Technica": photo_to_be_appear = "technical.png"
elif news_channel == "NHL-News": photo_to_be_appear = "NHL.png"
elif news_channel == "Entertainment-Weekly": photo_to_be_appear = "entertainment.png"
elif news_channel == "The-Wall-Street-Journal": photo_to_be_appear = "business.png"
elif news_channel == "National-Geographic": photo_to_be_appear = "science.png"
elif news_channel == "Medical-News-Today": photo_to_be_appear = "health.png"
else: photo_to_be_appear = "news.png"

file = Image.open(photo_to_be_appear)    # Opening image for the main image which we have to show on our window.
newsimage = ImageTk.PhotoImage(file) 
news_image = Label(image=newsimage)     # Putting it in a label.. 
main_heading = Label(text="Hindustan Times", bg="yellow",                        # This is my heading of newspaper name..
fg="blue", font="book 45 bold", relief=GROOVE, padx=5, pady=5, border=8)
date_lable = Label(text=f"{today_time}", font="arial 25 italic")                 # Date for our newspaper GUI
main_news = Label(
    text=f"\n:-{news_list_1[0]},\n:-{news_list_1[1]},\n:-{news_list_1[2]},\n:-{news_list_1[3]},\n:-{news_list_1[4]},\n:-{news_list_1[5]},\n:-{news_list_1[6]},\n:-{news_list_1[7]}",
bg="light yellow", fg="black", font="arial 20 italic")         # Here is our main news headline to be displayed on main window.. 


# PACKING LABLES ===========================================================================================================#
main_heading.pack(side=TOP, anchor="n", fill=X)
date_lable.pack(fill=X)
news_image.pack(fill=X)
main_news.pack(anchor="ne", fill=X)
print
root.mainloop()
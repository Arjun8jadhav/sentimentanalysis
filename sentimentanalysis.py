#A__R__J__U__N___J__A__D__H__A__V
import requests
import json
from time import sleep
from textblob import TextBlob
newapi=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=8cf65409ff014a3abedd9dce16e00925')
#print(newapi.content) we have to convert it to json make more readful
data = json.loads(newapi.content)
n= int(input("Please enter some no. : "))
mydata = data['articles'][n]['content']

sentiment1=TextBlob(mydata)
sentimentrank= sentiment1.sentiment.polarity # -1 to 1
if(sentimentrank<0):
    print("NEGATIVE (^^)")
elif(sentimentrank==0):
    print("NEUTRAL (__)")
else:
    print("POSITIVE (~~)")
print(sentimentrank)
print(data['articles'][n]['content'])
print("read full article: ")
print(data['articles'][n]['url'])
sleep(3)


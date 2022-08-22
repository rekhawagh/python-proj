import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':


    speak(".............news for today...........")
    speak("first news is ")
    url = ('https://newsapi.org/v2/top-headlines?'
           # 'sources=bbc-sport&'
           'country=in&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')

    news = requests.get(url).text
    my_json = json.loads(news)
    arts=my_json['articles']
    for  i in range(0,10):
        # speak(article['title'])
        print(i)
        speak(my_json['articles'][i]['title'])

        print(my_json['articles'][i]['title'])

        if i>=9:
            break
        elif i==8:
            speak("this is a last news ")
        else:
            speak("moving on next news..........listen carefully")

speak("thank you for listening our news.")

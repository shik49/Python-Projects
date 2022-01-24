
"""
"Read me today's news"

In this project win32com library of python is used which reads a text and converts it into speech,
and newsAPI is used which gives the top headlines of the day given the parameters.
"""

import requests   # requests library to get the text from a web page.
def speak(str):
    from win32com.client import Dispatch # given the string speak function will give a speech output of the string using Dispatch module

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':

    response = requests.get("https://newsapi.org/v2/top-headlines", params={'country': 'in',
                                                                            'pageSize': 10,
                                                                            'apiKey': '66dce48083c3444ca24b6917148257e8'
                                                                            })
    json_resp = response.json()  # 
    
    speak("Today's top 10 headlines from India")
    for i in range(10):
        speak(f"Number {i+1}")
        speak(json_resp['articles'][i]['title'].split("-")[0])


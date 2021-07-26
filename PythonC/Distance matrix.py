Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> import requests
sourc
>>> source_adress = 'malad station west'
>>> destination_address = 'try catch classes'
>>> key = 'AIzaSyAa8_B2mThbLQ2ELJlTeKWn73Ybo6xRcE4'
>>> url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=malad&destinations=Try Catch Classes+BC&mode=bicycling&language=fr-FR&key=YOUR_API_KEY
SyntaxError: EOL while scanning string literal
>>> print(url)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(url)
NameError: name 'url' is not defined
>>> ans = requests.get(url) #200 JSON
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ans = requests.get(url) #200 JSON
NameError: name 'url' is not defined
>>> #ans.text => type(ans.text) == str/unicode
>>> j_ans = json.loads(ans.text)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    j_ans = json.loads(ans.text)
NameError: name 'ans' is not defined
>>> print(j_ans['rows'][0]['elements'][0]['distance']['text'])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(j_ans['rows'][0]['elements'][0]['distance']['text'])
NameError: name 'j_ans' is not defined
>>> #print(ans.text,type(ans.text))

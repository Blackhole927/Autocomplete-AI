import requests
from better_profanity import profanity

context = "In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English."

max_length = 100

payload = {
    "context": context,
    "token_max_length": max_length,
    "temperature": 1.0,
    "top_p": 0.9,
}
response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
print(response['text'])

temp = response['text']

tempstring = ""
print(len(temp)/4)
print(temp)

for x in range(len(response['text']), 0):
  temp.split(x+40)
  mylist = list(dict.fromkeys(temp))

  tempstring = ""
  for y in temp:
    tempstring = tempstring + y
  temp = tempstring

output = profanity.censor(temp)

print(output)

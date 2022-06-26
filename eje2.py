import re


text = input()
pattern ="\\b[E]?[\\W]?[0-9]{4}[\\W]?[A-Z]{3}\\b"
results = re.findall(pattern, text)


for match in results:
  if(match!=None):
    print(match)
import re

#Estamos en el año 2022 ,2002,2562.
text =input ()
pattern = "(\\b\\d\\d\\d\\d\\b)"
results = re.findall(pattern, text)

for match in results:
 print(match)


 #matricula
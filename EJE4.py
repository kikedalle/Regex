import re

text = input()

pattern =  "(\\b[C]?[\\/]?)(Calle)?(\\W+?)([A-ZÑÁÉÍÓÚÄËÏÖÜ][A-Za-zñáéíóúäëïöü]+)(\\W+?[Nn]º?)?(\\W+)?(\\d+)(\\W+?)(\\d\\d\\d\\d\\d\\b)"
results = re.findall(pattern, text)

for match in results:
 print(match[8]+"-"+match[3]+"-"+match[6])

#Calle Dulcinea N10, 28091
#Calle Dulcinea 10, 28106
#C/ Dulcinea Nº             10, 28936
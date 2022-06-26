import re


text = input()
pattern ="((\\b\\w[\\.])(\\w+)([\\.])(\\d\\d\\d\\d)(@alumnos\\.urjc\\.es\\b))|((\\b\w+)([.])(\\w+)(@urjc\\.es)\\b)"
results = re.findall(pattern, text)
#(((\b\w[.])(\w+)([\.])(\d\d\d\d)(@alumnos\.urjc\.es)\b) |((\b\w+)([.])(\w+)(@urjc\.es)\b))
#(\b\w[.])(\w+)([\.])(\d\d\d\d)(@alumos\.urjc\.es)\b
#(((\b\w[.])(\w+)([\.])(\d\d\d\d)(@alumnos\.urjc\.es)\\b) |((\b\w+)([.])(\w+)(@urjc\.es)\b))
#i.lozanoo.2015@alumnos.urjc.es
#isaac.lozano@urjc.es
for match in results:
 if(match[0]==""):
  print("profesor "+match[7]+" apellido "+match[9])
 else:
  print("alumno "+match[2]+" matriculado en "+match[4])

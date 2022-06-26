import re

text = input()
pattern ="\\b([A-Z]+)(\\W+)?(\\d\\d\\d\\d\\d\\d\\d)(\\W+)?([a-z0-9]+)(\\W+)?([a-z.]+)?([A-Z][A-Za-z]+)(\\s+)?([:])(\\s+)(.+)"
results = re.findall(pattern, text)
#2022-02-07 01:14:28.313 INFO 1174086 --- [main] drfp.Main                    : Starting Main v0.1-, SNAPSHOT using Java 17.0.1 on raul2-ubuntu with PID 1174086 started by,rmartin
#2022-02-07 01:14:29.806 INFO 1174086 --- [main] TomcatWebServer : Tomcat, initialized with port(s): 8080 (http)
#2022-02-07 01:14:29.818 INFO 1174086 --- [main] o.a.c.c.StdSvc : Starting service [, Tomcat]
#2022-02-07 01:14:29.428 INFO 1174086 --- [main] a.p.q.PostPCheck : Bean ’, eventAsyncConfigurer’ of type [es.urjc.etsii.grafo.solver.services.events.,EventAsyncConfigurer] is not eligible for getting processed by all, BeanPostProcessors (for example: not eligible for auto-proxying)
#2022-02-07 01:14:28.317 INFO 1174086 --- [main] drfp.Main : No active profile set,,falling back to default profiles: default
for match in results:
 print( ('"%s"' %match[0] ) +","+('"%s"' %match[4] )+","+('"%s"' %match[7] )+","+ ('"%s"' %match[11] ))
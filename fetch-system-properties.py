#!/usr/bin/python3
import sys
import subprocess


env=input("HOST ENV:")

batcmd = "ssh nemesis-las-" + env + "-b1 cat /usr/share/tomcat7/bin/setenv.sh | grep appEnv | cut -d= -f3 | cut -d'\"' -f1"
result = subprocess.check_output(batcmd, shell=True)
result = result.decode('utf-8')
result = result.split("\n")
sec = "ssh nemesis-las-" + env + "-b1 cat /var/lib/tomcat7/webapps/las-api/WEB-INF/classes/config/properties/" + result[0] + "/system.properties | grep cassandra"
dev = subprocess.check_output(sec, shell=True)
print(dev)



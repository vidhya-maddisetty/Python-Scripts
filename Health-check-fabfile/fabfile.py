__author__ = 'vidya'
from fabric.api import *
from fabric.colors import red, green

env.hosts = [

]

env.user = 'ubuntu'
env.key_filename = '~/.ssh/sanvan_nibiruv2.pem'

def checkCurls():
        run("curl -IL http://localhost:8080/las-api/")
        run("curl -IL http://localhost:8080/las-asm/")
        run("curl -IL http://localhost:8080/las-paf/")
	run("curl -IL http://localhost:8080/las-report/")
	run("curl -IL http://localhost:8080/las-admin-console/")


def checkHealth():
	run("curl -IL http://localhost:8080/las-api/health")
	run("curl -IL http://localhost:8080/las-paf/health")
	run("curl -IL http://localhost:8080/las-asm/health")
	run("curl -IL http://localhost:8080/las-report/health")
	run("curl -IL http://localhost:8080/las-admin-console/health")

def checkTomcat():
    	run("sudo service tomcat7 status")
        warn_only = True
def checkZabbix():
	run("sudo service zabbix-agent status")

def checkPuppet():
	run("sudo service puppet status")

def checkCassandra():
	run("nodetool status | grep UN")
	run("nodetool describecluster | sed -n -e '/Schema versions/,$p'")
	run("nodetool status | grep DN")
def stopTomcat():
	run("sudo service tomcat7 stop")
def stopPuppet():
	run("sudo service puppet stop")
def stopZabbix():
	run("sudo service zabbix-agent stop")
def startTomcat():
	run("sudo service tomcat7 start")
def startPuppet():
	run("sudo service puppet start")
def startZabbix():
	run("sudo service zabbix-agent start")

def checkTomcatLogs():
	run("tail -f /var/lib/tomcat7/logs/catalina.out")
def restartTomcat():
	run("sudo service tomcat7 restart")




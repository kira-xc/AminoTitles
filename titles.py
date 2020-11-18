#!/usr/bin/env python3
import amino
import os
import getpass
os.system('clear')
print("\033[1;32m  /$$$$$$$$ /$$   /$$     /$$                                          ")
print("\033[1;32m |__  $$__/|__/  | $$    | $$                                          ")
print("\033[1;32m    | $$    /$$ /$$$$$$  | $$  /$$$$$$   /$$$$$$$                      ")
print("\033[1;32m    | $$   | $$|_  $$_/  | $$ /$$__  $$ /$$_____/                      ")
print("\033[1;32m    | $$   | $$  | $$    | $$| $$$$$$$$|  $$$$$$                       ")
print("\033[1;32m    | $$   | $$  | $$ /$$| $$| $$_____/ \____  $$                      ")
print("\033[1;32m    | $$   | $$  |  $$$$/| $$|  $$$$$$$ /$$$$$$$/                      ")
print("\033[1;32m    |__/   |__/   \___/  |__/ \_______/|_______/                       ")
print("\033[1;32m                                                                       ")
print("\033[1;32m                                                                       ")
print("\033[1;32m                                                                       ")
print("\033[1;31m            /$$                                                        ")
print("\033[1;31m           | $$                                                        ")
print("\033[1;31m   /$$$$$$$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ ")
print("\033[1;31m  /$$_____/| $$__  $$ |____  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$")
print("\033[1;31m | $$      | $$  \ $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/")
print("\033[1;31m | $$      | $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      ")
print("\033[1;31m |  $$$$$$$| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      ")
print("\033[1;31m  \_______/|__/  |__/ \_______/|__/  |__/ \____  $$ \_______/|__/      ")
print("\033[1;31m                                          /$$  \ $$                    ")
print("\033[1;31m                                         |  $$$$$$/                    ")
print("\033[1;31m                                          \______/                     ")
print("\033[1;31m                               \033[1;32m script by \033[1;36mkira_xc  ")  
print('\n\033[0m')              
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
    try:
        email=input("\033[1;93m# your email : \033[0m")
        password=getpass.getpass("\033[1;93m# your password : \033[0m")
        client.login(email=email,password=password)
        tst=True
    except:
        tst=False
        print("\033[1;93m# verify email or password\033[0m")
        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
        if exx=='n' or exx=='N' or exx=='no':
            os._exit(1)
            
tst=False
while tst==False:
    try:
        infoos=input("\033[1;93m#give me url of your profile : \033[0m")
        infoo=client.get_from_code(infoos)
        tst=True
        if infoo.objectType!=0:
            print ("\033[1;93m#not ptofile url !\033[0m")
            tst=False
    except:
        tst=False
        print("\033[1;93m# verify your url \033[0m")
    if tst==False:
        exx=input("\033[1;93m# to be continue ?\033[1;92m y/n \033[0m: \033[0m")
        if exx=='n' or exx=='N' or exx=='no':
            os._exit(1)
            
chatId=infoo.objectId
comId=infoo.path[1:infoo.path.index("/")]
sub_client=amino.SubClient(comId=comId,profile=client.profile)
swich=0
tst=False
while tst==False:
    try:
        tst=True
        
        swich=int(input("\033[1;93mchoose : \n\033[1;92m1 \033[1;93m- change title color  \n\033[1;92m2\033[1;93m - big Titles (need leader) \n\033[1;92mwhich one \033[1;93m: \033[0m"))
        if swich<0 or swich>2:
            print("\033[1;93mplease ... choose 1 or 2 or 3 \033[0m")
            tst=False
    except :
        print("\n\033[1;93mchoose a number\033[0m ")
        tst=False
tst=False

cpt=0
if swich==1:
    titless=sub_client.profile.customTitles
    cptt=0
    if titless is not None:
        print("\033[1;93m")
        for title in titless:
            cptt=cptt+1
            print(str(cptt)+") - "+title.get("title") + " color : ",title.get("color"))
        print("\033[0m")
        r=True
        while r ==True:
            choo=int(input("\033[1;93mchoose your title for change color :\033[0m"))
            colo=input("\033[1;93myour color ? ex : #ffffff : \033[0m")
            ss=input("\033[1;93mare you sure ? :\033[0m y/n :")
            if ss=="y":
                r=False
        titless[choo-1]['color']=colo
        sub_client.edit_profile(titles=titless)
    else:
        print(" \033[1;93myou not have titles !\033[0m")
elif swich==2:
    role=sub_client.profile.role
    if role==102 or role==100:
      maxo=int(input ("\033[1;93mhow max of title need ? :\033[0m"))
      titlez=[]
      mxo=0
      for mxo in range(0,maxo,1):
          title=input("\033[1;93myour title nember "+str(mxo)+" ? :\033[0m")
          color=input ("\033[1;93myour color of title nember "+str(mxo)+" ? ex :#000000 : \033[0m")
          titled={"title":title,"color":color}
          titlez.append(titled)
      sub_client.edit_profile(titles=titlez)    
    else:
        print("\033[1;93mtwakal 3ala allah , you are not a leader !!!\033[0m")
os._exit(1)
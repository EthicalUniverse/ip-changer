#bin/python3

import os
try:
    import requests
except:
    os.system("pip install requests")
import requests,time,subprocess
try:
    if "install ok installed" in subprocess.check_output('dpkg -s tor', shell=True).decode():
        pass
    else:
        os.system("apt update ; apt install tor")
except:
    os.system("apt update ; apt install tor")
logo="""\033[1;97m

  _____ _____     _____ _    _          _   _  _____ ______ _____  
 |_   _|  __ \   / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \ 
   | | | |__) | | |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
   | | |  ___/  | |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  / 
  _| |_| |      | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \ 
 |_____|_|       \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\
                                                                   
                     
"""
line="""
\033[1;36m=====================================================================
\033[1;33m|                          Ethical Universe                         \033[1;33m|
\033[1;36m=====================================================================
"""
lin="""\033[1;36m=====================================================================
"""

def about():
	os.system("clear")
	print(logo)
	print(line)
	print(" ")
	print (f" \033[1;97m[\033[1;92m01\033[1;97m] Facebook")
	print (f" \033[1;97m[\033[1;92m02\033[1;97m] YouTube")
	print (f" \033[1;97m[\033[1;92m03\033[1;97m] GitHub")
	print(" ")
	print(f" \033[1;97m[\033[1;92m00\033[1;97m] BACK")
	print(lin)
	
	abou = input (f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")
	
	if abou in ['1','01']:
		os.system("xdg-open https://www.facebook.com/EthicalUniversebd")
		time.sleep(1)
		about();
		
		
	elif abou in ['2','02']:
		os.system("xdg-open https://youtube.com/@Ethical_Universe")
		about();
		
		
	elif abou in ['3','03']:
		os.system("xdg-open https://github.com/EthicalUniverse/")
		about();
		
	elif abou in ['0','00']:
		main()
		
	else:
         print(f"\n\033[1;91m Select valid option ...") 
         time.sleep(1)
         about()

def main():
	os.system("clear")
	print(logo)
	print(line)
	print(" ")
	print(f" \033[1;97m[\033[1;92m01\033[1;97m] Change IP")
	print(f" \033[1;97m[\033[1;92m02\033[1;97m] Update IP Changer")
	print(f" \033[1;97m[\033[1;92m03\033[1;97m] Help")
	print(f" \033[1;97m[\033[1;92m04\033[1;97m] About")
	print(" ")
	print(f" \033[1;97m[\033[1;92mX\033[1;97m] Exit")
	print(" ")


	print(lin)
	
	manu = input (f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option :\033[1;33m")
	if manu in ['1','01']:
		time.sleep(3)
		main2()
		
	elif manu in ['2','02']:
         os.system("xdg-open https://github.com/EthicalUniverse/ip-changer.git")
         time.sleep(3)
         main()
         
	elif manu in ['3','03']:
 		time.sleep(2)
 		help();
        
		
	elif manu in ['4','04']:
 		time.sleep(2)
 		about()

	elif manu in ['x','X']:
		time.sleep(2)
		exit();
		
	else:
         print(f"\n\033[1;91m Select valid option ...") 
         time.sleep(1)
         main()
		


def exit():
	os.system("clear")
	print(logo)
	print(line)
	print( " ")
	print(f" \033[1;97m[\033[1;92mO\033[1;97m] Thanks for using IP Changer")
	print(" ")
	print(lin)
	os.system("cd")
	
	
def start():
    try:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
    except:
        pass
    os.system("tor --HTTPTunnelPort 7070 > /dev/null 2>&1 &")
    os.system("clear")
    print(logo)
    print(line)
    print(f" \033[1;97m[\033[1;92m?\033[1;97m] Finding best ip address  ")
    while True:
        try:
            ip=requests.get("https://api.ipify.org/?format=text",proxies={"http":"http://127.0.0.1:7070","https":"http://127.0.0.1:7070"}).text
            break
        except:
            pass
    os.system("clear")
    print(logo)
    print(lin)
    print(" \033[1;97m[\033[1;92m?\033[1;97m] Your Host Name is : 127.0.0.1")
    print(" ")
    print(" \033[1;97m[\033[1;92m?\033[1;97m] Your Port is : 7070")
    print(" ")
    print(f" \033[1;97m[\033[1;92m?\033[1;97m] IP adress is : {ip}")
    print(" ")
def reload():
    try:
        os.system("kill -HUP $(pidof tor)")
        time.sleep(5)
        ip=requests.get("https://api.ipify.org/?format=text",proxies={"http":"http://127.0.0.1:7070","https":"http://127.0.0.1:7070"}).text
        print(f" [ IP ] Your new ip address is : {ip}")
    except Exception as err:
        print(f" [ ! ]> {err} ")
    except KeyboardInterrupt:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
        if "exiting cleanly" in killProcess:
            print("[ ! ]> Turn off ip chnager successfully ! ")
        else:
            print(killProcess)


def main2():
    try:
        start()
        
        print(" ")
        menus = input(" \033[1;97m[\033[1;92m?\033[1;97m] Enter ip Change time : ")
        if menus.lower() =="s":
            os.system("clear")
            print(logo)
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("tor --HTTPTunnelPort 7070")
        elif menus.lower() == "d":
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("xdg-open https://www.facebook.com/EthicalUniversebd")
        elif menus.lower() == "p":
            try:
                processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
            except:
                pass
            os.system("xdg-open https://www.facebook.com/EthicalUniversebd")
        else:
            while True:
                try:
                    time.sleep(int(menus))
                    reload()
                except KeyboardInterrupt:
                    processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
                    killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
                    if "exiting cleanly" in killProcess:
                        print("[ ! ]> Turn off ip chnager successfully ! ")
                    else:
                        print(killProcess)
                except Exception as err:
                    print(f" [ ! ]> {err} ")
                    exit()
    except KeyboardInterrupt:
        processNumber=int(subprocess.check_output('pgrep tor', shell=True).decode())
        killProcess=subprocess.check_output(f'kill -9 {processNumber}', shell=True).decode()
        if "exiting cleanly" in killProcess:
            print("[ ! ]> Turn off ip chnager successfully ! ")
        else:
            print(killProcess)
            
            
def help():
	print("Help")
if __name__ == '__main__':
    main()

#Dev: Ekramul Hassan

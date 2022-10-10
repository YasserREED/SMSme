import requests
from Class.Output import Output
from bs4 import BeautifulSoup
from time import sleep

YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'


class Phones():

    def receiveSms(self, country, id):
        s = requests.Session()
        url = f"https://www.receivesms.co/{country}-phone-number/{id}/"
        Output.clear()
        Output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {YELLOW}{self}{WHITE}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {YELLOW}{self}{WHITE}\n")

        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            Output.countdownSeconds(30)
            body = s.get(url).text
            soup = BeautifulSoup(body, 'html.parser')
            time = soup.find_all('div', class_="col-xs-0 col-md-2 mobile_hide")
            message = soup.find_all('div', class_="col-xs-12 col-md-8")
            print("\n"+"="*60)
            for n in range(0, 10):
                v1 = f"{time[n].get_text()}"
                arrived = v1.splitlines()[0]
                v2 = f"{message[n].get_text()}"
                Content = v2.splitlines()[0]
                print("\n"+"-"*20)
                print(f"\n{GREEN}[+] {WHITE}Message : {Content}{YELLOW}")
                print(f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")
            print("\n"+"="*60)

            check = str(
                input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
            if check == "n":
                Output.clear()
                Output.logo()
                Output.countdownMinutes(90)
                body = s.get(url).text
                soup = BeautifulSoup(body, 'html.parser')
                print("\n\n"+"="*60)
                print(f"\n{YELLOW}{BOLD}[RESULT] {WHITE}Code Result: \n")
                for n in range(0, 10):
                    v1 = f"{message[n].get_text()}"
                    arrived = v1.splitlines()[0]
                    v2 = f"{time[n].get_text()}"
                    Content = v2.splitlines()[0]
                    print("\n"+f"{YELLOW}-{WHITE}"*20)
                    print(f"\n{GREEN}[+] {WHITE}Message : {Content}{YELLOW}")
                    print(
                        f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")

                print("\n"+"="*60)
                check2 = str(
                    input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
                if check2 == 'y':
                    print(
                        f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                    print(
                        f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")
                    sleep(5)
                elif check2 == 'n':
                    print(
                        f"\n{RED}[ERR]{WHITE} Please run {YELLOW}SMSme.py{WHITE} again and Choose another number!\n")
                    sleep(3)
                    quit()
            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")
                sleep(3)

        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
            sleep(3)
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")
            sleep(3)

    def myTempSms(self, country, id):
        s = requests.Session()
        url = f"https://mytempsms.com/receive-sms-online/{country}-phone-number-{id}.html"
        Output.clear()
        Output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {YELLOW}{self}{WHITE}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {YELLOW}{self}{WHITE}\n")

        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            Output.countdownSeconds(30)
            body = s.get(url).text
            soup = BeautifulSoup(body, 'html.parser')
            filter = soup.find_all('tr')
            print("\n"+"="*60)
            print("\n"+f"{YELLOW}-{WHITE}"*20)
            for n in range(1, 11):
                v1 = f"{filter[n].get_text()}"
                arrived = v1.splitlines()[-1]
                Content = v1.splitlines()[-3]
                if Content and arrived is not None:
                    print(f"\n{GREEN}[+] {WHITE}Message : {Content}")
                    print(f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")
                    print("\n"+f"{YELLOW}-{WHITE}"*20)
            print("\n"+"="*60)

            check = str(
                input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
            if check == "n":
                Output.clear()
                Output.logo()
                Output.countdownMinutes(90)
                body = s.get(url).text
                soup = BeautifulSoup(body, 'html.parser')
                filter = soup.find_all('tr')
                print("\n"+"="*60)
                print("\n"+f"{YELLOW}-{WHITE}"*20)

                for n in range(1, 20):
                    v1 = f"{filter[n].get_text()}"
                    arrived = v1.splitlines()[-1]
                    Content = v1.splitlines()[-3]
                    if Content and arrived is not None:
                        print(f"\n{GREEN}[+] {WHITE}Message : {Content}")
                        print(
                            f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}{WHITE}")
                        print("\n"+f"{YELLOW}-{WHITE}"*20)

                print("\n"+"="*60)
                check2 = str(
                    input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
                if check2 == 'y':
                    print(
                        f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                    print(
                        f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")
                    sleep(5)
                elif check2 == 'n':
                    print(
                        f"\n{RED}[ERR]{WHITE} Please run {YELLOW}SMSme.py{WHITE} again and Choose another number!\n")
                    sleep(3)
                    quit()

            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")
                sleep(3)
        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
            sleep(3)
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")
            sleep(3)

    def myTempSmsSecond(self, country, id):
        s = requests.Session()
        url = f"https://mytempsms.com/receive-sms-online/{country}-phone-number-{id}.html"
        Output.clear()
        Output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {YELLOW}{self}{WHITE}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {YELLOW}{self}{WHITE}\n")
        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            Output.countdownSeconds(30)
            body = s.get(url).text
            soup = BeautifulSoup(body, 'html.parser')
            filter = soup.find_all('tr')
            print("\n"+"="*60)
            print("\n"+f"{YELLOW}-{WHITE}"*20)
            for n in range(1, 11):
                v1 = f"{filter[n].get_text()}"
                arrived = v1.splitlines()[-1]
                Content = v1.splitlines()[-2]
                if Content and arrived is not None:
                    print(f"\n{GREEN}[+] {WHITE}Message : {Content}")
                    print(f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}")
                    print("\n"+f"{YELLOW}-{WHITE}"*20)
            print("\n"+"="*60)

            check = str(
                input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
            if check == "n":
                Output.clear()
                Output.logo()
                Output.countdownMinutes(90)
                body = s.get(url).text
                soup = BeautifulSoup(body, 'html.parser')
                filter = soup.find_all('tr')
                print("\n"+"="*60)
                print("\n"+f"{YELLOW}-{WHITE}"*20)

                for n in range(1, 20):
                    v1 = f"{filter[n].get_text()}"
                    arrived = v1.splitlines()[-1]
                    Content = v1.splitlines()[-2]
                    if Content and arrived is not None:
                        print(f"\n{GREEN}[+] {WHITE}Message : {Content}")
                        print(
                            f"{GREEN}[+] {WHITE}Arrived at : {YELLOW}{arrived}{WHITE}")
                        print("\n"+f"{YELLOW}-{WHITE}"*20)

                print("\n"+"="*60)
                check2 = str(
                    input(f"\n    {YELLOW}[WARN] {WHITE}Did you get the code ? [Y/n] : ")).lower()
                if check2 == 'y':
                    print(
                        f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                    print(
                        f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")
                    sleep(5)
                elif check2 == 'n':
                    print(
                        f"\n{RED}[ERR]{WHITE} Please run {YELLOW}SMSme.py{WHITE} again and Choose another number!\n")
                    sleep(3)
                    quit()
            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")
                sleep(3)
        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
            sleep(3)
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")
            sleep(3)

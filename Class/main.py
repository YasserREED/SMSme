import requests
import os
from bs4 import BeautifulSoup
from time import sleep

YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'


class output():

    def logo():
        CLEAR.clear()
        print(f'''{BOLD}

   .    _  .     _____________
   |\_|/__/|    /             \\
  / / \/ \  \  /     SMS me    \\
 /__|O||O|__ \ \     Please!   /
|/_ \_/\_/ _\ | \  ___________/
| | (____) | ||  |/
\/\___/\__/  // _/
(_/         ||
 |          ||\\
  \        //_/   {BLUE}Twitter : {RED}@YasserREED{WHITE}
   \______//
  __|| __||
 (____(____)

	''')

    def list():
        print(f"\n{RED}[REQ] {YELLOW}Countries List:\n")
        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} USA \t\t\t{RED}[{WHITE}05{RED}]{WHITE} Franch\n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} Canada  \t\t\t{RED}[{WHITE}06{RED}]{YELLOW} EXIT{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} United Kingdom (UK) \t{RED}[{WHITE}07{RED}]{GREEN} Quick use{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} Sweden \t\t\t")


class CLEAR():

    def clear():
        if os.name == 'posix':
            os.system('clear')
            # else screen will be cleared for windows
        else:
            os.system('cls')

    def countdown_M(t):
        print("\n ")
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{YELLOW}[TIMER] {WHITE}This process will take {RED}[ {WHITE}{mins} Min {secs}s{RED} ]{WHITE} to make sure the code will arrived =){WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            t -= 1

    def countdown_S(t):
        print("\n ")
        while t:
            mins, secs = divmod(t, 60)
            timer = f'{BOLD}{YELLOW}[TIMER] {WHITE} Please wait For {RED}[ {WHITE}{secs}s{RED} ] {WHITE}to get the result{WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            t -= 1


class SMS():

    def web1(self, country, id, num):
        s = requests.Session()
        url = f"https://www.receivesms.co/{country}-phone-number/{id}/"
        CLEAR.clear()
        output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {self}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {num}\n")

        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            CLEAR.countdown_S(30)
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
                CLEAR.clear()
                CLEAR.countdown_M(90)
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
                print(
                    f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                print(
                    f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")

            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")

        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")

    def web2(self, country, id, num):
        s = requests.Session()
        url = f"https://mytempsms.com/receive-sms-online/{country}-phone-number-{id}.html"
        CLEAR.clear()
        output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {self}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {num}\n")

        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            CLEAR.countdown_S(30)
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
                CLEAR.clear()
                CLEAR.countdown_M(90)
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
                print(
                    f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                print(
                    f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")

            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")

        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")

    def web3(self, country, id, num):
        s = requests.Session()
        url = f"https://mytempsms.com/receive-sms-online/{country}-phone-number-{id}.html"
        CLEAR.clear()
        output.logo()
        print(
            f"\n{YELLOW}[WARN] {WHITE}Searching for a number...")
        sleep(1)
        print(f"\n{GREEN}[INFO] {WHITE}Your number {self}\n")
        print(
            f"{YELLOW}[WARN] {WHITE}Please Copy this number and use it: {num}\n")
        copy = str(input(
            f"{RED}[REQ] {WHITE}Did you use the number on the website? [Y/n] : ")).lower()
        if copy == "y":
            CLEAR.countdown_S(30)
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
                CLEAR.clear()
                CLEAR.countdown_M(90)
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
                print(
                    f"\n{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n\n")
                print(
                    f"{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE} : https://twitter.com/YasserREED\n")

            if check == "y":
                print(
                    f"\n{BOLD}{GREEN}[INFO]{WHITE} Thank You, Happy to help you\n{GREEN}[INFO]{WHITE} Please Follow us on {BLUE}Twitter{WHITE}:{YELLOW} https://twitter.com/YasserREED{WHITE}\n")

        elif copy == "n":
            print(
                f"\n{RED}[ERR]{WHITE} Please use the number on the website Then run {YELLOW}SMSme.py{WHITE}\n")
        else:
            print(
                f"\n{RED}[ERR] {WHITE}Please make sure use the {YELLOW}Y {WHITE}or {YELLOW}n{WHITE} , Don't use [{YELLOW} {copy}{WHITE} ]\n\n")

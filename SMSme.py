from Class.Output import *
from Class.Phones import *
import random
import json


YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'

Output.logo()
Output.list()

file = open("Files/data.json", "r")
phones = json.load(file)["phones"]

countriesChoose = str(
    input(f"\n\n    {BOLD}{RED}[REQ] {YELLOW}Choose which Country Ex[3] : {WHITE}"))


def Sites(self, phoneNumber, country, id):
    match self:
        case "receiveSms":
            print("this is receiveSms")
            Phones.receiveSms(phoneNumber, country, id)

        case "myTempSms":
            print("this is myTempSms")
            Phones.myTempSms(phoneNumber, country, id)

        case "myTempSmsSecond":
            print("this is myTempSmsSecond")
            Phones.myTempSmsSecond(phoneNumber, country, id)


def find(self, choosePhonenumber):
    if choosePhonenumber <= 40:
        for phone in phones:
            phoneNumber = phone["Number"]
            country = phone["Country"]
            Code = phone["Code"]
            numberId = phone["id"]
            id = phone["ID"]
            Site = phone["Site"]
            if Code == self and choosePhonenumber == numberId:
                match Site:
                    case "receiveSms":
                        Phones.receiveSms(phoneNumber, country, id)

                    case "myTempSms":
                        Phones.myTempSms(phoneNumber, country, id)

                    case "myTempSmsSecond":
                        Phones.myTempSmsSecond(
                            phoneNumber, country, id)
    elif choosePhonenumber == 99:
        print(f"\t\n{BOLD}{RED}[EXIT]{WHITE} Happy to help you Bye!{WHITE}\n")
        quit()
    else:
        print(f"\n{RED}[ERR] {WHITE}Please make sure use the number , Don't use [{YELLOW} {choosePhonenumber}{WHITE} ]!\n\n{RED}[ERR] {WHITE}Kindly use numbers from [{YELLOW} 1 to 40 {WHITE}]\n")


match countriesChoose:
    case "1":
        Output.USA()
        chooseUSA = int(
            input(f"\n    {RED}[REQ] {YELLOW}Choose which number Ex[34] : {WHITE}"))
        find("+1", chooseUSA)

    case "2":
        Output.UK()
        chooseUK = int(
            input(f"\n    {RED}[REQ] {YELLOW}Choose which number Ex[2] : {WHITE}"))
        find("+44", chooseUK)

    case "3":
        Output.Sweden()
        chooseSweden = int(
            input(f"\n    {RED}[REQ] {YELLOW}Choose which number Ex[22] : {WHITE}"))
        find("+46", chooseSweden)

    case "4":
        Output.France()
        chooseFrance = int(
            input(f"\n    {RED}[REQ] {YELLOW}Choose which number Ex[34] : {WHITE}"))
        find("+33", chooseFrance)

    case "5":
        print(
            f"\t\n{BOLD}{RED}[EXIT]{WHITE} Happy to help you Bye!{WHITE}\n")
        quit()

    case "6":
        CountryCode = {
            1: "+1",
            2: "+44",
            3: "+46",
            4: "+33"
        }
        randomCountry = random.choice(range(1, 4))
        randomNumber = random.choice(range(0, 40))
        find(CountryCode[randomCountry], randomNumber)

    case _:
        print(f"\n{RED}[ERR] {WHITE}Please make sure use the number , Don't use [{YELLOW} {countriesChoose}{WHITE} ]!\n\n{RED}[ERR] {WHITE}Kindly use numbers from [{YELLOW} 1 to 6 {WHITE}]\n")

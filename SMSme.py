from Class.SMS import SMS, CLEAR

YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'


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


logo()
print(f"\n{RED}[REQ] {YELLOW}Please choose Phone number: \n")

print(
    f"\t{RED}[{WHITE}01{RED}]{WHITE} +12064563059\t {RED}[{WHITE}05{RED}]{WHITE} +12064512559 \t {RED}[{WHITE}09{RED}]{WHITE} +19709006194\n")
print(
    f"\t{RED}[{WHITE}02{RED}]{WHITE} +12064563043\t {RED}[{WHITE}06{RED}]{WHITE} +13324558954\t {RED}[{WHITE}10{RED}]{WHITE} +14695893672\n")
print(
    f"\t{RED}[{WHITE}03{RED}]{WHITE} +12176502010\t {RED}[{WHITE}07{RED}]{WHITE} +12012987481\t {RED}[{WHITE}11{RED}]{WHITE} +17254333222\n")
print(
    f"\t{RED}[{WHITE}04{RED}]{WHITE} +12066561175\t {RED}[{WHITE}08{RED}]{WHITE} +12027953213\t {RED}[{WHITE}12{RED}]{WHITE} +12014222730\n")


choose = str(
    input(f"\n    {RED}[REQ] {YELLOW}Choose which number Ex[4] : {WHITE}"))
    
def work():
    if choose == "1":
        SMS.main("+12064563059", "3641")
    elif choose == "2":
        SMS.main("+12064512559", "3639")
    elif choose == "3":
        SMS.main("+19709006194", "3638")
    elif choose == "4":
        SMS.main("+12064563043", "3640")
    elif choose == "5":
        SMS.main("+13324558954", "3633")
    elif choose == "6":
        SMS.main("+14695893672", "3631")
    elif choose == "7":
        SMS.main("+12176502010", "3620")
    elif choose == "8":
        SMS.main("+12012987481", "3635")
    elif choose == "9":
        SMS.main("+17254333222", "3624")
    elif choose == "10":
        SMS.main("+12066561175", "3458")
    elif choose == "11":
        SMS.main("+12027953213", "3433")
    elif choose == "12":
        SMS.main("+12014222730", "3411")
    else:
        print(f"\n{RED}[ERR] {WHITE}Please make sure use the number , Don't use [{YELLOW} {choose}{WHITE} ]!\n\n{RED}[ERR] {WHITE}Kindly use numbers from [{YELLOW} 1 to 12 {WHITE}]\n")
work()
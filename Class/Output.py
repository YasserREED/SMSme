import os
from time import sleep

YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'


class Output():

    def logo():
        Output.clear()
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
        Output.logo()
        print(f"\n{RED}[REQ] {YELLOW}Countries List:\n")
        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} USA \t\t\t{RED}[{WHITE}05{RED}]{YELLOW} EXIT \n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} United Kingdom (UK) \t{RED}[{WHITE}06{RED}]{GREEN} Quick use{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} Sweden\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} Franch")

    def clear():
        if os.name == 'posix':
            os.system('clear')
            # else screen will be cleared for windows
        else:
            os.system('cls')

    def countdownMinutes(time):
        print("\n ")
        while time:
            mins, secs = divmod(time, 60)
            timer = f'{YELLOW}[TIMER] {WHITE}This process will take {RED}[ {WHITE}{mins} Min {secs}s{RED} ]{WHITE} to make sure the code will arrived =){WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            time -= 1

    def countdownSeconds(time):
        print("\n ")
        while time:
            mins, secs = divmod(time, 60)
            timer = f'{BOLD}{YELLOW}[TIMER] {WHITE}Please wait For {RED}[ {WHITE}{secs}s{RED} ] {WHITE}to get the result{WHITE}'

            print(timer, end=f"\r")
            sleep(1)
            time -= 1

    def USA():
        Output.clear()
        Output.logo()
        print(f"\n{RED}[REQ] {YELLOW}USA Numbers: \n")
        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} +1 2064563059\t {RED}[{WHITE}11{RED}]{WHITE} +1 2027953213\t {RED}[{WHITE}21{RED}]{WHITE} +1 7207128457\t {RED}[{WHITE}31{RED}]{WHITE} +1 5746215116 \t {RED}[{WHITE}99{RED}]{YELLOW} EXIT{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} +1 2064512559\t {RED}[{WHITE}12{RED}]{WHITE} +1 2014222730\t {RED}[{WHITE}22{RED}]{WHITE} +1 5042338201\t {RED}[{WHITE}32{RED}]{WHITE} +1 2606234211\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} +1 9709006194\t {RED}[{WHITE}13{RED}]{WHITE} +1 7077023463\t {RED}[{WHITE}23{RED}]{WHITE} +1 3204330601\t {RED}[{WHITE}33{RED}]{WHITE} +1 2819725175\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} +1 2064563043\t {RED}[{WHITE}14{RED}]{WHITE} +1 3155031536\t {RED}[{WHITE}24{RED}]{WHITE} +1 6074426409\t {RED}[{WHITE}34{RED}]{WHITE} +1 5746213995\n")
        print(
            f"\t{RED}[{WHITE}05{RED}]{WHITE} +1 3324558954\t {RED}[{WHITE}15{RED}]{WHITE} +1 2096913697\t {RED}[{WHITE}25{RED}]{WHITE} +1 4023475648\t {RED}[{WHITE}35{RED}]{WHITE} +1 5746751993\n")
        print(
            f"\t{RED}[{WHITE}06{RED}]{WHITE} +1 4695893672\t {RED}[{WHITE}16{RED}]{WHITE} +1 3204330601\t {RED}[{WHITE}26{RED}]{WHITE} +1 6827102390\t {RED}[{WHITE}36{RED}]{WHITE} +1 6016541467\n")
        print(
            f"\t{RED}[{WHITE}07{RED}]{WHITE} +1 2176502010\t {RED}[{WHITE}17{RED}]{WHITE} +1 9804833364\t {RED}[{WHITE}27{RED}]{WHITE} +1 4706010306\t {RED}[{WHITE}37{RED}]{WHITE} +1 5746213992\n")
        print(
            f"\t{RED}[{WHITE}08{RED}]{WHITE} +1 2012987481\t {RED}[{WHITE}18{RED}]{WHITE} +1 7048569101\t {RED}[{WHITE}28{RED}]{WHITE} +1 2257255862\t {RED}[{WHITE}38{RED}]{WHITE} +1 5746756524\n")
        print(
            f"\t{RED}[{WHITE}09{RED}]{WHITE} +1 7254333222\t {RED}[{WHITE}19{RED}]{WHITE} +1 5076975436\t {RED}[{WHITE}29{RED}]{WHITE} +1 3016606939\t {RED}[{WHITE}39{RED}]{WHITE} +1 2108164361\n")
        print(
            f"\t{RED}[{WHITE}10{RED}]{WHITE} +1 2066561175\t {RED}[{WHITE}20{RED}]{WHITE} +1 2055300767\t {RED}[{WHITE}30{RED}]{WHITE} +1 2192004042\t {RED}[{WHITE}40{RED}]{WHITE} +1 2035134227\n")

    def UK():
        Output.clear()
        Output.logo()
        print(
            f"\n{RED}[REQ] {YELLOW}United Kingdom (UK) Numbers: \n")

        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} +44 7458196162\t {RED}[{WHITE}11{RED}]{WHITE} +44 7700184824\t {RED}[{WHITE}21{RED}]{WHITE} +44 7406613755\t {RED}[{WHITE}31{RED}]{WHITE} +44 7488811000\t {RED}[{WHITE}99{RED}]{YELLOW} EXIT{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} +44 7418310635\t {RED}[{WHITE}12{RED}]{WHITE} +44 7700184822\t {RED}[{WHITE}22{RED}]{WHITE} +44 7488810909\t {RED}[{WHITE}32{RED}]{WHITE} +44 7488810608\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} +44 7451286650\t {RED}[{WHITE}13{RED}]{WHITE} +44 7700184821\t {RED}[{WHITE}23{RED}]{WHITE} +44 7488810908\t {RED}[{WHITE}33{RED}]{WHITE} +44 7488810607\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} +44 7893106709\t {RED}[{WHITE}14{RED}]{WHITE} +44 7700184820\t {RED}[{WHITE}24{RED}]{WHITE} +44 7488810904\t {RED}[{WHITE}34{RED}]{WHITE} +44 7488810606\n")
        print(
            f"\t{RED}[{WHITE}05{RED}]{WHITE} +44 7893106708\t {RED}[{WHITE}15{RED}]{WHITE} +44 7700184818\t {RED}[{WHITE}25{RED}]{WHITE} +44 7488811009\t {RED}[{WHITE}35{RED}]{WHITE} +44 7488810605\n")
        print(
            f"\t{RED}[{WHITE}06{RED}]{WHITE} +44 7893106706\t {RED}[{WHITE}16{RED}]{WHITE} +44 7700184817\t {RED}[{WHITE}26{RED}]{WHITE} +44 7488810903\t {RED}[{WHITE}36{RED}]{WHITE} +44 7488810604\n")
        print(
            f"\t{RED}[{WHITE}07{RED}]{WHITE} +44 7700185280\t {RED}[{WHITE}17{RED}]{WHITE} +44 7700184816\t {RED}[{WHITE}27{RED}]{WHITE} +44 7488810902\t {RED}[{WHITE}37{RED}]{WHITE} +44 7488810600\n")
        print(
            f"\t{RED}[{WHITE}08{RED}]{WHITE} +44 7488843894\t {RED}[{WHITE}18{RED}]{WHITE} +44 7700184815\t {RED}[{WHITE}28{RED}]{WHITE} +44 7488811004\t {RED}[{WHITE}38{RED}]{WHITE} +44 7458196163\n")
        print(
            f"\t{RED}[{WHITE}09{RED}]{WHITE} +44 7700185281\t {RED}[{WHITE}19{RED}]{WHITE} +44 7406613757\t {RED}[{WHITE}29{RED}]{WHITE} +44 7488811003\t {RED}[{WHITE}39{RED}]{WHITE} +44 7458196950\n")
        print(
            f"\t{RED}[{WHITE}10{RED}]{WHITE} +44 7700184823\t {RED}[{WHITE}20{RED}]{WHITE} +44 7406613756\t {RED}[{WHITE}30{RED}]{WHITE} +44 7488811001\t {RED}[{WHITE}40{RED}]{WHITE} +44 7458196951")

    def Sweden():
        Output.clear()
        Output.logo()
        print(f"\n{RED}[REQ] {YELLOW}Sweden Numbers: \n")

        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} +46 765196294\t {RED}[{WHITE}11{RED}]{WHITE} +46 731297727\t {RED}[{WHITE}21{RED}]{WHITE} +46 731295135\t {RED}[{WHITE}31{RED}]{WHITE} +46 731291503\t {RED}[{WHITE}99{RED}]{YELLOW} EXIT{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} +46 769436252\t {RED}[{WHITE}12{RED}]{WHITE} +46 731297726\t {RED}[{WHITE}22{RED}]{WHITE} +46 731295002\t {RED}[{WHITE}32{RED}]{WHITE} +46 731291502\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} +46 769436470\t {RED}[{WHITE}13{RED}]{WHITE} +46 731297019\t {RED}[{WHITE}23{RED}]{WHITE} +46 731295001\t {RED}[{WHITE}33{RED}]{WHITE} +46 731297792\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} +46 769436246\t {RED}[{WHITE}14{RED}]{WHITE} +46 731297018\t {RED}[{WHITE}24{RED}]{WHITE} +46 731295000\t {RED}[{WHITE}34{RED}]{WHITE} +46 731297730\n")
        print(
            f"\t{RED}[{WHITE}05{RED}]{WHITE} +46 765196089\t {RED}[{WHITE}15{RED}]{WHITE} +46 731297013\t {RED}[{WHITE}25{RED}]{WHITE} +46 731291509\t {RED}[{WHITE}35{RED}]{WHITE} +46 731297790\n")
        print(
            f"\t{RED}[{WHITE}06{RED}]{WHITE} +46 731297792\t {RED}[{WHITE}16{RED}]{WHITE} +46 731295142\t {RED}[{WHITE}26{RED}]{WHITE} +46 731291508\t {RED}[{WHITE}36{RED}]{WHITE} +46 731297734\n")
        print(
            f"\t{RED}[{WHITE}07{RED}]{WHITE} +46 731297733\t {RED}[{WHITE}17{RED}]{WHITE} +46 731295141\t {RED}[{WHITE}27{RED}]{WHITE} +46 731291507\t {RED}[{WHITE}37{RED}]{WHITE} +46 731297732\n")
        print(
            f"\t{RED}[{WHITE}08{RED}]{WHITE} +46 731297730\t {RED}[{WHITE}18{RED}]{WHITE} +46 731295139\t {RED}[{WHITE}28{RED}]{WHITE} +46 731291506\t {RED}[{WHITE}38{RED}]{WHITE} +46 731297729\n")
        print(
            f"\t{RED}[{WHITE}09{RED}]{WHITE} +46 731297731\t {RED}[{WHITE}19{RED}]{WHITE} +46 731295138\t {RED}[{WHITE}29{RED}]{WHITE} +46 731291505\t {RED}[{WHITE}39{RED}]{WHITE} +46 731297725\n")
        print(
            f"\t{RED}[{WHITE}10{RED}]{WHITE} +46 731297728\t {RED}[{WHITE}20{RED}]{WHITE} +46 731295136\t {RED}[{WHITE}30{RED}]{WHITE} +46 731291504\t {RED}[{WHITE}40{RED}]{WHITE} +46 731297017\n")

    def France():
        Output.clear()
        Output.logo()
        print(f"\n{RED}[REQ] {YELLOW}France Numbers: \n")
        print(
            f"\t{RED}[{WHITE}01{RED}]{WHITE} +33 757130424\t {RED}[{WHITE}11{RED}]{WHITE} +33 757137385\t {RED}[{WHITE}21{RED}]{WHITE} +33 757130741\t {RED}[{WHITE}31{RED}]{WHITE} +33  757137408\t {RED}[{WHITE}99{RED}]{YELLOW} EXIT{WHITE}\n")
        print(
            f"\t{RED}[{WHITE}02{RED}]{WHITE} +33 757137387\t {RED}[{WHITE}12{RED}]{WHITE} +33 757137382\t {RED}[{WHITE}22{RED}]{WHITE} +33 757130740\t {RED}[{WHITE}32{RED}]{WHITE} +33 757137409\n")
        print(
            f"\t{RED}[{WHITE}03{RED}]{WHITE} +33 757137388\t {RED}[{WHITE}13{RED}]{WHITE} +33 757137381\t {RED}[{WHITE}23{RED}]{WHITE} +33 757131519\t {RED}[{WHITE}33{RED}]{WHITE} +33 757130284\n")
        print(
            f"\t{RED}[{WHITE}04{RED}]{WHITE} +33 757130420\t {RED}[{WHITE}14{RED}]{WHITE} +33 757137404\t {RED}[{WHITE}24{RED}]{WHITE} +33 757131518\t {RED}[{WHITE}34{RED}]{WHITE} +33 757130279\n")
        print(
            f"\t{RED}[{WHITE}05{RED}]{WHITE} +33 757130955\t {RED}[{WHITE}15{RED}]{WHITE} +33 757137380\t {RED}[{WHITE}25{RED}]{WHITE} +33 757131517\t {RED}[{WHITE}35{RED}]{WHITE} +33 757137305\n")
        print(
            f"\t{RED}[{WHITE}06{RED}]{WHITE} +33 757137389\t {RED}[{WHITE}16{RED}]{WHITE} +33 757137403\t {RED}[{WHITE}26{RED}]{WHITE} +33 757131516\t {RED}[{WHITE}36{RED}]{WHITE} +33 757137402\n")
        print(
            f"\t{RED}[{WHITE}07{RED}]{WHITE} +33 757137388\t {RED}[{WHITE}17{RED}]{WHITE} +33 757137308\t {RED}[{WHITE}27{RED}]{WHITE} +33 757131514\t {RED}[{WHITE}37{RED}]{WHITE} +33 757130279\n")
        print(
            f"\t{RED}[{WHITE}08{RED}]{WHITE} +33 757130955\t {RED}[{WHITE}18{RED}]{WHITE} +33 757137304\t {RED}[{WHITE}28{RED}]{WHITE} +33 757131513\t {RED}[{WHITE}38{RED}]{WHITE} +33 757137307\n")
        print(
            f"\t{RED}[{WHITE}09{RED}]{WHITE} +33 757130320\t {RED}[{WHITE}19{RED}]{WHITE} +33 757137300\t {RED}[{WHITE}29{RED}]{WHITE} +33 757131512\t {RED}[{WHITE}39{RED}]{WHITE} +33 757130278\n")
        print(
            f"\t{RED}[{WHITE}10{RED}]{WHITE} +33 757137386\t {RED}[{WHITE}20{RED}]{WHITE} +33 757130742\t {RED}[{WHITE}30{RED}]{WHITE} +33 757137384\t {RED}[{WHITE}40{RED}]{WHITE} +33 757137306\n")

import concurrent.futures
import random
import string
from pystyle import Anime , Center, Colorate, Colors, Write
import webbrowser
import tls_client
from colorama import Fore, Style
import dtypes
import os

pussy = (Write.Input("""\n┌────(Token Joiner)-[Want To Install Module? (Y/N)]
└────$""", Colors.red_to_blue, interval=0.02))

if pussy.lower() == 'y':

    os.system("pip install -r requirements.txt")

    Write.Print("""\n┌────(Token Joiner)-[✓] Requirements Installed Successfully!""", Colors.red_to_blue, interval=0.02)

elif pussy.lower() == 'n':
    
    Write.Print("""\n┌────(Token Joiner)-Skipping Requirements Installation...""", Colors.red_to_blue, interval=0.02)
else:
    Write.Print("""\n┌────(Token Joiner)-Invalid Choice. Please enter 'Y' or 'N'""", Colors.red_to_blue, interval=0.02)

join = r"""


 _____     _                  ___       _                 
|_   _|   | |                |_  |     (_)                
  | | ___ | | _____ _ __       | | ___  _ _ __   ___ _ __ 
  | |/ _ \| |/ / _ \ '_ \      | |/ _ \| | '_ \ / _ \ '__|
  | | (_) |   <  __/ | | | /\__/ / (_) | | | | |  __/ |   
  \_/\___/|_|\_\___|_| |_| \____/ \___/|_|_| |_|\___|_|   


                                      
                                             Press Enter └────$"""
                                                   
Anime.Fade(Center.Center(join), Colors.red_to_blue, Colorate.Vertical, interval=0.080, enter=True)
webbrowser.open('https://discord.com/invite/NTOP')
webbrowser.open('https://github.com/ReXx4SuRe/')
                                                          
                                                          

class Joiner:
    def __init__(self, data: dtypes.Instance) -> None:
        self.session = data.client
        self.session.headers = data.headers
        self.get_cookies()
        self.instance = data

    def rand_str(self, length: int) -> str:
        return ''.join(random.sample(string.ascii_lowercase + string.digits, length))

    def get_cookies(self) -> None:
        site = self.session.get("https://discord.com")
        self.session.cookies = site.cookies

    def join(self) -> None:
        self.session.headers.update({"Authorization": self.instance.token})
        result = self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}", json={
            'session_id': self.rand_str(32),
        })

        if result.status_code == 200:
            print(f"[\x1b[38;5;46m+\x1b[0m] Joined server")
        else:
            print(f"[\x1b[38;5;9m-{Fore.RESET}] Failed to join server")

class logger:
    colors_table = dtypes.OtherInfo.colortable

    @staticmethod
    def printk(text) -> None:
        print(f"[>] {text}")

    @staticmethod
    def convert(color):
        return color if color.__contains__("#") else logger.colors_table[color]

    @staticmethod
    def color(opt, obj):
        return f"{logger.convert(opt)}{obj}{Style.RESET_ALL}"




Write.Print("                     ______      __                     __      _                                            \n", Colors.red_to_blue, interval=0.000) 
Write.Print("                    /_  __/___  / /_____  ____         / /___  (_)___  ___  _____                            \n", Colors.red_to_blue, interval=0.000) 
Write.Print("                     / / / __ \/ //_/ _ \/ __ \   __  / / __ \/ / __ \/ _ \/ ___/                            \n", Colors.red_to_blue, interval=0.000) 
Write.Print("                    / / / /_/ / ,< /  __/ / / /  / /_/ / /_/ / / / / /  __/ /                                \n", Colors.red_to_blue, interval=0.000) 
Write.Print("                   /_/  \____/_/|_|\___/_/ /_/   \____/\____/_/_/ /_/\___/_/                                 \n", Colors.red_to_blue, interval=0.000) 
Write.Print("                                                                                                             \n", Colors.red_to_blue, interval=0.000) 
Write.Print("            ════════════════════════════════════════════════════════════════════════════                 \n", Colors.red_to_blue, interval=0.000) 
Write.Print("               Developer - rex.4sure  ||   NUKERS TERRITORY    ||    Discord.gg/ntop                   \n", Colors.red_to_blue, interval=0.000) 
Write.Print("            ════════════════════════════════════════════════════════════════════════════              \n\n\n", Colors.red_to_blue, interval=0.000) 

                                                         

class intilize:
    @staticmethod
    def start(i):
        Joiner(i).join()
        
if __name__ == '__main__':
    with open("tokens.txt") as file:
        tokens = [line.strip() for line in file]

    instances = []
    max_threads = 5
    invite = Write.Input("""┌────(Token Joiner)-[INVITE LINK]
└────$""", Colors.red_to_blue, interval=0.02)
    
    try:
        invite=invite.split("/")[-1]
    except:
        pass

    for token_ in tokens:
        header = dtypes.OtherInfo.headers
        instances.append(
            dtypes.Instance(
                client=tls_client.Session(
                    client_identifier=f"chrome_{random.randint(110, 115)}",
                    random_tls_extension_order=True,
                ),
                token=token_,
                headers=header,
                invite=invite,
            )
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in instances:
            executor.submit(intilize.start, i)

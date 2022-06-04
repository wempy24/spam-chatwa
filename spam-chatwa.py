import requests, os, sys, json, time
from time import sleep

def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)

url_api_spam_wa = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

os.system('clear')
print ('\033[36;1mFollow Ig Ku Ngab \033[37m@azsa_.24 \033[36bos! :v')
os.system('termux-open-url https://www.instagram.com/azsa_.24/')
sleep(5)
os.system("clear")
print ("")
mengetik("\033[31;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[36;1m██║     ██║ █████╗")
mengetik("\033[31;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[36;1m██║ ██  ██║██╔══██╗")
mengetik("\033[31;1m ███████╗██████╔╝███████║██╔████╔██║ \033[36;1m██║████╔██║███████║")
mengetik("\033[31;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[36;1m████  ████║██╔══██║")
mengetik("\033[31;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[36;1m███║   ███║██║  ██║")
mengetik("\033[31;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[36;1m ╚═╝    ╚═╝╚═╝  ╚═╝")
print ("")
mengetik("\033[33;1m╔════════════════════════════════════════════════╗")
mengetik("\033[33;1m║  \033[36;1m [•] Authour : WEM GANS                      \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m [•] GitHub  : https:github.com/wempy24      \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m [•] Instagram : azsa_.24                    \033[33;1m ║")
mengetik("\033[33;1m╚════════════════════════════════════════════════╝")
print ("")
mengetik("\033[36;1m╔═══════════════════════════╗")
mengetik("\033[36;1m║\033[33;1m GUNAKAN DENGAB BJIAK NGAB\033[36;1m ║")
mengetik("\033[36;1m╚═══════════════════════════╝")
sleep(1)
print ("")
nomor = input("\n[+] Input Nomor : ")
jumlah = input("[?] Jumlah Spam : ")
print()
data = {
"nomor": nomor
}
for free_tutorial in range(int(jumlah)):
        wem = requests.get(url_api_spam_wa, params=data)
        if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in wem.text:
                print("[✓] Berhasil Tod Jangan Lupa Follow IG @azsa_.24")
        else:
                print("[×] Gagal Tod Jangan Lupa Follow IG @azsa_.24")
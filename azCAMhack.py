import requests, re , colorama
colorama.init()
print("""
 
 █████╗    ███████╗         ██████╗ █████╗ ███╗   ███╗          
██╔══██╗        ██║       ██╔═════╝██╔══██╗████╗ ████║          
███████║      ██ ╔╝█████╗ ██║      ██║  ██ ██ █║██╔██║     
██╔══██║    ██     ╚════╝ ██║      ██╔══██║██║╚██╔╝██║     
██║  ██║   ██              ██████╗ ██║  ██║██║ ╚═╝ ██║               
██║  ██║   ███████         ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  

              AMYTsecurity 
Azerbaijan                   

""")

try:
    print()
    countries = ["AZ", "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = 1
    if num not in range(1, 91+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(f"https://www.insecam.org/en/bycountry/{country}", headers=headers)
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()

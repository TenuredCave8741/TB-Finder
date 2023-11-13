import requests
import re
from colorama import Fore, Style, init
from bs4 import BeautifulSoup

init()

banner_print = print(f"""{Fore.RED}

    _________ ______     _______ _________ _        ______   _______  _______ 
    \__   __/(  ___ \   (  ____ \\__   __/( (    /|(  __  \ (  ____ \(  ____ )
       ) (   | (   ) )  | (    \/   ) (   |  \  ( || (  \  )| (    \/| (    )|
       | |   | (__/ /   | (__       | |   |   \ | || |   ) || (__    | (____)|
       | |   |  __ (    |  __)      | |   | (\ \) || |   | ||  __)   |     __)
       | |   | (  \ \   | (         | |   | | \   || |   ) || (      | (\ (   
       | |   | )___) )  | )      ___) (___| )  \  || (__/  )| (____/\| ) \ \__
       )_(   |/ \___/   |/       \_______/|/    )_)(______/ (_______/|/   \__/
                                                                          
                                                              
            """)


def verificacion(user, plataforma_url):
    linkfound = re.search(patron, plataforma_url)

    if linkfound:
        url = linkfound.group()
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}Perfil de {user} encontrado: {url}{Style.RESET_ALL}")
        elif response.status_code == 404:
            print(f"{Fore.RED}Error: no se pudo encontrar el perfil en: {plataforma_url}{Style.RESET_ALL}")
        else:
            print("Error de búsqueda.")


if __name__ == "__main__":
    banner_print
    nombredeusuario = input("Introduce el nombre de usuario que desea buscar: ")

    plataformas = {
        "GitHub": f"https://github.com/{nombredeusuario}",
        "TikTok": f"https://www.tiktok.com/@{nombredeusuario}",
        "Replit": f"https://replit.com/@{nombredeusuario}",
}
    patron = r'https?://\S+'

    for plataforma, url in plataformas.items():
        verificacion(nombredeusuario, url)
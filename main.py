import requests
from bs4 import BeautifulSoup

def main():
    
    url_input = input("Enter URL here: ")
    url = url_input
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    
if __name__ == "__main__": 
    main()
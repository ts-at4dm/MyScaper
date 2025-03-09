import requests
from bs4 import BeautifulSoup

def main():
    
    url_input = input("Enter URL here: ") # Takes input from the user
    response = requests.get(url_input) # requests the data from the given URL
    
    soup = BeautifulSoup(response.text, 'html.parser') # Takes raw data, parses the raw data into a 'BeautifulSoup' Object
    
    print(soup) # Prints the data to the console for testing
    
    # Writes the data to an output file
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(str(soup))
    
if __name__ == "__main__": 
    main()
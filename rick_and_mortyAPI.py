# Rick and Morty API Test
import requests

base_url = 'https://rickandmortyapi.com/api'
endpoint = 'character'

def character_info(name):
    url = f"{base_url}/{endpoint}/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data for {name}. Status code: {response.status_code}")

def req():
    char_name = input("Enter the name of any Rick and Morty character: ").strip()
    char_info = character_info(char_name)
    if char_name == "" or char_name is None:  # Exit code for empty input
        print("No character name provided. Exiting...")
        return
    elif char_name.lower() == "exit":  # Exit code
        print("Exiting...")
        return

    if char_info and 'results' in char_info:
        for character in char_info['results']:
            print(f"Image: {character['image']}")
            print(f"Name: {character['name']}")
            print(f"ID: {character['id']}")
            print(f"Status: {character['status']}")
            print(f"Species: {character['species']}")
            print(f"Origin: {character['origin']['name']}")
            print(f"Location: {character['location']['name']}")
req();
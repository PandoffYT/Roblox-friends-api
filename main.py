import os
import requests
import json
import winshell
from winshell import shortcut

def get_friends(user_id):
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return [(friend['id'], friend['name'], friend['displayName']) for friend in data.get('data', [])]
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def create_shortcut(target_url, shortcut_path):
    with winshell.shortcut(shortcut_path) as link:
        link.path = target_url
        link.description = "Roblox User Profile"

def main():
    user_id = input("Enter the Roblox user ID: ")
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder = os.path.join(desktop, "SCRIPT_FRIENDS")
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    friends = get_friends(user_id)
    
    for friend_id, friend_name, display_name in friends:
        profile_url = f"https://www.roblox.com/users/{friend_id}/profile"
        shortcut_name = os.path.join(folder, f"{friend_name}.lnk")
        create_shortcut(profile_url, shortcut_name)
        print(f"Created entry for \"{display_name}\" (as \"{friend_name}\")")
    
    input("Press any key to exit...")

if __name__ == "__main__":
    main()

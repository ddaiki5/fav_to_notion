from get_fav import get_fav, setting_api
from set_fav_to_notion import add_pages, setting_client

import os

def main():
    api = setting_api()
    client = setting_client()
    
    target = os.environ.get("TARGET_ID")
    favs = get_fav(api, target, count=20)
    add_pages(client, favs)
    
    return 


if __name__ == "__main__":
    main()
    print("Complete databse update.")
    
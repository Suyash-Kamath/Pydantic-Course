import requests

def fetch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response=requests.get(url)
    # we get the response as a string , it looks like an object but it is a string
    data=response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username,country=fetch_random_user_freeapi()
        print(f"Username: {username}\n Country: {country}")
    except Exception as e:
         print(str(e))

if __name__ =="__main__":
    main()

import requests

def get_art_work(artist,limit):
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search",
                                {"q":artist,"limit":limit})
        response.raise_for_status()

    except:
        print('There was an error getting the artwork')
        return []
    
    content = response.json()
    return [artist['title'] for artist in content['data']]
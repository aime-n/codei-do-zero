import requests

# Define your API key here
API_KEY = "1f1e861cb85a624a24a4d969c230a10d"

import re

def remove_links(text):
    # Define a regex pattern to match the links enclosed within <>
    pattern = r'<a href="[^>]+">Read more on Last\.fm</a>.'
    
    # Use the re.sub() method to remove all matched patterns
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text


def fetch_track_info(artist_name, track_name):
    # Define the endpoint URL (include method, track, artist, api_key, and format as parameters)
    url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={artist_name}&track={track_name}&format=json"
    
    # Make the GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Load the JSON data from the response
        data = response.json()
        
        # Extract and print track information
        track = data.get('track')
        if track:
            print(f"Track Name: {track.get('name')}")
            # print(f"Artist: {track['artist']['name']}")
            # print(f"Album: {track['album']['title']}")
            # print(f"Listeners: {track.get('listeners')}")
            # print(f"Playcount: {track.get('playcount')}")
            # tags = [i['name'] for i in track.get('toptags').values()]
            tags = track.get('toptags')['tag']
            tags = [dic['name'] for dic in tags]
            print(f"Tags: {tags}")
            try:
                wiki = remove_links(track.get('wiki')['summary'])
                wiki = wiki[:100]
                print(f"Wiki: {wiki}")
                return tags, wiki
            except:
                print(f'{track_name} não achou wiki')
                return tags, None

        else:
            print("Track not found.")
    else:
        print(f"Failed to retrieve the track info. Status code: {response.status_code}")


if __name__ == '__main__':
    # Example usage:
    fetch_track_info("the beatles", "a day in the life")


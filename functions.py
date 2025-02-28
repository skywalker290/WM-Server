import requests
import os

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:        
        image_name = os.path.join('Images', image_url.split("/")[-1])
        with open(image_name, 'wb') as f:
            f.write(response.content)
        return image_name
    return None
    
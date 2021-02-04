#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=gT8fYoCsl1LkiFELTUe1kBKSPpMgxAVoVGwSmG6F").json()
    
   # img_links = []

    camera = input('Choose a camera >')
    link = None

    for pic in range(len(roverresp['photos'])):

        if camera == roverresp['photos'][pic]['camera']['name']:
            
            link = roverresp['photos'][pic]['img_src']
            rover = roverresp['photos'][pic]['rover']['name']
            dt_taken = roverresp['photos'][pic]['earth_date']

            print(rover, '\n', dt_taken, '\n', link)

    if link == None:
        print('There are no photos for this camera or this rover does not have the camera type you entered.')

            
if __name__ == "__main__":
    main()

import requests
from ascii_art import * 
from termcolor import cprint, colored

NEWLINE = '\n'

def current_location():
    # Gets the user's current location from ipinfo.io 
    
    loc_api = "https://ipinfo.io/loc"
    loc_req = requests.get(loc_api).text
    lat, long = (float(ll) for ll in loc_req.split(','))
    return lat, long

lat, long = current_location()
print(f'Lat: {lat}')
print(f'Long: {long}')
quit()

cprint(NEWLINE.join(sunny), 'yellow')
cprint(NEWLINE.join(clouds), 'white')
cprint(NEWLINE.join(rain), 'blue')
cprint(NEWLINE.join(drizzle), 'cyan')
cprint(NEWLINE.join(snow), 'white')
cprint(NEWLINE.join(fog), 'grey')

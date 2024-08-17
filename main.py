from weather import get_weather
from glyphs import *
from datetime import datetime

NEWLINE = '\n'

def is_nighttime():
	hour = datetime.now().hour
	# naive approach - day-time defined as 6:00 AM -> 8:00 PM
	nighttime = not (6 <= hour <= 20)
	return nighttime

def select_glyph(condition_id, wind_speed):
    category, subcategory = condition_id // 100, condition_id % 100
    nighttime = is_nighttime()
    
    match category, subcategory, nighttime:
        case 8,(2|3): glyph = partial_clouds.fullcolor()
        case 8, 0, True: glyph = night.fullcolor()
        case 2,_,_: glyph = thunderstorm.fullcolor()
        case 5,_,_: glyph = rain.fullcolor()
        case _,_,_: glyph = "?"

    return glyph

def main():

    weather = get_weather()
    print(weather)
    glyph = select_glyph(weather.condition_id, 10)

    print(NEWLINE.join(glyph))

main()

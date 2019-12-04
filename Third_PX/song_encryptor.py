import re
pattern = r"^([A-Z])([a-z' ]+):([A-Z ]+)$"

final_artist = ''
final_song = ''

while True:
    command = input()
    if command == 'end':
        break
    match = re.match(pattern, command)
    if match:
        artist = f'{match.group(1)}{match.group(2)}'
        key = len(artist)
        song = f'{match.group(3)}'
        for i in artist:
            final_artist = final_artist + (chr(ord(i)+key))
#TODO ASCII Incrementation and logic!

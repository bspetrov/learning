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
            if i.isalpha():
                sum = ord(chr(key)) + ord(i)
                if sum > ord('z'):
                    n = sum - ord('z')
                    final_artist = final_artist + (chr(ord('a') + n-1))
                else:
                    final_artist = final_artist + (chr(ord(i) + key))
            elif i == ' ' or i == "'":
                final_artist = final_artist + i
        #TODO -- Finish incrementation for song!!!
        for j in song:
            if j.isalpha():
                sum = ord(chr(key)) + ord(j)
                if sum > ord('Z'):
                    n = sum - ord('Z')
                    final_song = final_song + (chr(ord('A') + n-1))
                else:
                    final_song = final_song + (chr(ord(j) + key))
            elif j == ' ' or j == "'":
                final_song = final_song + j
        print(f'Successful encryption: {final_artist}@{final_song}')
        final_song = ''
        final_artist = ''
    else:
        print(f'Invalid input!')


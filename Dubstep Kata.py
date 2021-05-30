song="WUBTHISWUBISWUBAWUBTESTWUB"
#First, find any instances of multiple "WUB"s and replace with single "WUB"
while 'WUBWUB' in song:
    song = song.replace('WUBWUB', 'WUB')
#Song should now only have single WUB's inside
#Replace WUB with ' '
song = song.replace('WUB', ' ')
#Remove any spaces from the beginning and end of the string. 
song = song.strip()
print(song)
 print('sfghsdg')
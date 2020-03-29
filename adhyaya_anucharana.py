from pydub import AudioSegment
from pydub import playback
import track_list

adhyaya_number = input("Enter the Adhyaya Number[1-16] : ")
track_name, set_name, sholka_count = track_list.playlist[adhyaya_number] 
adhyaya = AudioSegment.from_mp3(str(track_name))
seconds = 1000

ucharana_sholka = adhyaya[0:0.1]
print(type(adhyaya))
for sholka in range(0,sholka_count):
    print("Adhyaya : "+str(track_name)+" Sholka : "+str(sholka))
    begin = set_name[sholka][1] * seconds
    mid   = set_name[sholka][2] * seconds 
    end   = set_name[sholka][3] * seconds 
    ucharana_sholka = ucharana_sholka + adhyaya[begin: mid]*3 + adhyaya[mid: end]*3 + adhyaya[begin: end]*3


playback.play(ucharana_sholka)
    

from pydub import AudioSegment
from pydub import playback
import track_list

adhyaya_number = input("Enter the Adhyaya Number[1-16] : ")
track_name, set_name, shloka_count = track_list.playlist[adhyaya_number] 
adhyaya = AudioSegment.from_mp3(str(track_name))
seconds = 1000

ucharana_shloka = adhyaya[0:0.1]
print(type(adhyaya))
for shloka in range(0,shloka_count):
    print("Adhyaya : "+str(track_name)+" shloka : "+str(shloka))
    begin = set_name[shloka][1] * seconds
    mid   = set_name[shloka][2] * seconds 
    end   = set_name[shloka][3] * seconds 
    ucharana_shloka = ucharana_shloka + adhyaya[begin: mid]*3 + adhyaya[mid: end]*3 + adhyaya[begin: end]*3


playback.play(ucharana_shloka)
    

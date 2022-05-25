#영단어 set의 단어들의 미국식, 영국식 발음 추출 => 40분 실행 후, gtts.tts.gTTSError: 200 (OK) from TTS API, Probable cause: Unknown에러와 함께 크롤링 중단됨
from english_words import english_words_set
from gtts import gTTS #Google Text to Speech
import time 

__author__ = 'info-lab' 

#english_words_set: 대소문자로 이루어진 영어 단어 set
for input_word in english_words_set:
    time.sleep(10)
    tts = gTTS( text=input_word,lang='en', slow=False) #미국식 
    tts.save('./voice/'+input_word+'_USA_gtts.mp3')

    time.sleep(10)
    tts1 = gTTS( text=input_word,lang='en', tld='co.uk', slow=False) #영국식 
    tts1.save('./voice/'+input_word+'_UK_gtts.mp3')

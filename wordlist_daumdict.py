#영단어 set의 단어들을 다음사전에서 검색하여 미국식, 영국식 발음을 추출 => 7034개 단어들 중 다음사전에 있는 966개 수집 후 TimeoutError
 
#필요 패키지 로드
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve 
from english_words import english_words_set

for input_word in english_words_set:

	# 1) requests 라이브러리를 활용한 HTML 페이지 요청: res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
	res = requests.get('https://dic.daum.net/search.do?q='+input_word)

	# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
	soup = BeautifulSoup(res.content, 'html.parser')

	# 3) CSS Selector로 필요한 데이터 추출: 다음사전 특정 단어 검색결과 화면에서 f12키를 눌러 html태그 분석
	#단어
	word = soup.select("#mArticle > div.search_cont > div:nth-of-type(3) > div:nth-of-type(2) > div > div.search_word > strong > a > span")
	print(word[0].get_text()) # 입력한 단어와 동일한지 확인용

	word = word[0].get_text()

	#음성(미국)
	audio = soup.select("#mArticle > div.search_cont > div:nth-of-type(3) > div:nth-of-type(2) > div > div.wrap_listen > span:nth-of-type(1) > a")
	if not audio:	#크롤링된 값이 없으면(음성x)
		print("not found USA audio")
	else:
		#음성 저장
		audio_link = audio[0].attrs["href"]
		urlretrieve(audio_link, "./voice/"+word+"_USA.mp3") #단어_USA.mp3을 제목으로 갖는 음성 저장 완료

	#음성(영국)
	audio2 = soup.select("#mArticle > div.search_cont > div:nth-of-type(3) > div:nth-of-type(2) > div > div.wrap_listen > span:nth-of-type(2) > a")
	if not audio2:	#크롤링된 값이 없으면(음성x)
		print("not found USA audio")
	else:
		#음성 저장
		audio2_link = audio2[0].attrs["href"]
		urlretrieve(audio2_link, "./voice/"+word+"_UK.mp3") #단어_UK.mp3을 제목으로 갖는 음성 저장 완료

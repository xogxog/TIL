
import requests
import requests
from bs4 import BeautifulSoup #이름만봐도 beautifulsoup이 클래스인 것을 알 수 있다.

#요청을 보낼 url
url = 'https://finance.naver.com/marketindex/'

# 실제 요청을 보내고 ,응답 객체를 response 변수에 저장
response = requests.get(url) # 200 이 나오는데, 약속된 말. 200은 잘 됐다는 말

#응답 객체의 본문(text)을 출력
#print(response.text)
#print(type(response.text)) # string
 

#크롤링 : 긴 문서에서 내가 원하는 데이터를 가지고오는 행위

# requests의 역할은 html을 받아오는 것까지! 원하는 대로 사용하기 위해서는 추가적인 작업이 필요!!! =>beautifulsoup
#beautiful 라이브러리는 파이썬 라이브러리고 html에서 문서를 가지고오는 역할

#응답 객체의 본문(text)을 해석
data = BeautifulSoup(response.text, 'html.parser') # 나 분석할건데 html.paser를 써서 

print(type(response.text),type(data)) # string, bs4.BeautifulSoup

#해석한 data에서 원하는 정보를 선택하고 ,내용만 kospi에 저장
USD_value = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text # 브라우저에 원하는거 넣어서 copy selector해주고 붙여넣는다.

print(USD_value)

##크롤링의 단점
# 1. 브라우저가 아닌 상황에서 필요 없는 데이터가 너무 많음. html은 예쁜배경을 위한 코드들도 들어가있는데 여기선 필요없어..
# 2. 원하는데이터를 얻기위한 추가작업

# 1. 핵심데이터만 받을 수 없을까?
# 2. 원하는 데이터를 쉽게 접근 할 수는 없을까?

#API에 대해 이야기.

#API Server : 응용 프로그램(개발자)를 위한 데이터를 응답하는 프로그램

#API 서버로부터 받아오기 

#agify.py 확인

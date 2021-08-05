import requests

url = 'https://api.agify.io?name=michael'

#응답 json str을 dict로 파싱해서 response에 저장
response = requests.get(url).json() #json을 써야 딕셔너리 형태쓸 수 있다.

print(response) # 위의 .json()쓰지 않으면 {'name': 'michael', 'age': 69, 'count': 233482}딕셔너리형태로보이지만 string이다.
print(type(response))


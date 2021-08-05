#중간값 찾기

numbers = [
    85,72,38,80,69,65,68,96,22,49,67,
    51,61,63,87,66,24,80,83,71,60,64,
    52,90,60,49,31,23,99,94,11,25,24
]

# numbers = [ 4,3,2,1 ]
numbers.sort() # 원본값을 sort함. 반환값 없음
numbers_median = round(int(len(numbers))/2)

# 중앙값은 자료수가 홀수이냐, 짝수이냐에 따라 계산 값이 달라지므로
#if : 리스트가 홀수개일 경우, else : 리스트가 짝수개일 경우
if len(numbers) % 2 != 0 :
    print(numbers[numbers_median])
else : print((numbers[numbers_median]+numbers[numbers_median-1])/2)




#sort함수말고 for문으로 풀어보자
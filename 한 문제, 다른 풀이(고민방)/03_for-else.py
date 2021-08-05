# numbers 리스트에 4가 있을 경우 True를 출력하고, 없을 경우 False를 출력한다.

numbers = [1, 3, 7, 4, 9]

for num in numbers :
    if num == 4 : 
        print("True")
        break
else : print("False")
    
# for else 가 없는 언어에서 하는 방법

flag = bool()

for num in numbers :
    if num == 4 : 
        flag = True
        break
    else : flag = False    

if flag : print("True")
else : print("False")    

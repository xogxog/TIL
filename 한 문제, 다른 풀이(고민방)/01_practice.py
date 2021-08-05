##단어 뒤집기##
#입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = input()
#내가 작성한 코드
for i in range(len(word)-1,-1,-1) :
    print(word[i],end = "")



#swap 방법으로 풀어보기
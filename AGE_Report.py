# 실습리포트 60172437 전성배

# 이름,주민번호 입력과 출력
while(1):

 A =input("이름과 주민번호 앞 6자리를 입력하세요.")
 print(A)

# len()으로 이름 수 상관없이 이름,주민번호 구별
 name = A[0:len(A)-6]
 num=int(A[ len(A)-6 : len(A)-4 ])

# 성 입력으로 2글자이상의 성 입력가능(영어이름 가능)
 B =int(input("성이 몇글자인가요?"))
 print("성 : ", name[0:B] , "이름 : ", name[B:])

# 1920 ~ 2021 의 100살까지 나이 측정 
 if num <=21 :
   birth = num+2000
 else:
   birth = num+1900

 age = 2021-(birth)+1

 print("출생연도 :",birth , "나이:", age)
#####데이터 구조 활용 개발 리포트#####
######## 60172437 전성배 ###########

#큐 모듈 사용
import queue

#인적사항 입력, 시험 안내
stdnum = input("시험은 객관식 3문제 , 주관식 3문제로 이루어져 있습니다.\n이름학번을 순서대로 입력한 후 엔터를 누르시면 시험 시작합니다. \n")

#이름 저장
name = stdnum[0:len(stdnum)-8]

#답 , 문제 난이도 설정
ans= [1,1,3,'해싱' , '슬롯' ,'충돌']
balance =[5,5,15,15,20, 20,20]

# Q -> 사용자 답안 저장용
# T_F -> 오답 판단용
Q =queue.Queue(maxsize = len(ans))
T_F = queue.Queue(maxsize = len(ans))



#객관식 문제 함수 q -> 문제 , qnum -> 문제 개수 확인 , a-> 보기 , 개수 변경 가능
def question_m(q , qnum, a ):
  
  print("(객관식)" )
  print("문제 ",qnum,"번: ",q)

  for n in range(1,5):
    print(n,'번 ', a[n-1]) 

  c=0
  while(c==0):

   choice = input()

   if (len(choice)>1 ): # 숫자 이외의 값 입력할 경우
     print('숫자만을 입력해주세요') 

   elif (int( choice) > len(a) or int( choice) < 1):  # 답안 외 번호를 입력할 경우
     print('잘못된 번호입니다. 선택지에서 골라주세요') 

   else:
     choice = int(choice)
     c=1
 
   Q.put(choice)
  

#주관식 문제 함수  q -> 문제 , qnum -> 문제 개수 확인
def question_e(q , qnum):
  
  
  print("(객관식)" )
  print("문제 ",qnum,"번: ",q)
  print('(단어만을 입력해주세요.)')

  choice = input()
  
  Q.put(choice)


    
#문제 출제
q1 = '1+1은?'
a1=[2,4,6,8]
question_m(q1 , 1, a1)

q2 = "속담 '_ 쫒던 개 지붕 쳐다본다'에서 _에 들어갈 말은?"
a2=['닭','고양이','소','비둘기' , '호랑이']
question_m(q2 , 2, a2)

q3 = '정렬 알고리즘 중 간단한 정렬 알고리즘에 속하는 정렬은?'
a3=['쉘정렬','삽입정렬','병합정렬','퀵정렬']
question_m(q3 , 3, a3)

q4 = '키 값에 직접 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근하는 정렬?'
question_e(q4  , 4)

q5 = '행렬의 행과 열처럼 해시테이블에서 역할을 하는 구조는 버킷과 _가 있다, _에 들어갈 말은 ?'
question_e(q5  , 5)

q6 = '서로 다른 키를 갖는 항목들이 같은 해시 주소를 가지는 현상은?'
question_e(q6 , 6 )



# 전체 답안 출력 ,오답 판단
print(name,'님의 답 : ')

for n in range(len(ans)):

 m= Q.get()
 if( m == ans[n]):
    T_F.put('o')
 else:
   T_F.put('x')
 print(n+1,'번: ', m)

  


# 실제 정답 출력
print('\n정 답 ' )
for n in range(len(ans)):
  print(n+1,'번: ', ans[n] )


#정답여부 출력, 정답여부로 최종 점수 계산
print('\n정답여부' )

score=0
for n in range(len(ans)):
  i= T_F.get()

  if (i == 'o'):
    score += balance[n] 
  print(n+1,'번 : ', i )  


# 등급 계산 후 점수,등급 출력


A = 90 ; B = 80 ; C=70 ; D= 60
if (score >= A):
  grade = 'A'
elif (A > score >= B):
  grade = 'B'
elif (B > score >= C):
  grade = 'C'
elif (C > score >= D ):
  grade = 'D'
elif (D > score):
  grade = '재시험 요망'    

print('\n',name, '님의 점수는',score,'입니다.')
print('당신의 등급은',grade,'입니다.')

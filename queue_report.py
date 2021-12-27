#큐리포트 60172437 전성배
print("스택리포트, 학번:60172437 , 이름:전성배")

 
large=[]
small=[]
top=[]  

#큐 코드 모듈 사용 
import queue
Q=queue.Queue(maxsize = 10)

#스택 코드 직접 개발
def sb_is_empty():
  return len(top) == 0

def sb_push(item):
  top.append(item)

def sb_pop():
  return top.pop(-1)

# 숫자 입력 , 큐에 삽입
for n in range(1,11):
  print(n,"번째 숫자를 입력하세요",end="") 
  i=int(input())
  Q.put(i)

# 큐의 값 꺼내며 화면출력 , 스택에 삽입
print("큐에 삽입된 숫자는",end='')

for n in range(1,11):
  m= Q.get()
  print(m, end=' ')
  sb_push(m)
  
print( "입니다.")

#기준숫자 입력 , 숫자분류
standard = int(input("기준숫자를 입력하세요? "))

while sb_is_empty() == False:
 c=sb_pop()
 
 if c >= standard :
   large.append(c)
 else:
   small.append(c)

print("기준숫자보다 크거나 같은 수들 : ")
print(large)
print("기준숫자보다 작은 수들 : ")
print(small)

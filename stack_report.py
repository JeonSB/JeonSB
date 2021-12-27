#스택리포트 60172437 전성배
print("스택리포트, 학번:60172437 , 이름:전성배")

top=[]  
large=[]
small=[]

def sb_is_empty():
  return len(top) == 0

def sb_push(item):
  top.append(item)

def sb_pop():
  return top.pop(-1)


for n in range(1,11):
  print(n,"번째 숫자를 입력하세요",end="") 
  i=int(input())
  sb_push(i)
print("입력한 숫자는",top, "입니다.")

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

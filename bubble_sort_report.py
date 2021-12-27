#정렬 리포트, 학번:60172437, 이름:전성배

#10개 정수 입력
original=[]
for n in range(1,11):
  print(n,"번째 숫자를 입력하세요",end=" ") 
  i=int(input())
  original.append(i)

#새로운 영역에 복사
copy=[]
for n in range(0,10):
 copy.append(original[n])

#이진정렬
n=len(copy)
count1=0
count2=0

for i in range(n-1,0,-1):
  for j in range(i):
    print(copy[j], '과',copy[j+1],'을 비교',end=' ')
    count1 = count1+1
    print('[비교 : ',count1,']')

    if(copy[j]>copy[j+1]):
      print(copy[j], '과',copy[j+1],'을 교환',end=' ')
      count2 = count2 + 1
      print('[이동 : ',count2,']')
      copy[j], copy[j+1] = copy[j+1], copy[j]

#정렬결과 출력
print('정렬결과')
print('원본 목록 :',original)
print('정렬 목록 :',copy)
print('총 비교횟수 : ',count1)
print('총 이동횟수 : ',count2)
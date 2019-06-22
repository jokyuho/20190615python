# 문제1 주민번호 성별체크
'''
a = input("주민번호 입력 : ")

if a[7] == '1' or a[7] == '3':
    print("남자")
elif a[7] == '2' or a[7] == '4':
    print("여자")
'''

# 문제2 구구단 출력하기
'''
for i in range(2,10):        # ①번 for문
    print("\n--[%d단]--" %i)
    for j in range(1, 10):   # ②번 for문
         print("%d x %d = %d" %(i,j,i*j))  
'''
'''
for i in range(1,10):        # ①번 for문

    for j in range(2, 10):   # ②번 for문
         print("%d x %d = %2d" %(j,i,j*i), end=' ') # %2d는 공간 확보때문에 씀.
         # print("{} x {} = {:2}" .format(j,i,j*i), end=' ')
    print()
'''
'''
# 문제3 커피가격
coffee={'아메리카노':2500,'카페라뗴':3000,'카푸치노':3500}

for c in coffee:
    print(c, end='  ')
print()

order = input("선택 : ")
for i,j in coffee.items(): # 튜플로 리턴 (키,값)
    if i==order:
        print(j)
'''

# 문제 4. 덧셈문제 맞추기
'''
import random

count = 0
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    print("%d + %d ="%(a,b))
    c=int(input())
    if a+b==c:
        print("정답!")
        count+=1
    else:
        print("오답!")
print("%d개 맞음"%count)
'''
'''
import random

count = 0
oper=['+','-','*','/']
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz,'=')
    print(eval(quiz))
    c=float(input('정답='))

    if float(eval(quiz))==c:
        print("정답!")
        count+=1
    else:
        print("오답!")

print("%d개 맞음"%count)
'''
'''
# 문제5. 시간 맞추기 게임
import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()
input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()
et = end - start
print("실제 시간 : ", et, "초")
print("차이 : ",abs(et-20), "초")
'''

# 문제 6. 숫자 맞추기
'''
import random
b = random.randint(1,100)
count = 0

while True:
    a = int(input("1~100사이 숫자를 입력하세요 :"))
    if a==b:
        break
    elif a>b:
        print("더 작은 수를 입력하시오.")
        count += 1
    elif a<b:
        print("더 큰 수를 입력하시오.")
        count += 1

print("당신은 %d회만에 정답을 맞추었습니다." %count) 
'''
'''
import random, time

com=random.randint(1,100)
count=0
print('답 :',com)
input("시작!")
start = time.time()
while True:
    input_no = int(input('1~100사이 숫자를 입력하세요\n'))
    count+=1
    if com==input_no:
        print('정답입니다. {}번만에 맞추셨습니다.'.format(count))
        break
    elif com>input_no:
        print("더 큰수를 입력하세요.")
    else:
        print("더 작은수를 입력하세요.")
end = time.time()
t = end-start
print('걸린 시간은 {:0f}초입니다.'.format(t))
'''
'''
# 문제 7. 로또번호생성
import random
for i in range(5):
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num in lotto):
            num=random.randint(1,45)
        lotto[x]=num
    print("로또 : ",sorted(lotto))
'''
'''
import random

for i in range(1,6):
    print("로또 : ", sorted(random.sample(range(1,46),6)))
'''
'''
# 문제8. 야구게임
import random

def F(A,N) :
    B = 0 ; S = 0
    for i in range(3) :
        if int(A[i]) == N[i] :
            S += 1
        elif int(A[i]) in N :
            B += 1
    if S == 3 :
        return 0
    else :
        return [S,B]


while True :
    T = input('야구게임 시작을 원하시면 \'시작\'을, 종료를 원하시면 \'종료\'를 입력해주세요. :')
    if T == '종료' :
        print('종료합니다.')
        break
    elif T == '시작' :
        Num = [i for i in range(1,10)]
        N = []
        for i in range(3) :
            l = len(Num)
            X = Num.pop(random.randint(0,l-1))
            N.append(X)
        print('N은 각 자리의 숫자가 모두 다른 세 자리의 자연수입니다.')
        while True :        
            while True :
                A = input('N은 얼마일까요? :')
                if 99<int(A)<1000 and A[0] != A[1] and A[1]!=A[2] and A[0] != A[2] :
                    break
                else :
                    print('각 자릿수가 서로 다른 세 자리의 자연수를 입력하세요.')
            
            if F(A,N) == 0 :
                print('홈런! 정답입니다.')
                break
            print(F(A,N)[0], '스트라이크', F(A,N)[1], '볼입니다.')

    else :
        print('다시 입력해주세요.')
        continue
'''


# 문제9. 타자게임
import random
import time

n=1
w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
q=random.choice(w)
input('시작!')
start = time.time()
while n<=5:
	print("*문제",n)
	print(q)
	x=input()
	if q == x:
	    print("통과!")
	    n=n+1
	    q=random.choice(w)
	else:
	    print("오타! 다시도전!")

end = time.time()
t = end-start
print('타자시간 : {:.0f}초'.format(t))
'''
f=open("./python_basic/word.txt", 'r')
'''
''' 쓰기연습
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
'''
''' 읽기연습
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
'''
''' 타자문제 불러오기
import random, time
w=["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]

while True:
    print("1.문제불러오기 2.타자게임 3.종료하기")
    menu = input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open('./python_basic/word.txt','r')
        line = 1
        w.clear() # 기존문제 제거하고 추가하기
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                w.append(line)
        print(w)
    elif menu=='2':
        n=1
        print("[타자 게임]준비되면 엔터!")
        input()
        start=time.time()
        q=random.choice(w)
        print(q)
        x=input()
        if q == x:
            print("통과!")
            n=n+1
            q=random.choice(w)
        else:
            print("오타! 다시 도전!")

        end = time.time()
        et=end-start
        et=format(et,".2f")
        print("타자 시간 : ",et,"초")
    elif menu=='3':
        break
'''

'''
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
'''

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

'''
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee-1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''
'''
a=0
while a<10:
    a=a+1
    if a%2 == 0: continue
    print(a)
'''
'''
# Q1. 3의 배수의 합
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:  # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result)

# Q2. 50점 이상의 총합
A = [20,55,67,82,45,33,90,87,100,25]
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
print(result)

# Q3. 별 표시하기1
i = 0
while True:
    i += 1  # while문 수행 시 1씩 증가
    if i > 4: break  # i 값이 4보다 크면 while문을 벗어난다.
    print ('*' * i)
'''
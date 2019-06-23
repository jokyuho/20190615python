import re

custlist=[]
page=-1 # 리스트는 0부터 시작이니 -1부터 하나도 안들어가면 -1임

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램종료
    ''').upper()

    if choice=="I":
        customer={'name':'','sex':'','email':'','birthyear':''}
        customer['name']=input("이름을 입력하세요 : ")

        while True:
            customer['sex']=input("성별(M/m 또는 F/f)을 입력하세요 : ")
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
        
        while True:
            customer['email']=input("이메일을 입력하세요(@포함해서) : ")
            check = 0

            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-z]{2,6}[.][a-zA-z]{2,3}$')# ^~로 시작하는, [^]은 부정 {4,10} 최소 4 최대10까지 허용
            while True:
                customer['email']=input("이메일을 입력하세요 : ")
                golbang = regex.search(customer['email']) # 입력받은 내용과 매치시켜본다.
                if golbang: # 매치가 됬으면 나가!
                    break
                else: # 매치 안됬으면 다시 쓰라하고 다시 반복문 실행
                    print('"@"를 포함한 정확한 이메일을 써주세요')
            
            check=0
            for i in custlist:
                if i['email']==customer['email']:
                    check=1
        
            if check==0:
                break
            print('중복되는 이메일이 있습니다.')


        while True:
            customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")

            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit(): # 문자열 안의 값들이 숫자값으로만 되있는지 확인하는 함수(isdigit)
                break
        
        print(customer)
        custlist.append(customer)
        print(custlist)
        # page += 1
        page=len(custlist)-1 # 마지막꺼 가리키게 해주는 작업.
        print(page)

        print("고객 정보 입력")
    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >= 0:
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")
    elif choice=="P":
        print("이전 고객 정보 조회")
        if page<=0:
            print('첫번째 페이지이므로 이전 페이지 이동이 불가합니다.')
            print(page)
        else:
            page-=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])

    elif choice=="N":
        print("다음 고객 정보 조회")
        if page>=len(custlist)-1:
            print('마지막 페이지므로 다음 페이지 이동이 불가합니다.')
            print(page)
        else:
            page+=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])

    elif choice=="U":
        print("고객 정보 수정")
        while True:
            choice1 = input('수정하려는 고객 정보의 이메일을 입력하세요.')
            idx = -1 # 인덱스가 -1이면 인덱스가 없는 것.
            for i in range(0,len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx = i
            if idx == -1:
                print('등록되지 않은 이메일입니다.')
                break
            
            choice2 = input('''
            다음 중 수정하실 정보를 골라주세요.
                  name, sex, birthyear
            (수정할 정보가 없으면 'exit' 입력)
            ''')
            if choice2 in ('name', 'sex', 'birthyear'):
                custlist[idx][choice2]= input('수정할 {}을 입력하세요 :'.format(choice2))
                break
            elif choice2 == 'exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break

    elif choice=="D":
        print("고객 정보 삭제")
        choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
        delok = 0 # 지움여부 확인 변수
        for i in range(0,len(custlist)):
            while custlist[i]['email'] == choice1:
                print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok=1
                break

            if delok == 1:
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)

    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print("잘 못 입력하셨습니다!")
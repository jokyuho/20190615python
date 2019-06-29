import pickle

data = {1: 'python', 2: 'you need'}
# type dict 딕셔너리 즉 파이썬에서 사용할 수 있는 데이터 타입.
print(type(data))

# 파일로 저장
with open("./python_basic/test.pickle",'wb') as f:
    pickle.dump(data,f)

# 파이썬 내에서 사용 바이트 형태
datab=pickle.dumps(data) # dump는 파일과 관련, dumps는 문자열과 관련
print(type(datab))

# 파일을 읽어옴.
with open("./python_basic/test.pickle",'rb') as f:
    data=pickle.load(f)
    print(data)

# 바이트 타입을 파이썬 형태의 데이타 타입으로
data1 = pickle.loads(datab)
print(data1)
print(type(data1))
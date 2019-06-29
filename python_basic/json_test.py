import json
 
# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
 
# JSON 인코딩
jsonString = json.dumps(customer)
 
# 문자열 출력
print(jsonString)
print(type(jsonString))   # class str

jsonString = json.dumps(customer, indent=4)
print(jsonString)

with open('./python_basic/data.json','wt') as f:
    f.write(jsonString)

'''
import json
 
# 테스트용 JSON 문자열
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
 
# JSON 디코딩
dict = json.loads(jsonString)
 
# Dictionary 데이타 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])
'''

# json.dumps 파이썬 내에서 바로 사용
jsonString = json.dumps(customer, indent=4)
print(jsonString)

# json.dump 파일로 바로 저장
with open('./python_basic/data.json','wt') as f:
    json.dump(customer, f, indent=4)

# json.loads json 문자를 읽어서 파이썬 객체로 변경
customer1 = json.loads(jsonString)
print(customer1)

# json.load json 파일을 읽어서 파이썬 객체로 변경
with open('./python_basic/data.json','rt') as f:
    customer2 = json.load(f)
    print(type(customer2))
    print(customer2)

# json模块
import json

# some JSON:
x = '{ "name":"Bill", "age":63, "city":"Seatle"}'

# parse x:
y = json.loads(x)
print(x)
print("这里是分割线".center(30, "*"))
print(y)
print(y["name"])
print(y["age"])
# 字典转为json
x = {
    "name": "Bill",
    "age": 63,
    "city": "Seatle"
}


y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)

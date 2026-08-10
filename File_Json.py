import json
products = [
    {"name": "Apple", "price": 3.5, "stock": 20},
    {"name": "Orange", "price": 5, "stock": 15}
]

#json.dump是储存资料 #需要放list的变量名+file (students,file)
#encoding="utf-8" 告诉电脑要换成 utf-8编码来储存或读取
#indent=4 是换成文档时排版比较好看
#ensure_ascii=False 不会把非英文和数字转换成unicode像(\u82f9\u679c)这样看不懂
#ensure_ascii=False #indent=4 (这几个需要放在存文档的地方就好)(json.dump)
with open("products.json","w",encoding="utf-8") as file: #这里的student等同于文档名，可以随便放, .json 只是方便识别是用json,放不放没关系
    json.dump(products,file,indent=4,ensure_ascii=False) #json.dump是储存资料 #需要放list的变量名+file (students,file)

with open("products.json","r",encoding="utf-8") as file:
    products = json.load(file) #json.load 读取文件的方法

for product in products:
    print(f"Product : {product['name']}\nPrice : RM {product['price']:.2f}\n")

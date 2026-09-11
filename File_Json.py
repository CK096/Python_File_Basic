import json

products = [
    {"name": "Apple", "price": 3.5, "stock": 20},
    {"name": "Orange", "price": 5, "stock": 15}
]

# ==============================
# dump() / load() (操作 JSON 文件)
# ==============================

# json.dump()
# 将 Python 资料 (list、dict...) 储存到 JSON 文件

# json.load()
# 从 JSON 文件读取资料，并转换回 Python 的 list 或 dict

# encoding="utf-8"
# 告诉 Python 使用 UTF-8 编码来储存或读取文件，避免乱码

# indent=4
# 让 JSON 文件排版更整齐，方便阅读

# ensure_ascii=False
# 中文、日文等字符直接保存，不转换成 \uXXXX

# .json 不是必须，但建议保留
# 方便辨识这是 JSON 文件

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4, ensure_ascii=False)

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

for product in products:
    print(f"Product : {product['name']}")
    print(f"Price   : RM {product['price']:.2f}")
    print()

# ==========================================
# dumps() / loads() (操作 JSON 字符串，不是文件)
# ==========================================

# json.dumps()
# 将 Python 物件 (list、dict...) 转换成 JSON 字符串 (str)

text = json.dumps(products)

print(text)
print(type(text))      # <class 'str'>

# json.loads()
# 将 JSON 字符串 (str) 转换回 Python 的 list 或 dict

data = json.loads(text)

print(data)
print(type(data))      # <class 'list'>

# 容易记的方式
# dump   -> File
# load   -> File

# dumps  -> String
# loads  -> String

# 没有 s = File（文件）
# 有 s = String（字符串）

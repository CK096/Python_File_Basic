import os

# ===========================
# Python 检测档案、资料夹
# ===========================

# 方法一：Raw String（推荐）
path = r"C:\Users\user\Desktop\workshop"

# 方法二：使用双反斜线
# 每个 '\' 都要写成 '\\'
path2 = "C:\\Users\\user\\Desktop\\workshop"

print(path)
print(path2)



# ---------------------------
# os.path.exists()
# ---------------------------
# 检查路径是否存在
#
# 语法：
# os.path.exists(path)
#
# 回传：
# True  -> 路径存在
# False -> 路径不存在

if os.path.exists(path):
    print("路径存在！")
else:
    print("路径不存在！")



# ---------------------------
# os.path.isfile()
# ---------------------------
# 检查路径是否为文件
#
# 语法：
# os.path.isfile(path)

if os.path.isfile(path):
    print("该路径为文件")



# ---------------------------
# os.path.isdir()
# ---------------------------
# 检查路径是否为资料夹（目录）
#
# 语法：
# os.path.isdir(path)

elif os.path.isdir(path):
    print("该路径为资料夹（目录）")

else:
    print("路径不存在")

import os

# ===========================
# os.path 常用函数
# ===========================

path = r"C:\Users\user\Desktop\workshop\test.txt"


# ---------------------------
# os.path.basename()
# ---------------------------
# 取得文件名称（最后一层）
#
# 语法：
# os.path.basename(path)

print(os.path.basename(path))

# 输出：
# test.txt



# ---------------------------
# os.path.dirname()
# ---------------------------
# 取得文件所在的资料夹（上一级路径）
#
# 语法：
# os.path.dirname(path)

print(os.path.dirname(path))

# 输出：
# C:\Users\user\Desktop\workshop



# ---------------------------
# os.path.join()
# ---------------------------
# 拼接路径（推荐）
#
# 语法：
# os.path.join(path1, path2, ...)
#
# 优点：
# - 自动加入正确的路径分隔符
# - Windows、Linux、macOS 都适用
# - 比自己用 "/" 或 "\" 拼接更安全

folder = r"C:\Users\user\Desktop\workshop"

file_path = os.path.join(folder, "test.txt")

print(file_path)

# 输出（Windows）：
# C:\Users\user\Desktop\workshop\test.txt



# ---------------------------
# os.path.getsize()
# ---------------------------
# 取得文件大小（单位：Byte）
#
# 语法：
# os.path.getsize(path)

print(os.path.getsize(path))

# 输出：
# 例如：1024
# 表示文件大小为 1024 Bytes（1 KB）

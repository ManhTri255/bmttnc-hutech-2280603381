import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()  # Sửa lỗi thiếu dấu "=" khi khai báo biến
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = calculate_md5(input_string)  # Sửa lỗi thiếu dấu "=" khi gán biến

print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
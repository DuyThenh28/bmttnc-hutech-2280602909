def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True 
    else:
        return False 
my_dict = {'a': 1,'b': 2,'c' :3,'d' :4 }
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("phần từ đã được xoá từ Dictionary: ", my_dict)
else:
    print("Ko tìm thấy phần từ cẩn xoá từ Dictionary.")
    
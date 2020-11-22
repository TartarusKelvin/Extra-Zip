import fileutil
import sys

to_hide_file = fileutil.Binary_File(sys.argv[1],False)
bytes_to_hide = to_hide_file.content
if len(bytes_to_hide) > 6000:
    print("File To Big")

size = len(bytes_to_hide).to_bytes(2, byteorder='little')

zip_file = fileutil.Binary_File(sys.argv[2],True)
w_count = 0
length = len(bytes_to_hide)
while w_count < len(bytes_to_hide):
    zip_file.skip(18)
    comp_length = zip_file.read_int(4)
    zip_file.skip(4)
    name_length = zip_file.read_int(2)

    to_write = 6000 if length - w_count > 6000 else length - w_count
    w_count += to_write
    size = len(to_write).to_bytes(2, byteorder='little')
    zip_file.replace_bytes(2,size)
    zip_file.insert_bytes(bytes_to_hide[w_count:to_write])
    zip_file.skip(name_length+comp_length)

zip_file.save_file(sys.argv[3])

# zip_file.seek(28)
# print(f"Adding {len(bytes_to_hide)} ({size}) bytes")
# zip_file.replace_bytes(2,size)
# zip_file.insert_bytes(bytes_to_hide)
# print("Saving")
# zip_file.save_file(sys.argv[3])
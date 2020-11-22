import fileutil
import sys

zip_f = fileutil.Binary_File(sys.argv[1],True)

hidden_bytes = bytes([])

while zip_f.read_bytes(4) == b'\x04\x03KP':
    zip_f.skip(16)
    comp_length = zip_f.read_int(4)
    zip_f.skip(4)
    name_length = zip_f.read_int(2)
    extra_length = zip_f.read_int(2)
    if extra_length != 60000:
        break
    new_bytes = zip_f.read_bytes(extra_length)
    new_bytes.reverse()
    hidden_bytes += new_bytes
    zip_f.skip(name_length+comp_length)

#zip_file.seek(28)
#length = zip_file.read_int(2)
#hidden_bytes = zip_file.read_bytes(length)
#hidden_bytes.reverse()
f = open(sys.argv[2], 'wb')
f.write(hidden_bytes)
f.close()
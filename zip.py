import fileutil


class compressed_file:
    def __init__(self,version,gpbf,method,mod_time,mod_date,crc32,comp_size,decomp_size,file_name):
        self.version = version
        self.gpbf = gpbf
        self.method = method
        self.mod_time = mod_time
        self.mod_date = mod_date
        self.crc32 = crc32
        self.comp_size = comp_size
        self.decomp_size = decomp_size
        self.file_name = file_name
        self.data = None
    def add_data(self,data):
        self.data = data
    def describe(self):
        print(f"{self.file_name}: {self.comp_size}b/{self.decomp_size}b")
        print(f"{self.data}")
    @classmethod
    def read_from_bin(cls,zip_f):
        signature = zip_f.read_bytes(4)
        if(signature != b'\x04\x03KP'):
            print("Not A File")
            return None
        version = zip_f.read_int(2)
        gpbf = zip_f.read_bytes(2)
        method = zip_f.read_bytes(2)
        mod_time = zip_f.read_bytes(2)
        mod_date = zip_f.read_bytes(2)
        crc32 = zip_f.read_bytes(4)
        comp_size = zip_f.read_int(4)
        decomp_size = zip_f.read_int(4)
        name_length = zip_f.read_int(2)
        extra_length = zip_f.read_int(2)
        file_name = zip_f.read_str(name_length)
        extra = zip_f.read_bytes(extra_length)
        ret = cls(version,gpbf,method,mod_time,mod_date,crc32,comp_size,decomp_size,file_name)
        ret.add_data(zip_f.read_bytes(comp_size))
        ret.data.reverse()
        return ret


zip_file = fileutil.Binary_File("testers\\TestN.zip",True)

comp_files = []
while True:
    new_file = compressed_file.read_from_bin(zip_file)
    if new_file == None:
        break
    comp_files.append(new_file)

for f in comp_files:
    f.describe()

print(int.from_bytes(comp_files[0].method,"big"))
for d in comp_files[0].data:
    print("{:08b}".format(d), end = "  ")
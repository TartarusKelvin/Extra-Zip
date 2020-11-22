class Binary_File:
    def __init__(self,path,endianness):
        self.endianness = endianness
        self.content = None
        with open(path,"rb") as f:
            self.content = bytearray(f.read())
        if not self.content:
            print(f"Error Opening File: {path}")
        self.pointer = 0

    def seek(self,val):
        self.pointer = val

    def read_bytes(self,n):
        to_return =  self.content[self.pointer:self.pointer+n]
        self.pointer += n
        if self.endianness:
            to_return.reverse()
        return to_return

    def read_int(self,n):
        b = self.read_bytes(n)
        return int.from_bytes(b,"little" if not self.endianness else "big")
    
    def read_str(self,n,encoding="ascii"):
        to_return = self.content[self.pointer:self.pointer+n]
        self.pointer += n
        return to_return.decode(encoding)

    def skip(self, n):
        self.pointer += n

    def replace_bytes(self,n,data):
        self.content[self.pointer:self.pointer+n] = data[:n]
        self.pointer += n

    def insert_bytes(self,data):
        self.content = self.content[:self.pointer] + data + self.content[self.pointer:]
        self.pointer += len(data)
        pass

    def dump_hex(self,width=16):
        count = 0
        for c in self.content:
            if count % width == 0:
                if count != 0:
                    print()
                print("{:04x}".format(count), end = "|  ")
            print("{:02x}".format(c), end = "  ")
            count += 1

    def save_file(self,path):
        f = open(path, 'wb')
        f.write(self.content)
        f.close()
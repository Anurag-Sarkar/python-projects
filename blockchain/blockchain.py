import hashlib
import os
import shutil
import time

class BlockChain:
        

    def __init__(self):
        self.__current_block = ""
        self.__data = ""
        self.__binary = ""


        
    def get_details(self):
        while True:
            i = input("Enter Details: ")
            if i == "0":
                break
            elif i == "x":
                exit()
            else:
                i += "\n"
                self.__data += i
        
    def mine_block(self):
        i = 1
        x = len(self.__data)
        while True:
            self.__data = self.__data[:(x-1)] + str(i)
            hash = hashlib.sha256(self.__data.encode()).hexdigest()
            binary = str(bin(int(hash, 16)).zfill(8))
            if binary[-1:-11:-1] == "0000000000":
                self.__binary = binary
                break
            i+=1
    
    def block(self):
        flag = True
        i = 1
        while flag:
            path = "blockchain/block" + str(i)
            flag = (os.path.isdir(path))
            i+=1
        self.__current_block = i-1

    def create_block(self):
        path = "blockchain/block"+str(self.__current_block)
        data_path = path + "/data.txt"
        os.mkdir(path)
        hash_path = path + "/hash.txt"
        with open(data_path , "w") as f:
            f.writelines(self.__data)

        with open(hash_path , "w") as f:
            f.writelines(self.__binary)

        prev_path = "blockchain/block"+str((self.__current_block - 1))
        prev_hash = prev_path + "/hash.txt"
        with open(prev_hash , "r") as f:
            d = f.readlines()
        nxt_hash = path + "/old_hash.txt"
        with open( nxt_hash , "w") as f:
            f.writelines(d)

    def verification(self):
        flag = True
        data = ""
        i = 1
        while flag:
            path = "blockchain/block" + str(i)
            flag = (os.path.isdir(path))
            i+=1
        block = i-2
        if block == 1:
            print("Create Block to Verify")
        else:
            for i in range(1,block):
                path = "blockchain/block" + str(i)
                data_path = path + "/data.txt"
                with open (data_path,"r") as f:
                      x = f.readlines()
                for j in x:
                    data += j
                hash = hashlib.sha256(data.encode()).hexdigest()
                binary = str(bin(int(hash, 16)).zfill(8))
                data = ""

            nxt_path = "blockchain/block" + str(i+1)
            hash_path = nxt_path + "/old_hash.txt"
            with open (hash_path,"r") as f:
                      h = f.readline()
            if h == binary:
                pass
            else:
                print("Block"+str(i)+" Data Tampered!!!")
                exit()
            

        


obj = BlockChain()

print("Verifying Blocks...Please wait")
time.sleep(1)
obj.verification()
while True:
    print("\nReady to Create blocks... Enter x to quit")
    obj.get_details()
    print("\nMining Blocks")
    obj.mine_block()
    time.sleep(1)
    print("\nCreating Block")
    obj.block()
    obj.create_block()
    time.sleep(1)
    print("\nBlock Created")

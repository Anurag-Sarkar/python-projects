#------------------FILE HANDELING------------------
# import pickle
# import os
# with open("Files/file.txt" , "br") as f:
#     l = f.read()

# with open("Files/copy.txt" , "a") as f:
#     f.write(l)

# with open("Files/file.txt" , "r") as f, open("Files/copy.txt" , "w") as fw:
#     x = f.read()
#     print(x)
#     fw.write(x)

# with open("image.jpg" , "rb") as f, open("copy.txt" , "wb") as fw:
#     x = f.read()
#     fw.write(x)
# os.remove("index sum.py")
# --------------PICKLING------------------------
# with open('lol.txt','wb') as f:
#     d = "Hello"
#     pickle.dump(d,f,3)

# with open('lol.txt','rb') as f:
#     x = pickle.load(f)
#     print(x)
#-------------lol--------------------
with open("a.png" , "rb") as f, open("q.png","wb") as fw:
    l = f.read()
    fw.write(l) 

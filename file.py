data = ["anurag",9893433603,"Arduino2560",2000]
cash = 10000
with open ("file.txt","r") as f:
    data = f.read()
    details = data.split("\n")
print(details)
    
with open ("file.txt","w") as f:
    f.write(data.replace(str(details[3]),str(cash)))
    # for i in data:
    #     f.write(str(i))
    #     f.write("\n")
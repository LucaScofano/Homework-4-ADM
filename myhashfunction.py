def myhash1(s):
    import string
     
    a = string.printable
    lst = []
    for i in a:
        lst.append(i)  
        
    encoder = []
    for j in range(len(lst)):
        encoder.append((j*3)+47)
            

    keys= lst
    values= encoder
    dictionary = dict(zip(keys, values))
   
    empty= []
    for e in s:
        empty.append(dictionary.get(e))
    str1 =  int(''.join(map(str, empty)))
    return str1%2069

        
    
myhash1("abc")
    


def myhash2(s):
    import string
     
    a = string.printable
    lst = []
    for i in a:
        lst.append(i)  
        
    encoder = []
    for j in range(len(lst)):
        encoder.append(10 + (j*17))
            

    keys= lst
    values= encoder
    dictionary = dict(zip(keys, values))
   
    empty= []
    for e in s:
        empty.append(dictionary.get(e))
    str1 =  int(''.join(map(str, empty)))
    return str1%499

print(myhash1("efrtsdf"))
print(myhash2("efrtsdf"))
    
    
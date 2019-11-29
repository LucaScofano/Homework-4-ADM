import pandas as pd


pass1 = open(r"/Users/marcodicio/Desktop/Marco/DATA/passwords1.txt").read().splitlines()
pass2 =   open(r"/Users/marcodicio/Desktop/Marco/DATA/passwords2.txt").read().splitlines()

cutpass1 = pass1[:10000]
cutpass2 = pass2[:2000]  

#Hashing all the existing passwords in the database
hash1p1 = [myhash1(str(cutpass1[i])) for i in range(len(cutpass1))]
hash2p1 = [myhash2(str(cutpass1[i])) for i in range(len(cutpass1))]

#Hashing all the possible new passwords
hash1p2 = [myhash1(str(cutpass2[i])) for i in range(len(cutpass2))]
hash2p2 = [myhash2(str(cutpass2[i])) for i in range(len(cutpass2))]

df1 = pd.DataFrame(list(zip(hash1p1, hash2p1)), columns =['Hash1', 'Hash2']) 

#Creating the bloom filter which is initially a list of all 0s
bf0 = [0]*2069

#Joining the lists(set union) of the 2 hash functions applied to the existing passwords(passwords1)
hashlist = [hash1p1,hash2p1]
listunion =  list(set().union(*hashlist))
L = len(listunion)





#Filling in the bloom filter with 1 for every index that was created from hash functions
for i in range(L):
    bf0[listunion[i]] = 1

#Now we have to see if the possible new passwords already exist according to out bloom filter.
    
newhashlist = [hash1p2,hash2p2]

#Now I creat a yesno list saying if the potential new passwords exist or not, if both has indexes in the bloom filter equal 1, then exists, else they don't.

yesno= []
for i in range(len(hash1p2)):
    if bf0[newhashlist[0][i]] == 1 and bf0[newhashlist[1][i] == 1]:
        yesno.append("probably exists")
    else:
        yesno.append("doesn't exist")
    
    
    

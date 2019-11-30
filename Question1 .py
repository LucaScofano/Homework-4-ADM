import pandas as pd
import time
import string
import time

#Loading the password files
passwords1 = open(r"/Users/marcodicio/Desktop/Marco/DATA/passwords1.txt").read().splitlines()
passwords2 = open(r"/Users/marcodicio/Desktop/Marco/DATA/passwords2.txt").read().splitlines()
pass1 = passwords1
pass2 = passwords2

#Defining the 2 hash functions to be used.Method: For each existing string character i assign a value going from 0 to n (about 150). Then i perform some 
#transformations to make the hashes random and of similar length (for same length input). I finally mod with a prime number to minimise collisions.

def myhash1(s):
   
    a = string.printable
    lst = []
    for i in a:
        lst.append(i)  
        
    encoder = []
    for j in range(len(lst)):
        encoder.append(int((((j+100)**2)*5059)+47))
            

    keys= lst
    values= encoder
    dictionary = dict(zip(keys, values))
   
    empty= []
    for e in s:
        empty.append(dictionary.get(e))
    str1 =  int(''.join(map(str, empty)))
    return str1%8114217931

def myhash2(s):
    
    a = string.printable
    lst = []
    for i in a:
        lst.append(i)  
        
    encoder = []
    for j in range(len(lst)):
        encoder.append(int(10 + ((j+100)**(3/2))*67))
            

    keys= lst
    values= encoder
    dictionary = dict(zip(keys, values))
   
    empty= []
    for e in s:
        empty.append(dictionary.get(e))
    str1 =  int(''.join(map(str, empty)))
    return str1%7076121391

    

        


#Hashing passwords. 
    
#Running time note: I believe the hashing of the passwords should not be included in the bloom
#filter function since most passwords are stored in their hash equivalent and also hashing the whole database 1 time over actually takes a very long time.
    #The running time of my hash functions is between 0.0006 and 0.0008 per string. Total strings to hash are more than 100 million, with 2 hashes this takes about
    #6 to 8 hours. Hence the actual bloom filter will be used on the list of already hashed passwords.

#Hashing existing passwords.
hash1p1 = [myhash1(str(pass1[i])) for i in range(len(pass1))]
hash2p1 = [myhash2(str(pass1[i])) for i in range(len(pass1))]

#Hashing all the possible new passwords.
hash1p2 = [myhash1(str(pass2[i])) for i in range(len(pass2))]
hash2p2 = [myhash2(str(pass2[i])) for i in range(len(pass2))]



#Creating the bloom filter which is initially a list of all 0s.Length based on range of all possible hashes, determined by prime used in modding the hashes string.
def BloomFilter(pass1,pass2):
    start = time.time()
    bf0 = [0]*8114217931

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
            yesno.append(1)
        else:
            yesno.append(0)
    end = time.time()
    
#To calculate the probability of false positives i reference this source: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=903775
  #and use Bloom's classical formulae for the false positive rate.

    m = 8114217931#Length of bloom filter
    k = 2 #Number of hash functions used
    n = 100000000 #objects mapped in bloom filter(passwords1)
    p = (1-((1-1/m)**(k*n)))**k
  
    print('Number of hash function used: ', 2)
    print('Number of duplicates detected: ', sum(yesno))
    
    print('Probability of false positives: ', p)
    print('Execution time: ', end-start)

    


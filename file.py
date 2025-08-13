
a=1
if a>0:
        print("hello")
elif a==0:
        print("hello  0")

else:
        print("hello else")


b=4

if b%2==0:
    print("Even")
else:
    print("odd")
    
    
arr= ["a","b","c","d"]
 
for ar in arr:
    if ar=="b":
         print("aa "+ ar)
    else:
         print(ar)
         
         
def add(a,b):
    return a+b
    
re=add(4,5)
print(add(4,5))

def findword(li,a):

     for l in li:
         if l==a:
            print(l)
            return l
         else:
            print(l)
            
            
            
li=["a",1,"c","d"]          
print( findword(li,"d"))

print(round(9/2,0)==4)
import math

def findprime(pri):

     half= math.floor(pri/2)
     for i in range(2,half):
          if pri%i==0:
               return " not prime number"
               
     return "prime"

print(findprime(11))

def freq(arr):

  fre ={}

  for i in arr:
      fre[i]=fre.get(i,0)+1
  
  
  return {v:k for k, v in fre.items()}
  
print(freq(['apple', 'banana', 'apple', 'cherry']))
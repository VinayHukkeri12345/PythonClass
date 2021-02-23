#1

class Jumper:
    def __init__(self,word):
        self.word=word
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
            if self.index==len(self.word) or self.index==len(self.word):
                raise StopIteration
            if self.index%2==0:
                letter=self.word[self.index]
                self.index+=2
                return letter

jumper=Jumper("python")
it=iter(jumper)

print(next(it))
print(next(it))
print(next(it))

#2

import csv

with open("employee.csv",'w') as employee_file:
    f=csv.writer(employee_file,delimiter=",")
    f.writerow(["Abc",8])
    f.writerow(["Xyz",4])
    f.writerows(["pqr",2],["lmn",1])

#3

import os
import re
result=[]
for root,d_names,f_names in os.walk(".\Test"):
    #print(f_names)
    for fname in f_names:
        #print(fname)
        if re.findall("\w+.py",fname):
            result.append(fname)

print(result)

#4

import sys

for line in sys.stdin:
    if line.rstrip()=='q':
        break
    else:
        print(line)

print("Exit")

#5

from random import randint
class OutOfTries(Exception):
    def __init__(self,strin):
        print("Out of Specified Tries ",strin)


no_of_tries=4

count=0
while count <5:
    
    
    if count >=4:
        raise OutOfTries("5")
    

    num=randint(1,11)
    if num == 7:
        print(f"Correct guess :{num}")
    else:
        print(f"Incorrect guess :{num}")
    count+=1  

#6

try:
    inp=input("Enter value : ")
       
    print("Entered Number : "+int(inp))
except TypeError as te:
    print("TypeError : ",te)

except ValueError as ve:
    print("ValueError : ",ve)

#7

given_dict={"name":"vinay","email":"abc@gmail.com","mob no":"8888888888"}
given_list=[1,2,3,4,5,6]

try:
    given_dict["age"]
except KeyError as ke:
    print("KeyError : ",ke)


try:
    given_list[7]
except IndexError as ie:
    print("IndexError : ",ie)

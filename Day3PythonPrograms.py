
#1
dictcomp={num:num**2 for num in [1,2,3]}
print(dictcomp)


for key in [key for key in dictcomp]:
    print(dictcomp[key])

#2

print({num**2 for num in [1, 2, 5, 2, 3, 1, 4, 5]})

#3


given_list=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

ans={name:c for (name,c,m) in given_list if c>=m}
print(f"dict of those with proper balances (above or equal min bal) : {ans}")

ans={c for n,c,m in given_list}
print(f"set of all balances : {ans}")

ans=[n for n,c,m in given_list]
print(f"list of account holders : {ans}")

ans={n:m-c for n,c,m in given_list if c<m}
print(f"dict of user and money each need to fulfill the min balance requirement :{ans}")

ans=[(n,c) for n,c,m in given_list if c>0]
print(f"list of tuples with name and current balance if the balance is above 0  : {ans}")

#4


class Developer:

    def __init__(self,languages):
        self.languages=languages

    def code(self,language):
        if language in self.languages:
            print("code in "+language)
        else :
            print(f"{language} is not available")

    def resume(self):
        print(f"Available Languages :{self.languages}")


#develop=Developer(["python","Java","C++"])
#develop.code("python")

#develop.resume()


class SrDeveloper(Developer):

    def __init__(self,languages):
        Developer.__init__(self,languages)
    
    def review(self):
        print(self.languages)


#sr=SrDeveloper(["python","Java","C"])
#sr.review()


class TechLead(SrDeveloper):
    def __init__(self,languages):
        SrDeveloper.__init__(self,languages)


techLead=TechLead(["python","Java","C++"])
techLead.review()
techLead.code("C")
techLead.code("python")
techLead.resume()

#5

class Factorials:
    def __init__(self,numbers):
        self.numbers=numbers

    def compute(self):
        result=[]
        for num in self.numbers:
            mul=1
            for n in range(1,num+1):
                mul*=n
            result.append(mul)   
        return result

fact=Factorials([1,2,3,4,5,6])
print(f"Factorials are :{fact.compute()}")

#6

import module

module.print_message()

#modelu.py

def print_message():
    print("Inside print_message function...")

#7

from module import print_message as display

display()

#module.py

def print_message():
    print("Inside print_message function...")

#8

import Day3_8

Day3_8.display()

#Day3_8.py
def display():
    print("Inside Display function..")


if __name__=="__main__":
    print("I'm running...")


#9
file_content=open("Day3_1.py",mode='r')
print(file_content.read())

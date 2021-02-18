#1

names = ["john", "jake", "jack", "george", "jenny", "jason","john"]
set_names=set(names)
names=list(set_names)
for name in names:
    if len(name) <5 and 'e' not in name:
        print(name)

#2

word="python"
result='c'+word[1:len(word)]
print(result)

#3

given_dict={"name": "python", "ext": "py", "creator": "guido"}
for key in given_dict:
    print((key,given_dict[key]))

#4

for num in range(1,101):
    if num%5==0 and num%3==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    

#5

guess=int(input("Enter any number :"))

hardcoded_number=55

if guess < 55:
    print("Less than hardcoded number")
else:
    print("Greater than hardcoded number")
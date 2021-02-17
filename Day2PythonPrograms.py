#1.

for num in range(3):
    guess=int(input("Enter any number :"))

    hardcoded_number=55

    if guess < 55:
        print("Less than hardcoded number.")
    elif guess > 55:
        print("Greater than hardcoded number.")
    else:
        print("correctly guessed.")

#2.

given_list=['a','b','c','d','e']

for index,letter in enumerate(given_list):
    print(f"{index}, {letter}")

#3.

given_dict={"name":"shubham","age":"22","hobbies":"soccer"}

for key,value in given_dict.items():
    print(f"{value} belongs to {key}")

#4.

for num in range(5):
    print(num)
else:
    print("After complete execution of for loop")


#####

print("\n")

for num in range(5):
    print(num)
    if num==2:
        break
else:
    print("After complete execution of for loop")

#5.

def func_sum(a,b=3):
    '''
     This function returns sum of a and b
    '''
    str("Type of a is +"print(type(a)))
    return a+b

print(func_sum(2))

#6.

def func_print(*args):
    for letter in args:
        print(letter)


func_print('a','b','c','d')
    
#7.

def func_print(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} , {value}")

func_print(name="sachin",email="xyz@gmail.com",contact=8888888888)

#8.

def func_count(*args,**kwargs):
     print(f'There are {len(args)} Arg elements and {len(kwargs)} Kwarg elements')


func_count('a','b','c',name="yash",age=24,ht=5.9)

#9.

print([num**2 for num in [1,3,3,4,5,6] if num%2==1])

#10.

avg=lambda total,count:total/count

print(f"{avg(20,6):.2f}")

#11.

given_list={'abc':'v1','xyzw':'v2','pqrst':'v3','pqr':'v4','lmnop':'v5'}

print([word for word in given_list if len(word)>4])



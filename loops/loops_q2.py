#get input from the user 
num = int(input("what is your number:"))

#assign a variable to store the results
results = ""

if num < 2:
     print("Your number should be greater than 2.")
else:
    for i in range (1, num + 1):
        if i % 2 != 0:
            prime = str(i) + " "
            results += prime
    print(f" The prime numbers in the range {num} are {results} ")

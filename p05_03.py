Tinas = ["My Air", "My Puppy", "My Princess", "My Sunflower"]
for Tina in Tinas :
    print("I love", Tina)
print("Do you love me?")

#finding largest value
largest_so_far = -1
print("before", largest_so_far)
for the_num in [1, 10, 3, 4, 5, 20] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("after", largest_so_far)

#counting in a loop
count = 0
print("Before", count)
for numbers in [6, 5, 4, 3, 2, 1] :
    count = count + 1
    print(count, numbers)
print("after", count)

#searching using a boolean variable
found = False
print("Before", found)
for value in [1, 2, 3, 4, 5, 6] :
    if value == 3 :
        found = True
        print (found, value)
        break
print ("after", found)

#exercise 5.1
num = 0
tot = 0.0
while True :
    sval = input ("Enter a number: ")
    if sval == "done" :
        break
    try :
        fval = float(sval)
    except
        print("Invalid Input")
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval

# print("All Done!")
print("All Done!)
print(tot,num,tot/num)


num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = int(num)
    except :
        print('Invalid input')
    if smallest is None :
        smallest = numb
    elif numb < smallest :
        smallest = numb
    elif numb > largest :
        largest = numb
print("Maximum is", largest)
print("Minimum is", smallest)

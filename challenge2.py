# def solution(n, b):
#     #Your code here
#     for i in b:
#         print(n[i])

# def get_digit(number, n):
#     number = 10**number % 10
#     return 10**n % 10
    
#     print("here")


def get_digit(number, n):
    return number // 10**n % 10

def get_no_digits(number):
    return len(str(number))

def get_reverse(number):
    val = ""
    for i in range(len(str(number))):
    #print(n)
        z = get_digit(number, i)
        val = val + str(z)
    #print(val)
    return val

def get_diff(x, y):
    return x-y

def convert_decimal_to_base(number, base):
    remainders = []
    while number > 0:
        remainders.append(str(number % base))
        #print("number 1 = ", number)
        number = number // base
        #print("number 2 = ", number)
    remainders.reverse()
    return ''.join(remainders)

def convert_base_to_decimal(number, base):
    return int(number, base)

def sort_digits_in_descending_order(number):

    number = str(number)
    number = ''.join(sorted(number, reverse=True))
    return number

def solution(n, b):
    visited_solutions = []

    k = get_no_digits(n)
    
    #one stopping condition is that the number of digits is 1
    # while get_no_digits(n) != 1:
    visited_solutions.append(n)
    for i in range(10):
        #step 1: rearrange in descending order 
        x = sort_digits_in_descending_order(n)
        y = get_reverse(int(x))

        temp = convert_base_to_decimal(str(x), b) - convert_base_to_decimal(str(y), b)
        z = convert_decimal_to_base(temp, b)

        if(get_no_digits(z) != k):
            z = format(z.zfill(4))

        n = z
        
        cycle_val = 0
        #print(visited_solutions)
        for val in visited_solutions:
            # print ('val = ', val)
            # print('n = ', n)
            if(val == str(n)):
                # print("here")
                cycle_val = 1
                break           

        if(cycle_val == 1):
            #find the length of the enging cycle 
            #print(val)
            # print("here 2")
            break
        elif(int(val) == 0 or int(val) == 1 or int(val) == 2  or int(val) == 3  or int(val) == 4  or int(val) == 5  or int(val) == 6 or int(val) == 7 or int(val) == 8 or int(val) == 9):
            break

        else:
            visited_solutions.append(n)
           
        
        # print("the x value = ", str(x))
        # print("the y value = ", str(y))
        # #print(str(temp))
        # print("the z value = ", str(z))
        # print("\n")

        #visited_solutions.append(n)
        #print(str(k))

    # print("the final n value = ", n)

    temp = get_reverse(int(n))
   
    val = ""

    prev = 10
    count = 0
    ret_val = 0
    for digit in [int(i) for i in temp] :
        # prev = digit
        if (count == 0):
            prev = digit 
            ret_val = 1
            count = count + 1
            continue 
        else:
            if(prev == digit):
                ret_val = ret_val + 1
            else:
                break

    #print("ret_val", ret_val)
    return ret_val
        # print(i)
            
        # last_digit = int(last_digit_str)

        # val = val + str(last_digit)
    
    
    # return get_no_digits(n)
    



#solution(210022, 3)


# print (convert_decimal_to_base(484, 3))    # 11111111

# print(convert_base_to_decimal('20', 3))

# print(sort_digits_in_descending_order(638473))

# x = [1, 2, 3, 4]
# print(x.reverse())
#print (convert_base(25, 8))     # 31
#base(100, 3)
#do subtraction in that base - write a funcion
#1. do it manually
#2. implement code


# x = get_digit(987654321, 0)
# print(x)
# print("no of bits =", len(str(987654321)))
#print("get reverse =", get_reverse(987654321))

# 1



# y= get_digit(987654321, 5)
#print(y)
# 6

#TODO: not understanding what the return value is supposed to be
#TODO: do one of these problems manually
#def solution(n, b):
    #Stopping condition 1: until, n, x and y values are the same as in the previous itteration, then return the length 
    #Stopping condition 2: if algorithm reaches a constant - with length = 1, then return 1


    #get x
    #get y


#solution(1211, 4)
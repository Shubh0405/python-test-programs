######## program1

a = "My name445"
if "4" in a:
    print("String contains 4")
else:
    print("String does not contains 4")

####### program 2

array = [-1,2,-3,4,-5,6]
array.sort()
array.reverse()
print(array)


###### program 3

a = "abcab"

def check_string(a):

    curr = a[0]
    count = 1
    res = ""

    for i in range(1,len(a)):
        if a[i] == curr and count == 2:
            return "Invalid Input"
        elif a[i] == curr and count == 1:
            count += 1
        else:
            res += curr
            count = 1
            curr = a[i]

    return res + a[-1]

print(check_string(a))

######## program 4

def get_frequency(a):
    res_dic = {}

    for i in a.lower():
        if i in res_dic:
            res_dic[i] += 1
        elif i not in res_dic and i != " ":
            res_dic[i] = 1

    new_list = sorted(res_dic.items(), key = lambda x : (x[1], x[0]))

    new_dic = {}
    for i in new_list:
        new_dic[i[0]] = i[1]
    return new_dic

print(get_frequency("my name is SDET D M"))




    
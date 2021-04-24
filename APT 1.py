
def digitsum(input):
    s=0
    for i in input:
        string_to_int = int(i)
        s = s + string_to_int
    return s

user_no = input("enter the nummer")
my_nummer = "00814334"
user_sum = digitsum(user_no)
my_sum = digitsum(my_nummer)
print("user sum is :" +str(user_sum))
print("my sum is :" +str(my_sum))




def two_to_ten(strng):
    number = 0
    counter = 0
    for i in strng[::-1]:
        number += int(i)*(2**counter)
        counter += 1
    return number  
print(two_to_ten("100101"))
print(two_to_ten("1101"))
print(two_to_ten("10010111"))
def ten_to_two(num):
    strng = ""
    while num // 2 != 0:
        strng += str(num%2)
        num = num//2
    if num == 1:
        strng += "1"
    return strng[::-1]
print(ten_to_two(37))
print(ten_to_two(13))
print(ten_to_two(151))

print("**************** Several Triangle with Asterisk **************")
print("**************** Pyramid **************")


# # **************************** 1 *******************************

# n = int(input("Enter a integer number: "))
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*", end="")
#     print("\r")

# **************************** 2 *******************************

# n = 4
# k = 2 * n - 2
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print("\r")

# **************************** 3 *******************************



# **************************** 1 *******************************

# **************************** 1 *******************************

# **************************** 1 *******************************

# **************************** 1 *******************************

#
# p = 5
# for i in range(0, p):
#     for j in range(0, i+1):
#         print(end="*")
#     print(end="\n")
# print("\n")


#here you have an upside down version of an recursive function.
#
# def upside_down_asterix_triangle(i, t=0):
#     if i == 0:
#         return 0
#     else:
#         print('' * ( t + 1 ) + '*' * i)
#         return upside_down_asterix_triangle( i - 1, t + 1 )
#
# upside_down_asterix_triangle(13)


# # ********************
# print('Please input your number:')
# number = int(input())
# temp = number
#
# while number > 1:
#     number -= 1
#     temp = temp*number
#
# if temp == 0:
#     print(1)
# else:
#     print(temp)







# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
# def triangle(n):
#     # number of spaces
#     k = 2 * n - 2
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#
#             # decrementing k after each loop
#         k = k - 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ", end="")
#
#             # ending line after each row
#         print("\r")
#
#     # Driver Code
#
#
# n = 5
# triangle(n)




# Function to demonstrate printing pattern of numbers
# def numpat(n):
#     # initialising starting number
#     num = 1
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # re assigning num
#         num = 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing number
#             print(num, end=" ")
#
#             # incrementing number at each column
#             num = num + 1
#
#         # ending line after each row
#         print("\r")
#
#     # Driver code
#
#
# n = 5
# numpat(n)

#
# def contnum(n):
#     # initializing starting number
#     num = 1
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # not re assigning num
#         # num = 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing number
#             print(num, end=" ")
#
#             # incrementing number at each column
#             num = num + 1
#
#         # ending line after each row
#         print("\r")
#
#
# n = 5
#
# # sending 5 as argument
# # calling Function
# contnum(n)


# def alphapat(n):
#     # initializing value corresponding to 'A'
#     # ASCII value
#     num = 65
#
#     # outer loop to handle number of rows
#     # 5 in this case
#     for i in range(0, n):
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # explicitely converting to char
#             ch = chr(num)
#
#             # printing char value
#             print(ch, end=" ")
#
#             # incrementing number
#         num = num + 1
#
#         # ending line after each row
#         print("\r")
#
#     # Driver Code
#
#
# n = 5
# alphapat(n)


# def contalpha(n):
#     # initializing value corresponding to 'A'
#     # ASCII value
#     num = 65
#
#     # outer loop to handle number of rows
#
#
#     for i in range(0, n):
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # explicitely converting to char
#             ch = chr(num)
#
#             # printing char value
#             print(ch, end=" ")
#
#             # incrementing at each column
#             num = num + 1
#
#         # ending line after each row
#         print("\r")
#
# # Driver code
# n = 5
# contalpha(n)

#
# import xlwt
#
# workbook = xlwt.Workbook()
#
# sheet = workbook.add_sheet("Sheet Name")
#
# # Applying multiple styles
# style = xlwt.easyxf('font: bold 1, color red;')
#
# # Writting on specified sheet
# sheet.write(0, 0, 'SAMPLE', style)
#
# workbook.save("sample.xls")


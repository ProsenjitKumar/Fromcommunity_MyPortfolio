
# ********************************** practice *******************************
print("\n*************************Practice*********************************\n")


n = 4
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")


# # 11111111
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)
# # 1111111111111
# print(list(map(lambda x: x**2, range(10))))
# # 1111111111111111
# print( [x**2 for x in range(10)])
# print(([lambda x]))

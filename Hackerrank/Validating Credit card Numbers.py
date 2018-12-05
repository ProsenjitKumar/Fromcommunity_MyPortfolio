# import re
# TESTER = re.compile(
#     r"^"
#     r"(?!.*(\d)(-?\1){3})"
#     r"[456]"
#     r"\d{3}"
#     r"(?:-?\d{4}){3}"
#     r"$")
# for _ in range(int(input().strip())):
#     print("Valid" if TESTER.search(input().strip()) else "Invalid")


import re

n = int(input())
for i in range(n):
    s = input()
    if len(s) == 19:
        if s[0] in ("4", "5", "6"):
            if bool(re.match("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", s)):
                lst = []
                for z in range(len(s)):
                    if s[z] != "-":
                        lst.append(s[z])
                bool_4 = 1
                for t in range(3, len(lst)):
                    if lst[t] == lst[t - 1] and lst[t] == lst[t - 2] and lst[t] == lst[t - 3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")

    elif len(s) == 16:
        if s[0] in ("4", "5", "6"):
            if bool(re.match("[0-9]*$", s)):
                lst = []
                for k in range(len(lst)):
                    lst.append(s[k])
                bool_4 = 1
                for t in range(3, len(lst)):
                    if lst[t] == lst[t - 1] and lst[t] == lst[t - 2] and lst[t] == lst[t - 3]:
                        bool_4 = 0
                if bool_4 == 1:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")



    else:
        print("Invalid")
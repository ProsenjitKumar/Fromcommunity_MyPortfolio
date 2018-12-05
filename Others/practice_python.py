class Triangle:
    def choose(self, choice):
        if choice == 1:
            return self.asterisk()
        elif choice == 2:
            return self.number()
        else:
            print("\nWrong Pressed, Try again\n")
            return self.choose(int(input("Press 1 for Asterisk Triangle and\n"
                              "2 for Number Triangle: ")))

    def asterisk(self):
        n = int(input("Enter a integer number: "))
        k = 2 * n - 2
        for i in range(0, n):
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i + 1):
                print("*", end=" ")
            print("\r")
        return self.choose(int(input("Press 1 for Asterisk Triangle and\n"
                              "2 for Number Triangle: ")))

    def number(self):
        def same_row_and_serialize_column_number(n):
            num = 1
            for i in range(0, n):
                num = 1
                for j in range(0, i + 1):
                    print(num, end=" ")
                    num = num + 1
                print("\r")

        same_row_and_serialize_column_number(int(input("Enter a Integer Number: ")))
        self.choose(int(input("Press 1 for Asterisk Triangle and\n"
                              "2 for Number Triangle: ")))


triangle_obj = Triangle()
triangle_obj.choose(int(input("Press 1 for Asterisk Triangle and\n"
                              "2 for Number Triangle: ")))
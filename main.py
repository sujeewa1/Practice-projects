# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Sam's name")
print('Sam\'s "name"')
print(r'my name/name')
print(10*" name")


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        M1 = self.m1 + other.m1
        M2 = self.m2 + other.m2
        S3 = student(M1, M2)
        return S3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = student(54, 58)
s2 = student(54, 25)

s3 = s1 + s2

print(s3.m1)

if s1 > s2:
    print("S1 wins")

else:
    print("S2 wins")
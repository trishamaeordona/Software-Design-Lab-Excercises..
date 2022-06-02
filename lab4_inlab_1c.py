def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end='')

string = "strawberry"
print(string)
reverse(string)

string1 = "vanilla"
print("\n"+string1)
reverse(string1)
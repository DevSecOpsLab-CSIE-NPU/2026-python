print("請輸入一行數列並用空格分隔:")

array = list(map(int, input().split()))

def dedupe(array):
    return list(dict.fromkeys(array))

def asc(array):
    return sorted(array)

def desc(array):
    return sorted(array, reverse=True)

def evens(array):
    return [i for i in array if i % 2 == 0]

def output(text, array):
    print(text)
    for i in array:
        print(i, end=" ")
    print()



output("dedupe:", dedupe(array))
output("asc:", asc(array))
output("desc:", desc(array))
output("evens:", evens(array))
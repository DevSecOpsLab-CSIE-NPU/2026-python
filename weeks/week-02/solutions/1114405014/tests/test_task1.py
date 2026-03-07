print ("請輸入一行數列並用空格分隔:")
Array = input().split(" ")
for i in range(len(Array)):
    Array[i] = int(Array[i])

def dedupe(array):
    result = []
    for i in array:
        if i not in result: #如果i不在result裡面就把i加入result
            result.append(i)
    return result

def asc(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]: #如果array[i]比array[j]大就交換位置
                array[i], array[j] = array[j], array[i]
    return array

def desc(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]: #如果array[i]比array[j]小就交換位置
                array[i], array[j] = array[j], array[i]
    return array

def evens(array):
    result = []
    for i in array:
        if i % 2 == 0: #如果i是偶數就把i加入result
            result.append(i)
    return result

def output(text,array):
    print(text)
    for i in array:
        print(i, end=" ") #用空格分隔輸出
    print() #換行


output("dedupe:", dedupe(Array))
output("asc:", asc(Array))
output("desc:", desc(Array))
output("evens:", evens(Array))
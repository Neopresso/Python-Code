#main function for bubble sorting
def bubble_sorter(arr):
    listLength= len(arr)
    tempNum=0
    #loop for first number
    for n1 in range(listLength):
        #print('n1={}'.format(arr[n1]))
        #loop for second number
        for n2 in range(0, listLength-n1-1):
            #print('n2={}'.format(arr[n2]))
            #checks whether first number is greater than second
            if arr[n2]>arr[n2+1]:
                #swaps the numbers if the first number is greater than the second
                tempNum=arr[n2+1]
                arr[n2+1]=arr[n2]
                arr[n2]=tempNum


#List of integers to be sorted
arr = [64, 34, 111, 95, 22, 11, 90]
bubble_sorter(arr)

print(arr)

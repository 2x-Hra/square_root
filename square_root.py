



def dou_maker(arr):
    counter = 0
    result_arr = []
    dou = []
    while (counter < len(arr)):
        val = arr[counter]
        dou.append(val)
        dou.append(counter)
        result_arr.append(dou)
        counter += 1
    return result_arr


def cycle_finder(arr):
    result_arr =[]
    cycle_arr = []
    counter = 0

    while ( counter < len(arr)):


dataFile = open("data.in","r")
data_lines = dataFile.readlines()
sample_numbers = int(data_lines[0])

counter = 1
one_elements_arr =[]
while(counter < len(data_lines)):
    
    counter += 1
    elements = data_lines[counter]
    one_elements_arr.append(elements)
    counter += 1
    
print(one_elements_arr)
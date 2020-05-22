



def dou_maker(arr):
    counter = 0
    result_arr = []
    dou = []
    while (counter < len(arr)):
        dou = []
        val = arr[counter]
        dou.append(val)
        dou.append(counter)
        result_arr.append(dou)
        counter += 1
    return result_arr

def dou_deleter(num,arr):
    
    counter = 0
    while ( counter < len(arr)):
        if(arr[counter][0] == num):
            arr.pop(counter)
        counter += 1

    return arr
def dou_finder(num,arr):
    counter =0

    while ( counter < len(arr)):
        if(arr[counter][0]== num):
            return counter
        counter += 1


def cycle_finder(dou_arr):

    cycle_arr = []


            


                




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
    
# print(one_elements_arr)

print(dou_maker([2,3,0,1])) # test Dou_maker
print(dou_deleter(2,dou_maker([2,3,0,1])))

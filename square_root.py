



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
    val = dou_arr[0][0]
    cycle_arr.append(val)
    index = 0

    if(dou_arr[index][0] == dou_arr[index][1]):
        return cycle_arr
    else:
       
        cycle_arr.append(dou_arr[index][1])
        while(True):
        
            index = dou_finder(dou_arr[index][1], dou_arr)
           
            if(dou_arr[index][1] in cycle_arr):
                break
            cycle_arr.append(dou_arr[index][1])
            
    return cycle_arr
            
def all_cycles(dou_arr):
    print("in")
    cycles = []
    while( len(dou_arr) != 0):
        each_cycle = cycle_finder(dou_arr)
        cycles.append(each_cycle)
        
        for i in each_cycle:
            
            dou_deleter(i,dou_arr)

    return cycles        



dataFile = open("data.in","r")
data_lines = dataFile.readlines()
sample_numbers = int(data_lines[0])
i = 0
n_list = list()
while i<sample_numbers:
    index = (2*(i+1))-1
    n = int(data_lines[index])
    m_list = list()
    counter = 0
    line = data_lines[index+1].split()
    while counter<n:
        m_list.append(int(line[counter]))
        counter+=1
    n_list.append(m_list)
    i+=1
    
# print(n_list)

# print(dou_maker([2,0,3,1])) # test Dou_maker
# print(cycle_finder(dou_maker([2,3,0,1])))



print (all_cycles(dou_maker(n_list[99])))


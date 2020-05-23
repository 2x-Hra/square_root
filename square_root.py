



def dou_maker(arr):
    '''
        
        in fact this function will place each element next to its index
        for example it will change [2,3,0,1] to [[2,0],[3,1],[0,2],[1,3]]
    '''
    counter = 0
    result_arr = []
    dou = []
    while (counter < len(arr)):
        dou = []
        val = arr[counter]
        dou.append(counter)
        dou.append(val)
        
        result_arr.append(dou)
        counter += 1
    return result_arr

def dou_deleter(num,arr):

    '''
        it will erase the element that its first index is num
        for example the num is 2 and the arr is [[2,0],[3,1],[0,2],[1,3]] it will change it to [[3,1],[0,2],[1,3]]
    '''
    
    counter = 0
    while ( counter < len(arr)):
        if(arr[counter][0] == num):
            arr.pop(counter)
        counter += 1

    return arr

def dou_finder(num,arr):
    '''
        this function will find the elemet that its first index is num
        for example: Num = 2 and Arr= [[2,0],[3,1],[0,2],[1,3]]
        then result is : 0 
    '''
    counter =0

    while ( counter < len(arr)):
        if(arr[counter][0]== num):
            return counter
        counter += 1


def cycle_finder(dou_arr):
    '''
    this function will find a cycle depends on the first element of the array
    '''
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
    '''
        this function will find all the cycles
    '''
    
    cycles = []
    while( len(dou_arr) != 0):
        each_cycle = cycle_finder(dou_arr)
        cycles.append(each_cycle)
        
        for i in each_cycle:
            
            dou_deleter(i,dou_arr)

    return cycles        

def impossible_finder(arr):
    '''
        this function will find those sample that is impossible


    '''
    counter = 0
    cycle_counter = 0

    while ( counter < len(arr)):
        len_el = len(arr[counter])
        cycle_counter = 0
        counter2 =0
        if(len_el % 2 ==0): # agar cycle zowj bood
            while( counter2 < len(arr)):
                if (len_el == len(arr[counter2])):
                    cycle_counter += 1
                counter2 += 1
            if(cycle_counter % 2 != 0):
                return False

        counter += 1

    return True


def odd_roots(odd_cycle):

    

    mid_index = (len(odd_cycle)//2 ) 
    matrix_a = odd_cycle[0:mid_index]
    matrix_b = odd_cycle[mid_index+1:]
    counter = 0
    root =[]
    while ( counter < len(odd_cycle)//2):
        root.append(matrix_a[counter])
        root.append(matrix_b[counter])
        counter += 1
        
    root.append(odd_cycle[mid_index])
    return root


def even_roots(even_cycle1, even_cycle2):

    counter = 0
    root =[]
    while ( counter < len(even_cycle1)):
        root.append(even_cycle1[counter])
        root.append(even_cycle2[counter])
        counter += 1
        
    return root



def rootsFinder(cycle_sample):  

    roots = []   
    while(len(cycle_sample) != 0):
        if(len(cycle_sample[0]) % 2 ==0):
            counter =1
            while ( counter < len(cycle_sample)):

                if(len(cycle_sample[0])== len(cycle_sample[counter])):
                    even_root = even_roots(cycle_sample[0], cycle_sample[counter])
                    cycle_sample.pop(counter)
                    cycle_sample.pop(0)
                    roots.append(even_root)
                counter += 1
        else:
            odd_root = odd_roots(cycle_sample[0])
            cycle_sample.pop(0)
            roots.append(odd_root)
    return roots
# print(rootsFinder([[1,2,0]]))
def squareRootExe(sample_orig):
    '''
        for example sample_orig = [2,3,0,1]
    '''
    sample_cycles = all_cycles(dou_maker(sample_orig))
    cycles_roots = rootsFinder(sample_cycles)
    answer = []
    counter = 0
    while(counter < len(sample_orig)): #initialing with 0
        answer.append(0)
        counter += 1 
    
    counter = 0
    while(counter < len(cycles_roots)):

        counter1 = 0
        while(counter1 < len(cycles_roots[counter])):
            if(counter1 == len(cycles_roots[counter]) -1 ): # [[1,2,0]]
                val = cycles_roots[counter][counter1]
                answer[cycles_roots[counter][0]] = sample_orig[val]
            else:
                val = cycles_roots[counter][counter1]
                answer[cycles_roots[counter][counter1+1]] = sample_orig[val]
            counter1 += 1
        counter += 1

    return answer


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
    
counter3 = 0
samples_cycle = []

while(counter3 < len(n_list)):
    samples_cycle.append(all_cycles(dou_maker(n_list[counter3])))
    counter3 +=1

counter3 =0
while(counter3 < len(samples_cycle)):

    if(counter3 == 13):
        break
    if( not impossible_finder(samples_cycle[counter3]) ):
        print ("sHomare " + str(counter3+1) + ", ans : " + "Impossible")
    
    else:
        ans = squareRootExe(n_list[counter3])
        print("shomare " + str(counter3 + 1 ) + ", ans :" +str(ans))
    counter3 +=1
    print("\n")







# print (all_cycles(dou_maker(n_list[99])))


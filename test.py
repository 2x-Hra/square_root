def hossein(arr):
    cycles = list()
    n = len(arr)
    while n!=0:
        cycle = list()
        x = arr[0][0]
        y = arr[0][1]
        cycle.append(x)
        if x==y and n==1:
            cycles.append(cycle)
            break
        while x!=y:
            cycle.append(y)
            arr.remove([x,y])
            n = len(arr)
            i = 0
            while i<n:
                if y==arr[i][0]:
                    if x==arr[i][1]:
                        x = arr[i][0]
                        cycles.append(cycle)
                        arr.remove([arr[i][0],arr[i][1]])
                        n = len(arr)
                        break
                    else:
                        y = arr[i][1]
                        cycle.append(arr[i][1])
                        arr.remove([arr[i][0],arr[i][1]])
                        n = len(arr)
                        i = 0
                else:
                    i+=1
    return cycles



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

samples = list()
for i in one_elements_arr:
    samples.append(dou_maker(i))

cycles = list()
for i in samples:
    cycles.append(hossein(i))

counter = 1
for sample in cycles:
    if not hasSqr(sample):
        print("Sample " + str(counter) + " impossible")
    counter+=1


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


def cycle_finder(arr):

    
print(one_elements_arr)
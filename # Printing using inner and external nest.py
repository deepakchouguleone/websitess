# Printing using inner and external nested loops
list1 = ['I am ', 'You are']
list2 = ['Healthy', 'fine', 'geek']

list2_size = len(list2)

for item in list1:
    print('Start outer loop')
    i = 0 
    while(i < list2_size):
        print(item + list2[i])
        i += 1
    print('End outer loop')
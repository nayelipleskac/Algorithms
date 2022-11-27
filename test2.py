import timeit
# def pascal(layer): 
#     if len(layer) > 15:  #base cases
#         return
#     else: 
#         for i in layer:
#             print(i, end = ' ')
#         print()
#         new_layer = []
#         for i in range(len(layer)-1):
#             num1= layer[i]
#             num2 = layer[i+1]
#             new_layer.append(num1 + num2)

#         new_layer = [1] + new_layer + [1] 
#         layer = new_layer
#         pascal(layer)                                                                       
        
# print(1)
# layer = [1,1]
# # pascal(layer)
# t= timeit.timeit(stmt=lambda: pascal(layer), number = 1)
# t = round(t,8)
# print('time of pascal (recursive) : {:.8f} sec\n'.format(t))

def pascal():
    print(1)
    layer = [1, 1]
    layers = 1
    while layers < 15:
        for elem in layer:
            print(elem,end=' ')
        print()
        new_layer = []
        for i in range(len(layer)-1):
            num1 = layer[i]
            num2 = layer[i+1]
            new_layer.append(num1 + num2)
        new_layer=[1] + new_layer + [1]
        layer=new_layer
        layers+=1

t= timeit.timeit(stmt=lambda: pascal(), number = 1)
t = round(t,8)
print('time of pascal iterative: {:.8f} sec\n'.format(t))
# import numpy
# def arrays(arr):
#     arr=arr[::-1]
#
#     arr=list(map(float,arr))
#     arr=numpy.array(arr)
#     return(arr)



import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
     return numpy.flipud(numpy.array(arr, float))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
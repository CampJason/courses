#def my_revers(string):
 #   i = len(string)-1
  #  res_string = ''
   # while i > 0:
    #    res_string += string[i]
     #   i -= 1
      #  return res_string
#
#text = 'tolia'
#print(my_revers(text))


#def cont(string,char):
 #   for elem in string:
  #      if elem == char:
   #         return True
    #return False

#print(cont(text,'t'))
#from test2 import my_mul

def my_range(*args):
    start = 0
    stop = None
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    i =start
    nums=[]
    while i<stop:
        nums.append(i)
        i += step
    return nums

#print(my_range(0,10))

def my_revers_range(*args):
    start = 1
    stop = None
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = args[2]
    i = start
    nums = []
    while i > stop:
        nums.append(i)
        i -= step
    return nums

#print(my_revers_range(10,1))

#for i in range(10, 1):
#    print(i)


#for i in range(-1,10):
#    print(i)
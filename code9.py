import array 
values = array.array('i',[2,3,4,5,6,])
val = list(values)
val.sort()
values = array.array(values.typecode,(val))
 
print (values[3])

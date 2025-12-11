import numpy as array
sus = array.array([
    [1,2,3],
    [4,5,6]])
sas = sus.flatten()
sas2= sus.reshape(3,2)
print(sus)
print(sas)
print(sas2)
print(f"{sas[2]}")

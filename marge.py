def merge_arrays(arrayA,arrayB,arrayD):
	return  sorted(set(arrayA + arrayB + arrayD))

a = [1,3,5,6,4,6,3,5,3,2,1]
b = [2,3,4,4,1,2,7,8,9,4,5]
d = [0,3,47,2,3,7,81,9,1,2,30]
c = merge_arrays(a,b,d)
print(c)
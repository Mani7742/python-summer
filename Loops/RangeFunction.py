#-----------------------------------< Range Function >-------------------------------------------------
# range() function returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.
# Syntax: range(start, stop, step)
# start: The starting number of the sequence. Default is 0.
# stop: The end number of the sequence. This number is not included.
# step: The incrementation number. Default is 1.
print(range(5))
seq = range(5) #--> range(stop)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

for i in seq:
    print(i)

for j in range(2,5): #--> range(start,stop)
    print(j)

for j in range(1,10,2): #--> range(start,stop,step)--->Step size means k kitna say increase krna hy
    print(j)


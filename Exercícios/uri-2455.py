p1,c1,p2,c2 = map(int,raw_input().split())

x = p1 * c1
y = p2 * c2

if x == y: print 0

elif x < y : print 1

else : print -1

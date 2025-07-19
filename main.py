fru = {"apple","banana", "cherry"}
print(fru)
num = set([1,2,3,2,1])
print(num)
emps = set()
print(emps)
set = {1,2,3}
set.add(4)
print(set)
set.update([5,6,7])
print(set)
set = {1,2,3,4,5}
set.remove(3)
print(set)
A = {1,2,3}
B = {3,4,5}
C = {1,2}
print(f"The union of {A} and  {B} = {A | B}")
print(f"Teh intersection of {A} and {B} = {A & B}")
print(f"The difference between {A} & {B} = {A - B}")
print(f"The difference between {B} & {A} = {B - A}")
print(f" The symetric difference of  {A} and {B} = {A ^ B}")
print(len(A))
print(A.isdisjoint(B))
print(C.issubset(A))
print(A.issuperset(C))
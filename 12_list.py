"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""

N = int(input())
l = []
for x in range(1,N + 1):
    i = input().split(' ')
    if 'insert' in i:
        l.insert(int(i[1]), int(i[2]))
    elif 'print' in i:
        print(l)
    elif 'remove' in i:
        l.remove(int(i[1]))
    elif 'append' in i:
        l.append(int(i[1]))
    elif 'sort' in i:
        l.sort()
    elif 'pop' in i:
        l.pop()
    elif 'reverse' in i:
        l.reverse()

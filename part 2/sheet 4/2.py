vegetables = ['vegetables','mushroom','mashed potatoes']
list1 = input().split(':')
list2 = input().split(':')
result1 = result2 = False
for item in list1:
    if item.strip() in vegetables:
        result1 = True
for item in list2:
    if item.strip() in vegetables:
        result2 = True
if result1 == True and result2 == True:
    print('she loves vegetables')
elif result1 == True or result2 == True:
    print('she would neither hate nor love it.')
else:
    print('she hates vegetables')


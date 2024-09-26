expenses = [2200,2350,2600,2130,2190]

"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""
#1 
extra_money = expenses[1] - expenses[0]  #O(1)
print(f'{extra_money=}')
#2
quater_expenses  = sum([ expenses[i] for i in range(3)]) # O(n)
# print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150

print(f'{quater_expenses=}')
#3
find_exactly_2000 = [price for price in expenses if price == 2000] #O(n)
print(f'{find_exactly_2000=}')
# print("Did I spent 2000$ in any month? ", 2000 in exp) # False

#4
expenses.append(1980) #O(1)
print(f'{expenses=}')
#5
expenses[3] = expenses[3] - 200 # O(1)
print(f'{expenses=}')


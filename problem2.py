#Problem2
import random
import matplotlib.pyplot as plt

#part a)
def truncate (x):
    '''
    truncate the number after the third decimal place
    '''
    return int(x * 1000) / 1000

#part b)
initial_prices = [random.uniform(0, 200) for i in range(1400)]
baseline_sum = sum(initial_prices)

def index1 (n):
    old_index = 1000
    index_list = []
    for _ in range (n):
        price_change = random.uniform(-200 , 200)
        new_index = old_index + price_change * 100/baseline_sum
        index_list.append(new_index)
        old_index = new_index
    return index_list

#evolution over 1 day
one_frq = 2800
num1 = 1 * one_frq
one_day1 = index1(num1)
plt.plot(one_day1)
plt.show()
#evolution over 22month-660days
num2 = 22*30*one_frq
month1 = index1(num2)
plt.plot(month1)
plt.show()

#Part c)
# for one day
total = 0
for a in range(len(one_day1)):
    dif = abs(truncate(one_day1[a])-one_day1[a])
    total += dif
drop_avg = total / num1
print('how many points on average would you drop for one day:', drop_avg)
# for 22 months
for b in range(len(month1)):
    dif = abs(truncate(month1[b])-month1[b])
    total += dif
drop_avg = total / num2
print('how many points on average would you drop for 22 months:', drop_avg)



#part d)
def index2 (m):
    '''
    define a new truncated index function
    '''
    index_list = []
    old_index = 1000
    for _ in range (m):
        price_change = random.uniform(-200 , 200)
        new_index = old_index + price_change * 100/baseline_sum
        truncate_index = int(new_index*1000)/1000
        index_list.append(truncate_index)
        old_index = truncate_index
    return index_list
#truncated evolution over 1 day
one_day2 = index2(num1)
plt.plot(one_day2,'g') #truncated
plt.plot(one_day1,'r') #raw
plt.show()
#truncated evolution over 22month
month2 = index2(num2)
plt.plot(month2,'g') #truncated
plt.plot(month1,'r') #raw
plt.show()
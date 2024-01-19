import matplotlib.pyplot as plt

start_num = 6
nums = []

for i in range(100):
    nums.append(start_num)
    if start_num != 10:
        start_num = (start_num / 2) + 5
    else:
        print(f"Ended in {i} itteration. Last number: {start_num}")
        break
    
plt.plot(nums)
plt.ylabel('aiming_for_ten')
plt.show()
    
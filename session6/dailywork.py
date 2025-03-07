'''
Your day consists of various tasks, each requiring a certain amount of time. 
To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. 
You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, 
write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def find_task_pair(task_times, available_time):
    l,r = 0, len(task_times)-1
    while l < r:
        if task_times[l] + task_times[r] > available_time:
            r -= 1
        elif task_times[l] + task_times[r] < available_time:
            l += 1
        elif task_times[l] + task_times[r] == available_time:
            return True
    return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
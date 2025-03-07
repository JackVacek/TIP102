'''
You work with clients across different time zones and often have gaps between your work sessions. 
You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. 
Your task is to find the smallest gap between any two consecutive work sessions.
Given a list of tuples where each tuple represents a work session with a start and end time 
(both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
def regToMinutes(time):
    hours = time // 100
    minutes = time % 100
    return hours * 60 + minutes

def find_smallest_gap(work_sessions):
    minGap = float('inf')
    for i in range(len(work_sessions)-1):
        minGap = min(minGap,regToMinutes(work_sessions[i+1][0]) - regToMinutes(work_sessions[i][1]))
    return minGap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
#Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:
#answer[i] == "HulkSmash" if i is divisible by 3 and 5.
#answer[i] == "Hulk" if i is divisible by 3.
#answer[i] == "Smash" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.
def hulk_smash(n):
    lst = []
    for i in range(1,n+1):
        if i % 15 == 0:
           lst.append("HulkSmash")
        elif i % 3 == 0:
            lst.append("Hulk")
        elif i % 5 == 0:
            lst.append("Smash")
        else:
            lst.append(str(i))
    print(lst) 

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)

'''
["1", "2", "Hulk"]
["1", "2", "Hulk", "4", "Smash"]
["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
'''
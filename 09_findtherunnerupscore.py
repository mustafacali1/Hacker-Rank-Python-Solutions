"""
Given the participants' scoresheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
"""
n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
score = None

for num in arr:
    if num == mx:
        pass
    elif score == None:
        score = num
    elif num > score:
        score = num

print(score)
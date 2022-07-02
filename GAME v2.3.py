#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import random

def roll():
    return int(random()*60/10)+1

def sum1(n):
    result = []
    for i in range(n):
        result.append(roll())
    return result

def sum2(r):
    sum = 0
    for x in range(0, len(r)):
        if r[x] == 1:
            return 1
        sum = sum + r[x]
    return sum

A_score = 0
B_score = 0

while True:
    A_roll_times = input("Player A's turn：")
    if int(A_roll_times) > 10:
        print('Player A：lose')
        break
    turn_result = sum1(int(A_roll_times))
    A_score = A_score + sum2(turn_result)
    print('result：{}, point：{}'.format(turn_result, sum2(turn_result)))
    print('Player A：{} point(+{})\nPlayer B：{}\n'.format(A_score, sum2(turn_result), B_score))
    if A_score >= 100:
        print('Player A：winner')
        break
    
    B_roll_times = input("Player B's turn：")
    if int(B_roll_times) > 10:
        print('Player B：lose')
        break
    turn_result = sum1(int(B_roll_times))
    B_score = B_score + sum2(turn_result)
    print('result：{}, point：{}'.format(turn_result, sum2(turn_result)))
    print('Player A：{}\nPlayer B：{} point(+{})\n'.format(A_score, B_score, sum2(turn_result)))
    if B_score >= 100:
        print('Player B：winner')
        break


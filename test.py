import time 
import random


def reverse_link(head):
    p = head
    q = head.next 
    p.next = None
    while q:
        r = q.next 
        q.next = p
        p = q
        q = r 

def insert_sort(lis):
    for i in range(1, len(lis), 1):
        tmp = lis[i]
        j = i-1
        while j >= 0 and lis[j] > tmp:
            lis[j+1] = lis[j]
            j  -= 1
        lis[j+1] = tmp

def bubble_sort(lis):
    for i in range(len(lis)-1):
        exchange = False
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

def quick_sort(lis, left, right):
    if left < right:
        mid = partition(lis, left, right)
        quick_sort(lis, left, mid-1)
        quick_sort(lis, mid+1, right)

def partition(lis, left, right):
    tmp = lis[left]
    while left < right:
        while left < right and lis[right] > tmp:
            right -= 1
        lis[left] = lis[right]
        while left < right and lis[left] < tmp:
            left += 1
        lis[right]  = lis[left]
    lis[left] = tmp
    return left

    def bi_search(lis, val):
        low = 0
        high = len(lis)-1
        while low <= high:
            mid = (low+high)//2
            if lis[mid] == val:
                return mid
            elif lis[mid] < val:
                low = mid+1
            else:
                high = mid-1
        return None


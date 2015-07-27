import argparse
import random

def samplesort(lst):
    return sorted(lst)

def quicksort(lst):
    assert(len(lst) >= 0)
    if len(lst) <= 1:
        return lst
    for i in lst:
        if i != lst[0]:
            break
    else:
        return lst

    pivot = random.choice(lst)
    lst1 = []
    lst2 = []
    for i in lst:
        if i < pivot:
            lst1.append(i)
        else:
            lst2.append(i)
    s1 = quicksort(lst1)
    s2 = quicksort(lst2)

    ans = []
    while s1 != [] and s2 != []:
        if s1[0] < s2[0]:
            ans.append(s1[0])
            s1.pop(0)
        else:
            ans.append(s2[0])
            s2.pop(0)
    if s1 == []:
        ans.extend(s2)
    else:
        ans.extend(s1)
    return ans

def mergesort(lst):
    assert(len(lst) >= 0)
    if len(lst) <= 1:
        return lst
    for i in lst:
        if i != lst[0]:
            break
    else:
        return lst

    pivot = random.choice(lst)
    lst1 = [i for i in lst[:len(lst)/2]]
    lst2 = [i for i in lst[len(lst)/2:]]

    s1 = mergesort(lst1)
    s2 = mergesort(lst2)

    ans = []
    while s1 != [] and s2 != []:
        if s1[0] < s2[0]:
            ans.append(s1[0])
            s1.pop(0)
        else:
            ans.append(s2[0])
            s2.pop(0)
    if s1 == []:
        ans.extend(s2)
    else:
        ans.extend(s1)
    return ans

def bubblesort(lst):
    done = False
    while not done:
        done = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
    return lst

def insertionsort(lst):
    for i in [x+1 for x in range(len(lst) - 1)]:
        if lst[i] > lst[i-1]:
            continue
        k = 0
        while lst[i] <= lst[i-k]:
            k += 1
            if i-k == -1:
                break
        lst.insert(i-k+1, lst.pop(i))
    return lst

def selectionsort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(len(lst[i:])):
            if lst[j+i] < lst[minimum]:
                minimum = j+i
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst

def start():
    """ This function handles argument parsing """
    parser = argparse.ArgumentParser()
    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument('--list', nargs='+')
    group_input.add_argument('--file', nargs=1)

    # group_sort = parser.add_mutually_exclusive_group()
    # group_sort.add_argument('-q', type=str)

    args = parser.parse_args()

    lst = []
    if args.file:
        f = open(args.file[0], 'r')
        for line in f:
            lst.append(int(line))
    else:
        lst = [int(i) for i in args.list]

    ans = samplesort(list(lst))
    print "Sample sort returns {}".format(ans)
    print "Quicksort matches sample: {}".format(ans == quicksort(list(lst)))
    print "Mergesort matches sample: {}".format(ans == mergesort(list(lst)))
    print "Bubblesort matches sample: {}".format(ans == bubblesort(list(lst)))
    print "Insertionsort matches sample: {}".format(ans == insertionsort(list(lst)))
    print "Selectionsort matches sample: {}".format(ans == selectionsort(list(lst)))

if __name__=="__main__":
    start()
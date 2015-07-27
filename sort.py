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

    ans = samplesort(lst)
    print "Sample sort returns {}".format(ans)
    print "Quicksort matches sample: {}".format(ans == quicksort(lst))
    print "Mergesort matches sample: {}".format(ans == mergesort(lst))

if __name__=="__main__":
    start()
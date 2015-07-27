import random
import time

def samplesort(lst):
    start = time.clock()
    return sorted(lst), time.clock() - start

def quicksort(lst):
    def quicksort_helper(lst):
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
        s1 = quicksort_helper(lst1)
        s2 = quicksort_helper(lst2)

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
    start = time.clock()
    ans = quicksort_helper(lst)
    return ans, time.clock() - start
    
def mergesort(lst):
    def mergesort_helper(lst):
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

        s1 = mergesort_helper(lst1)
        s2 = mergesort_helper(lst2)

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
    start = time.clock()
    ans = mergesort_helper(lst)
    return ans, time.clock() - start    

def bubblesort(lst):
    start = time.clock()
    done = False
    while not done:
        done = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                done = False
    return lst, time.clock() - start

def insertionsort(lst):
    start = time.clock()
    for i in [x+1 for x in range(len(lst) - 1)]:
        if lst[i] > lst[i-1]:
            continue
        k = 0
        while lst[i] <= lst[i-k]:
            k += 1
            if i-k == -1:
                break
        lst.insert(i-k+1, lst.pop(i))
    return lst, time.clock() - start

def selectionsort(lst):
    start = time.clock()
    for i in range(len(lst)):
        minimum = i
        for j in range(len(lst[i:])):
            if lst[j+i] < lst[minimum]:
                minimum = j+i
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst, time.clock() - start


if __name__=="__main__":
    lst = []
    for i in range(100):
        lst.append(random.randint(1,100))

    ans = samplesort(list(lst))
    qs = quicksort(list(lst))
    ms = mergesort(list(lst))
    bs = bubblesort(list(lst))
    ins= insertionsort(list(lst))
    sel= selectionsort(list(lst))
    print "Sample sort returns {} in {}".format(ans[0], ans[1])
    print "Quicksort matches sample: {} in {}".format(ans[0] == qs[0], qs[1])
    print "Mergesort matches sample: {} in {}".format(ans[0] == ms[0], ms[1])
    print "Bubblesort matches sample: {} in {}".format(ans[0] == bs[0], bs[1])
    print "Insertionsort matches sample: {} in {}".format(ans[0] == ins[0], ins[1])
    print "Selectionsort matches sample: {} in {}".format(ans[0] == sel[0], sel[1])

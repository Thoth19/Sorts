import random
import argparse
import sort

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='?', type=int, default=1000, dest='number')
    args = parser.parse_args()
    lst = []
    for i in range(args.number):
        lst.append(random.randint(1,100))

    ans = sort.samplesort(list(lst))
    qs  = sort.quicksort(list(lst))
    ms  = sort.mergesort(list(lst))
    bs  = sort.bubblesort(list(lst))
    ins = sort.insertionsort(list(lst))
    sel = sort.selectionsort(list(lst))  
    
    print "Sample sort returns {} in {}".format(ans[0], ans[1])
    print "Quicksort matches sample: {} in {}".format(ans[0] == qs[0], qs[1])
    print "Mergesort matches sample: {} in {}".format(ans[0] == ms[0], ms[1])
    print "Bubblesort matches sample: {} in {}".format(ans[0] == bs[0], bs[1])
    print "Insertionsort matches sample: {} in {}".format(ans[0] == ins[0], ins[1])
    print "Selectionsort matches sample: {} in {}".format(ans[0] == sel[0], sel[1])
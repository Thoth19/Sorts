import random
import sort
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='?', type=int, default=1000, dest='number')
    args = parser.parse_args()
    lst = []
    for i in range(args.number):
        lst.append(random.randint(1,100))

    ans = sort.samplesort(list(lst))
    start = time.clock()
    print "Sample sort returns {} in {} seconds".format(ans, time.clock() - start)
    start = time.clock()
    print "Quicksort matches sample: {} in {} seconds".format(ans == sort.quicksort(list(lst)), time.clock() - start)
    start = time.clock()
    print "Mergesort matches sample: {} in {} seconds".format(ans == sort.mergesort(list(lst)), time.clock() - start)
    start = time.clock()
    print "Bubblesort matches sample: {} in {} seconds".format(ans == sort.bubblesort(list(lst)), time.clock() - start)
    start = time.clock()
    print "Insertionsort matches sample: {} in {} seconds".format(ans == sort.insertionsort(list(lst)), time.clock() - start)
    start = time.clock()
    print "Selectionsort matches sample: {} in {} seconds".format(ans == sort.selectionsort(list(lst)), time.clock() - start)

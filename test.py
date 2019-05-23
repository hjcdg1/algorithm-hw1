from hw1 import *
import timeit

def runtime(f, a, n, k):
    start = timeit.default_timer()
    f(a, n, k)
    end = timeit.default_timer()
    return end - start

for i in range(1, 5) :
    print("=========== " + str(i) + "th test case ===========")
    with open(str(i) + '.txt', 'r') as f :
        first_line = f.readline().split()
        n = int(first_line[0])
        k = int(first_line[1])
        a = []
        while True :
            line = f.readline()
            if not line :
                break
            a.append(int(line))

        print("<Randomized Select Algorithm>")
        sum = 0.0
        for i in range(0, 5) :
            sum = sum + runtime(randomized_select, a, n, k)
        runtime_random = sum / 5
        print('1. run time :', runtime_random)
        print('2. result :', randomized_select(a, n, k))
        print('3. correctness :', checker(a, n, k, randomized_select(a, n, k)))

        print("<Deterministic Select Algorithm>")
        runtime_deter = runtime(deterministic_select, a, n, k)
        print('1. run time :', runtime_deter)
        print('2. result :', deterministic_select(a, n, k))
        print('3. correctness :', checker(a, n, k, deterministic_select(a, n, k)))

        print("<Run time ratio = Randomized/Deterministic>")
        ratio = runtime_random / runtime_deter
        print(ratio)
        print()

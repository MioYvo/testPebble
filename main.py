import os
import time
from multiprocessing import Pool, TimeoutError
from pebble import ProcessPool


def f(s):
    print(f'in {os.getpid()} {s}')
    if s == 100:
        print(f'run forever {os.getpid()} {s}')
        while True:
            pass
    else:
        time.sleep(s)
    print(f'out {os.getpid()} {s}')
    return s


def main():
    with Pool(processes=1) as pool:
        res = pool.apply_async(f, [100])
        try:
            res.get(timeout=10)
        except TimeoutError as e:
            print(f'{e=}')

        time.sleep(2)

        res = pool.apply_async(f, )
        try:
            res.get(timeout=2)
        except TimeoutError as e:
            print(f'{e=}')

        time.sleep(100)


def main2():
    with ProcessPool(3) as pool:
        res = pool.schedule(f, [100], timeout=10)
        res2 = pool.schedule(f, [2], timeout=3)
        res3 = pool.schedule(f, [3], timeout=4)
        # try:
        #     print(f'{res.result(timeout=10)=}')
        # except Exception as e:
        #     print(f'{e=}')

        try:
            print(f'{res2.result(timeout=3)=}')
        except Exception as e:
            print(f'{e=}')

        time.sleep(2)

        res = pool.schedule(f, [3], timeout=4)
        try:
            res.result(timeout=4)
        except Exception as e:
            print(f'{e=}')

        time.sleep(100)


if __name__ == '__main__':
    # main()
    main2()

"""
Written by Carina Nilsson, March 2022, cnl@bth.se
"""
import sys
import os
import time
import logging
import pylint.lint
import numpy as np
from sorting import heapsort
from sorting import quicksort_pivot_first
from sorting import quicksort_pivot_median

# check if Python version is valid for this script
if sys.version < '3.7':
    print('Your Python version is old. It is ' +
          sys.version + ' . Upgrade to at least 3.7')
    sys.exit(1)

TEST_DATA_FILES = ['1000(0,1000).txt', '1000(0,100000).txt',
                   '1000(0,10000000).txt', '10000(0,1000).txt',
                   '10000(0,100000).txt', '10000(0,10000000).txt']


NEWLINE = '\n'
LINT_THRESHOLD = 8.0
TIME_LIMIT = 0.5

FUNC_LIST = ['quicksort_pivot_first', 'quicksort_pivot_median', 'heapsort']

LOG_LEVEL = 'INFO'  # Also DEBUG, INFO, WARNING, ...

TEST_DATA_FILES = ['1000(0,1000).txt', '1000(0,100000).txt',
                   '1000(0,10000000).txt', '10000(0,1000).txt',
                   '10000(0,100000).txt', '10000(0,10000000).txt']

# Large data sets
# TEST_DATA_FILES = ['100000(0,1000).txt', '100000(0,100000).txt',
#                    '100000(0,10000000).txt', '1000000(0,1000).txt',
#                    '1000000(0,100000).txt', '1000000(0,10000000).txt']

# Almost sorted datasets
# TEST_DATA_FILES = [
#     '1000(0,10000).txt', '10000(0,10000).txt', '50000(0,10000).txt']


# functions

def check_functions():
    """Check if required functions are implemented"""
    log.info(
        f'\nTesting if the required functions are implemented. ({FUNC_LIST})')
    print(f'\nTesting if the required functions are implemented.({FUNC_LIST})')
    for func in FUNC_LIST:
        if func not in globals():
            print(f'Test failed!\nThe function {func}() is missing.')
            sys.exit(1)

    log.info('All required functions are there.\n')
    print('All required functions are there.\n')
    return True


def check_quicksort():
    """Sortfunction for Quicksort meets requirements"""
    functions = [quicksort_pivot_first, quicksort_pivot_median]
    for func in functions:
        empty = []
        func(empty)
        if empty:
            print(f'\nEmpty list is not handled correctly.\n')
            return False

        one = [1]
        func(one)
        if one != [1]:
            print('Lists with only one element is not handled correctly')
            return False

        input_list = np.random.randint(-1000, 1000, size=1000).tolist()
        input_copy = input_list[:]
        result = func(input_list)
        if result is not None:
            if isinstance(result, list) and result is not input_list:
                print(
                    '\nTest failed! Quicksort does not seem to be implemented inplace.\n')
                return False

        sorted_list = input_list

        for i in range(0, len(sorted_list)-1):
            if sorted_list[i] > sorted_list[i+1]:
                print('\nTest failed! Sortortorder corrupt.\n')
                log.info('Quicksort sortorder corrupt.\n')
                return False
        for item in input_copy:
            if (sorted_list.count(item) != input_copy.count(item) or
                    len(sorted_list) != len(input_copy)):
                print('\nTest failed! Elements are missing or duplicated\n')
                log.info('Elements are missing or duplicated\n')
                return False

        return True


def check_heapsort(d):
    """Sortfunction for Heapsort meets rquirements"""
    empty = []
    heapsort(empty, d)
    if empty:
        print(f'\nEmpty list is not handled correctly for d={d}.\n')
        return False

    for i in range(d):
        test_list = list(range(d))
        np.random.shuffle(test_list)
        test_copy = test_list[:]
        heapsort(test_list, d)
        if test_list != sorted(test_copy):
            print(
                f'\nList with length {i} is not correctly handled for d={d}.\n')
            return False

    input_list = np.random.randint(-1000, 1000, size=1000).tolist()
    input_copy = input_list[:]
    result = heapsort(input_list, d)
    if result is not None:
        if isinstance(result, list) and result is not input_list:
            print('\nTest failed! Quicksort does not seem to be implemented inplace.\n')
            return False

    sorted_list = input_list

    for i in range(0, len(sorted_list)-1):
        if sorted_list[i] > sorted_list[i+1]:
            print('\nTest failed! Sortorder corrupt.\n')
            log.info('Sortorder corrupt.\n')
            return False
    for item in input_copy:
        if (sorted_list.count(item) != input_copy.count(item) or
                len(sorted_list) != len(input_copy)):
            print('\nTest failed! Elements are missing or duplicated\n')
            log.info('Elements are missing or duplicated\n')
            return False
    return True


def test_code_quality():
    print(
        f'\nChecking code quality by pylint score, {LINT_THRESHOLD} is minimum to pass ...\n')
    log.info(
        f'\nChecking code quality by pylint score, {LINT_THRESHOLD} is minimum to pass')
    stdout = sys.stdout
    outfile = open('pylint_report.txt', 'w')

    sys.stdout = outfile
    run = pylint.lint.Run(
        ['sorting.py'], exit=False)
    score = run.linter.stats['global_note']
    if score < LINT_THRESHOLD:
        log.info(
            f'The pylint score is only {score:.2f}, at least {LINT_THRESHOLD} required')
        sys.stdout = stdout
        outfile.close()
        print(
            f'Test failed!\nThe pylint score is only {score:.2f}, ' +
            f'at least {LINT_THRESHOLD} required')
        print('\nDetailed report can be viewed in pylint_report.txt\n')
        sys.exit(1)
    else:
        sys.stdout = stdout
        print(f'lint score is {score:.2f}')
    log.info('Lint score OK')
    print('\nLint score OK. Detailed lint report can be viewed in pylint_report.txt\n')


def test_sorting():
    """Function testing sorting properties for quicksort and d-ary quicksort"""
    print("\nTesting quicksort... \n")
    if check_quicksort():
        log.info('Correct sorting for Quicksort')
        print('Correct sorting for Quicksort')
    else:
        log.info('Failed sorting for Quicksort')
        print('Failed sorting for Quicksort')
        sys.exit(1)

    print("\nTesting d-ary heapsort... \n")
    for d in range(2, 10):
        if not check_heapsort(d):
            log.info(f'Failed sorting for Heapsort with d={d}')
            print(f'Failed sorting for Heapsort with d={d}')
            sys.exit(1)

    log.info(f'Correct sorting for Heapsort')
    print(f'Correct sorting for Heapsort')


def test_performance(functions, sortfunc_names):
    """Function testing performance for quicksort and d-ary quicksort"""

    print('\nTesting performance ...')
    print('--------------------------')
    for test_nr, file_name in enumerate(TEST_DATA_FILES):
        with open('Testdata/'+file_name, 'r') as file:
            num_list = list(map(int, file.readlines()))

        for i, func in enumerate(functions):
            test_data = num_list.copy()
            timestamp_before = time.perf_counter()
            if i != 2:
                func(test_data)
            else:
                func(test_data, 3)
            timestamp_after = time.perf_counter()
            sec = timestamp_after - timestamp_before
            print(
                f'{sortfunc_names[i]} sorted {len(test_data)} elements in {sec:.3} seconds')

            if sec > TIME_LIMIT:
                print('Test failed!\n')
                print(
                    f'\n{sortfunc_names[i]} sorted too slow ({sec:.4}) seconds,',
                    f'{TIME_LIMIT} seconds is maximum for 10 000 elements')
                log.info(
                    f'{sortfunc_names[i]} sorted too slow ({sec:.4}) seconds, {TIME_LIMIT} seconds is limit')
                sys.exit(1)
        print()

    print('Performance check OK, all timing requirements met')

    log.info('Performance check OK, all requirements met')


if __name__ == '__main__':
    directory = os.path.dirname(os.path.abspath(__file__))
    log = logging.getLogger(__name__)
    logging.basicConfig(filename=directory+'/test.log',
                        level=os.environ.get('LOGLEVEL', LOG_LEVEL),
                        filemode='w',
                        format='\n%(levelname)-4s [L:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')
    sys.setrecursionlimit(10000)
    func_list = [quicksort_pivot_first, quicksort_pivot_median, heapsort]
    func_names = []
    for func in func_list:
        func_names.append(func.__name__)
    check_functions()
    test_sorting()
    test_performance(func_list, func_names)
    test_code_quality()
    print('\nAll tests passed successfully!')
    log.info('\nAll tests passed successfully!')

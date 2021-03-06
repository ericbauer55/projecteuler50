from pe50.solver import *
from pe50.sequences import *
import pytest

##############################################################################################
# Sequence Tests
##############################################################################################

def test_generate_natural_numbers():
    a_max = 10
    A_natural = generate_natural_numbers(a_max=a_max)
    assert A_natural == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_generate_prime_sequence():
    # TODO: implement generate_prime_sequence
    a_max = 30
    A_prime = generate_prime_sequence(a_max=a_max)
    assert A_prime == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

##############################################################################################
# Solver (original) Algorithm Tests
##############################################################################################

def test_consec_sum_solver():
    # The easiest way to test the solver is with a natural number sequence
    a_max = 100
    A_natural = generate_natural_numbers(a_max=a_max)

    assert consec_sum_solver(a_max=a_max, A=A_natural) == 91 # see README for explaination

##############################################################################################
# Solver (new) Algorithm Tests
##############################################################################################

def test_get_partial_sums():
    # validate that the function returns the correct dictionary of partial sums
    # use natural numbers to confirm their triangular number sums
    a_max = 50
    A_natural = generate_natural_numbers(a_max=a_max)

    triangular_sums_dict = {1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45}

    assert get_partial_sums(a_max=a_max, A=A_natural) == triangular_sums_dict

def test_pe_case1():
    # Test the Project Euler specific cases
    # Case 1:
    a_max = 100
    A_prime = generate_prime_sequence(a_max=a_max)
    assert consec_sum_solver2(a_max=a_max, A=A_prime, verbose=True) == 41

def test_pe_case2():
    # Test the Project Euler specific cases
    # Case 2:
    a_max = 1000
    A_prime = generate_prime_sequence(a_max=a_max)
    assert consec_sum_solver2(a_max=a_max, A=A_prime, verbose=True) == 953





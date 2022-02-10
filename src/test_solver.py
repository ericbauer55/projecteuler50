from pe50.solver import *
from pe50.sequences import *
import pytest




def test_consec_sum_solver():
    # The easiest way to test the solver is with a natural number sequence
    a_max = 100
    A_natural = generate_natural_numbers(a_max=a_max)

    assert consec_sum_solver(a_max=a_max, A=A_natural) == 91 # see README for explaination
    



from tabnanny import verbose
from pe50.solver import *
from pe50.sequences import *

if __name__ == '__main__':
    a_max = 1000000
    print('Generating primes sequence...')
    A_prime = generate_prime_sequence(a_max=a_max, verbose=True)
    print(f'There are {len(A_prime)} primes in the sequence.')
    print('-'*50)
    print('Solving for the best prime...')
    best_prime = consec_sum_solver2(a_max=a_max, A=A_prime, verbose=True)
    print('-'*50)
    print(f'best prime = {best_prime}')

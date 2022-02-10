def generate_natural_numbers(a_max):
    """
    This function generates a list of positive natural numbers from 1 to @a_max

    The list of natural numbers is returned
    """
    return list(range(1,a_max+1))

def generate_prime_sequence(a_max):
    """
    This function implements the Sieve of Eratosthenses to find all prime numbers up to @a_max
    Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 

    Input:
    @a_max = this is the largest value in the sequence of primes that is allowed. 

    Output:
    returns a list of all prime numbers <= @a_max
    """
    # Generate a list of candidate prime numbers from 2 to a_max
    candidate_primes = generate_natural_numbers(a_max=a_max) # generates 1 to a_max
    candidate_primes = candidate_primes[1:]

    # Create a dictionary to store the results of each sieve pass
    # Each key is a candidate prime number
    # Each value is a flag for is_composite. If a number is found to be a composite, it is not prime
    sieve_dict = {candidate_num:False for candidate_num in candidate_primes}

    # Initialize the sieve with the prime number 2
    p = 2

    # Mark the initial composites of 2
    sieve_dict = _mark_composites(p, sieve_dict)

    # Filter out the composites to get the remaining prime candidates
    candidate_primes = [num for num in candidate_primes if sieve_dict[num]==False]
    candidate_primes.remove(p) # make sure we don't check p=2 again

    # Start looping after the initial step
    while len(candidate_primes) > 0:
        # Find the next smallest p that is still a candidate prime
        p = min(candidate_primes)

        # Mark composites of p
        sieve_dict = _mark_composites(p, sieve_dict)

        # Filter out the composites to get the remaining prime candidates
        candidate_primes = [num for num in candidate_primes if sieve_dict[num]==False]
        candidate_primes.remove(p) # make sure we don't check same p again
    
    # Gather up all of the candidates that are NOT marked as composites (i.e. are prime numbers):
    primes = [num for num, is_composite in sieve_dict.items() if is_composite==False]

    return primes

def _mark_composites(p, sieve_dict):
    a_max = max(sieve_dict.keys())

    multiple_k = 2
    while p * multiple_k <= a_max:
        sieve_dict[p * multiple_k] = True # mark the kth multiple of p as a composite
        multiple_k += 1 # increment multiple_k

    return sieve_dict

if __name__ == '__main__':
    primes = generate_prime_sequence(a_max=1000)
    print(primes[0:21])
    print(primes)
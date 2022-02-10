from msilib import sequence


def consec_sum_solver(a_max, A, verbose=False):
    """
    This functions finds the largest element of sequence A (and is at most @a_max) which is a partial sum of A.
    In other words, the largest partial sum is the sum of consecutive elements in sequence A. 

    Inputs:
    @a_max = this is the largest value in the sequence A that is allowed. 
    @A = list of elements in the sequence of interest
    @verbose = option to print out the key states for each value of k

    Output:
    @s_max = the maximum partial sum that is still in @A and <= @a_max
    """
    # Initialize the higest partial sum s_max as the value of a_1 in the sequence @A
    s_k = A[0] # k=1
    s_max = s_k
    k = 2 # start k at 2 for the while loop
    k_best = 2

    # Begin looping through
    while (s_k <= a_max) and (k <= len(A)):
        # Calculate the next partial sum candidate
        s_k = sum(A[0:k])

        if verbose:
            print(f'k={k}, a_k={A[k-1]} :: s_k={s_k}, s_max={s_max}')

        # Determine if s_k is in sequence @A and is still at most @a_max
        if (s_k <= a_max) and (s_k in A):
            # s_k is then the new highest partial sum that is valid
            s_max = s_k
            k_best = k

        # Increment k
        k += 1
    
    print('--'*20)
    print(f'For a_max = {a_max}, the best k={k_best} for the partial sum of {s_max}')
    print(f'\tThe consecutive values are:\n{A[0:k_best]}')

    return s_max


def consec_sum_solver2(a_max, A, verbose=False):
    """
    This function find the best prime that is the sum of the most consecutive prime terms

    Inputs:
    @a_max = this is the largest value in the sequence A that is allowed. 
    @A = list of elements in the sequence of interest
    @verbose = option to print out the key states for each value of k

    Output:
    @best_prime = the prime under @a_max that is the sum of the most consecutive prime terms
    """
    # 1. Find all partial sums s_k <= a_max
    sums_dict = get_partial_sums(a_max=a_max, A=A)

    # 2. Initialize the list of searched k values
    searched_k = []
    best_prime = None # starts as None to act as a flag
    best_n_terms = 0 # starts as 0 since any found prime is initially better
    best_k, best_j = None, None # for printing purposes, store these

    # 3. Start searching
    while len(searched_k) < len(sums_dict.keys()): # while there are still k values left to search...
        # Determine the highest, unsearched k value
        k = max([x for x in sums_dict.keys() if x not in searched_k])
        searched_k.append(k) # once selected, record that k has been searched

        # Retrieve the pre-computed partial sum for j=1 to k
        s_jk = sums_dict[k]
        for j in range(1,k):
            # check if s_jk is a prime
            if s_jk in A:
                n_terms = k-j+1
                # check if the prime has more terms. if so, update the best solution
                if n_terms > best_n_terms:
                    best_n_terms = n_terms
                    best_prime = s_jk
                    best_k, best_j = k, j
                # if a prime was found, stop increasing j (regardless if n_terms was better)
                # increasing j can only decrease n_terms for any subsequently found primes
                break
            # if not prime, modify s_jk 
            s_jk = sums_dict[k] - sums_dict[j]

    if verbose:
        print(f'The largest consecutive sum prime is {best_prime} with {best_n_terms} terms')
        print(f'terms: {A[best_j-1:best_k]}')
    
    return best_prime
    





def get_partial_sums(a_max, A):
    """
    This function creates all partial sums from elements 1 to k of sequence @A.
    The generation stops once the kth sum exceeds @a_max 

    Inputs:
    @a_max = this is the largest value in the sequence A that is allowed. 
    @A = list of elements in the sequence of interest

    Output:
    @sums_dict = dictionary where the keys are index k and values are the partial sum s_k = sum(a1...ak) <= @a_max
    """
    # initialize the partial sums list 
    k=1
    partial_sums = [A[0]]
    # initialize the next partial sum as the initial condition to enter the while loop
    s_k = partial_sums[k-1]

    # As long as the next partial sum is less than @a_max, append it to the list and k++
    while (s_k <= a_max) and (k < len(A)):
        s_k = partial_sums[k-1] + A[k]
        if s_k <= a_max:
            partial_sums.append(s_k)
        k += 1
    
    sums_dict = {i+1:sum for i, sum in enumerate(partial_sums)}
    return sums_dict

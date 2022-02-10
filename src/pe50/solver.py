def consec_sum_solver(a_max, A):
    """
    This functions finds the largest element of sequence A (and is at most @a_max) which is a partial sum of A.
    In other words, the largest partial sum is the sum of consecutive elements in sequence A. 

    Inputs:
    @a_max = this is the largest value in the sequence A that is allowed. 
    @A = list of elements in the sequence of interest

    Output:
    @s_max = the maximum partial sum that is still in @A and <= @a_max
    """
    # Initialize the higest partial sum s_max as the value of a_1 in the sequence @A
    s_k = A[0] # k=1
    s_max = s_k
    k = 2 # start k at 2 for the while loop

    # Begin looping through
    while (s_k <= a_max) and (k <= len(A)):
        # Calculate the next partial sum candidate
        s_k = sum(A[0:k])

        # Determine if s_k is in sequence @A and is still at most @a_max
        if (s_k <= a_max) and (s_k in A):
            # s_k is then the new highest partial sum that is valid
            s_max = s_k

        # Increment k
        k += 1

    return s_max
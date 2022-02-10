# Project Euler 50
I love Project Euler! It was one of the puzzle sites (besides Rosalind) I found early in my programming days. Especially in late High School and early college, I would work on various PE problems in C or C++ to try to learn algorithms. It is always a good idea to revisit them when you can. I have no idea if I have worked on problem 50 before, so it is fresh enough to try again in Python. I'm also going to try to employ TDD (Test-driven Development) on this quick project, so I learn something regardless.

The full description of the problem can be found on the [problem page](https://projecteuler.net/problem=50) but essentially, I need to write a program that will do the following:

> Which prime number under 1,000,000 is the sum of the most consecutive primes? (Ex: under 100, the answer is 41 = 2 + 3 + 5 + 7 + 11 + 13) 

## 1. Solution Checklist
- [x] Draft algorithm pseudocode for README
- [x] Write Unit tests for example solutions (*a*<sub>max</sub> = [100, 1000])
- [x] Write algorithm code framework in Python 
- [x] Test the framework using Triangular Sums 
- [x] Create a Prime Number generator
- [ ] Run sample problem specific unit tests
- [ ] Run algorithm for *a*<sub>max</sub> = 1,000,000 and submit to PE

## 2. Algorithm Pseudocode
Rather than doing this as my 2012 self would have, let me put "brute force" off the table for now. Sequences can be a pain mathematically, especially when evaluating the convergence of infinite sums of elements. Luckily, everything in this problem is finite. To start off, let us define some variables for the pseudocode:

- Let ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) represent the maximum value of the consecutive summation. For the test cases, it is 100 or 1000. For the final evaluation, it is 1000000.
- Let ![formula](https://render.githubusercontent.com/render/math?math=A=\\{a_i\\}_{i=1}^{N}) be the sequence of interest (primes for this problem), where *N* satisfies ![formula](https://render.githubusercontent.com/render/math?math=a_N%20\leq%20a_{max}).
- Define the partial sum of the first *k* elements in sequence *A* as ![formula](https://render.githubusercontent.com/render/math?math=s_k=\sum_{i=1}^k%20a_i). 
 
**Based on the definitions:** We want to find the largest partial sum satisfying ![formula](https://render.githubusercontent.com/render/math?math=s_k^*%20\leq%20a_{max}) and ![formula](https://render.githubusercontent.com/render/math?math=s_k^*%20\in%20A). Knowing the value of *k* will also tell us what subsequence of *A* was used! While not required for the problem, checking this subsequence will be useful for intuitive checking.

### Pseudocode

0. Initialize ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) to 100, 1000 or 1000000 depending on the test or evaluation scenario.
1. Initialize the sequence of interest, *A* for ![formula](https://render.githubusercontent.com/render/math?math=i^*%20\in%20[1,2,...,N]) and ![formula](https://render.githubusercontent.com/render/math?math=a_1=2) for the sequence of primes.
2. Initialize the highest partial sum ![formula](https://render.githubusercontent.com/render/math?math=s^*=a_1) for the case *k*=1. 
    - Also initialize ![formula](https://render.githubusercontent.com/render/math?math=s_k=a_1)
3. Initialize *k*=2 and ![formula](https://render.githubusercontent.com/render/math?math=s_k=2)
4. **WHILE** ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\leq%20a_{max}):
    1. Calculate the partial sum ![formula](https://render.githubusercontent.com/render/math?math=s_k)
    2. **IF** ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\in%20A) **AND** ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\leq%20a_{max}):
        - Reassign the largest valid partial sum with the *k*<sup>th</sup> partial sum ![formula](https://render.githubusercontent.com/render/math?math=s^*=s_k) 
    3. Increment *k* by 1
5. After the while condition fails, ![formula](https://render.githubusercontent.com/render/math?math=s^*) is the largest number in sequence *A* that is the consecutive sum of its elements and is also no more than ![formula](https://render.githubusercontent.com/render/math?math=a_{max}). **DONE**

Assuming all elements of sequence *A* are positive (which is true for the primes) then the partial sum of *k* elements is always larger than for *j<k*. If ![formula](https://render.githubusercontent.com/render/math?math=s_k) and ![formula](https://render.githubusercontent.com/render/math?math=s^*=s_j) are valid elements in sequence *A*, then there is no need to check in the pseudocode if ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\gt%20s^*) since that is implied.

**Implementation Note:** Step 0 will be implemented as a list since sequence *A* consists of at most 1,000,000 values. My computer shouldn't shed any tears over this being held in memory. Another possibility is to create the sequence using a Python generator statement. It is still necessary to store the *k*<sup>th</sup> subsequence of *A*, however.

## Testing the Code
Because the problem has 2 examples with solutions given (![formula](https://render.githubusercontent.com/render/math?math=a_{max}=100) and ![formula](https://render.githubusercontent.com/render/math?math=a_{max}=1000)), it will be easy to start with unit tests. The algorithm above will be implemented into some function `consec_sum_solver(a_max, A)` which takes the maximum element limit and generated sequence *A* as arguments. The sequence *A* should be generated by another function `generate_prime_sequence(a_max)` that will create elements up to the limit. Unit tests then will verify the following:

- :white_check_mark: Assert `consec_sum_solver(a_max=100, A) = 41`
- :white_check_mark: Assert `consec_sum_solver(a_max=1000, A) = 953`

### Verifying the Algorithm with Natural Numbers
The above unit tests are dependent on the existence of `generate_prime_sequence(a_max)` to create a prime sequence. This is a subtask of this particular Project Euler Problem. I will handle it after I verify the pseudocode algorithm works correctly. As such, I will test the algorithm implemented in `consec_sum_solver(a_max, A)` with a simple, toy sequence--the postive natural numbers 1,2,3...etcetera.

Let ![formula](https://render.githubusercontent.com/render/math?math=A=\\{i\\}_{i=1}^{a_max}) be the sequence of postivie natural numbers up to the maximum ![formula](https://render.githubusercontent.com/render/math?math=a_{max}). The partial sums of this sequence are known as [Triangular Numbers](https://en.wikipedia.org/wiki/Triangular_number) and have a nice, closed-form expression.

Specifically, the partial sum is: ![](images/triangular_sum_small.jpg). Hence it is easy to verify that ![formula](https://render.githubusercontent.com/render/math?math=s^*%20\leq%20a_{max}) for the best value of *k*<sup>*</sup> can be analytically derived for easy unit testing.

The following is a quick derivation of the the quadratic relationship to solve:

![](images/completed_squares.jpg)

By re-arranging the terms and completing the square, I arrive at the relationship in yellow. It is easy now to see the visual intuition on what the optimal *k*<sup>*</sup> is:

![](images/optimal_k_region.jpg)

To guarantee that ![formula](https://render.githubusercontent.com/render/math?math=s^*%20\leq%20a_{max}) is still satisfied and ![formula](https://render.githubusercontent.com/render/math?math=s^*%20\in%20A) (i.e. is a natural number), I must apply the floor function to the root of the *k*<sup>*</sup> quadratic. Hence the formula for the triangular numbers solution is:

![](images/triangular_solution.jpg)

### Natural Numbers Unit Test
Suppose that ![formula](https://render.githubusercontent.com/render/math?math=a_{max}=100), then 91 = 1+2+3+4+...+12+13 is the largest natural number under ![formula](https://render.githubusercontent.com/render/math?math=a_{max}=100) that can be written as the sum of consecutive natural numbers in sequence *A*. Using the formula derived above, *k*<sup>*</sup>=13 which leads to the optimal partial sum of 91!

So for the unit test, I can assert the following assuming a very simple `generate_natural_numbers(a_max)` function creates input sequence `A`:

- :white_check_mark: Assert `consec_sum_solver(a_max=100, A) = 91`

After developing the algorithm based on the pseudocode, I tested it using the natural numbers:

![](images/pytest_algo_check.png)

It is expected that the prime sequence generator and the two Project Euler sample cases fail. They have not been developed yet. 

## 3. Generating Prime Numbers
Generating a list of prime numbers up to a limit (in this case up to ![formula](https://render.githubusercontent.com/render/math?math=a_{max})) is a problem I solved a long time ago when I originally got into Project Euler. In fact, [Problem 7](https://projecteuler.net/problem=7) is very much related to this. Given that the crux of Problem 50 is not generating prime numbers, I will refer back to the algorithms of my youth:

1. Building a list of primes with [Trial Division](https://en.wikipedia.org/wiki/Trial_division) and a square root heuristic
2. Building a list of primes with the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

The Sieve method seems like a method to use for this Problem 50. In the interest of space, I won't repeat the sieve algorithm here. Please see the `pe50.sequences` code for its implementation. 

After developing the Sieve code, my tests run a bit better:

![](images/pytest_sieve_check.png)

I now pass `test_generate_prime_sequence`, which was intended, as well as the first case of the Problem 50 examples--`test_pe_case1`. All that's left is to get the second example working and then run it for ![formula](https://render.githubusercontent.com/render/math?math=a_{max}=1000000).

## 4. Getting Case 2 to Work
It is very strange that Case 1 works but Case 2 does not. To investigate this further, I added in some more verbose print statements to the solver function. It's result on the failed test is:

![](images/debugging_case2.png)

Consider the second case again:

> The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

What is strange from the print out is that 963 is the partial sum that is closest to 953, but is 10 over and thus not in the primes sequence. Additionally, 963 is the partial sum for *k*=24. The prompt mentions that there are 21 terms...so...if I take out the first 3 terms [2,3,5] I get a 21 term subsequence that sums to 953. 

![DAMN](images/bamboozle.jpg)

This means that my understanding of the problem is not accurate and the pseudocode above doesn't apply. If you've read this far then I assure you I am swearing enough for the both of us. Anyways, onwards and upwards.

## 5. Rethinking the Problem
**Goal**: The longest sum of consecutive primes that is still a prime and is under ![formula](https://render.githubusercontent.com/render/math?math=a_{max}). 

A solution with the most terms in the sum will consequently be a larger number given a sequence of primes. Hence, my original focus of finding the largest prime under ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) that is a partial sum of the primes sequence. This is close, but I over constrained myself. Specifically, my partial sum method assumes that the subsequence to sum over is ![formula](https://render.githubusercontent.com/render/math?math=A_k=\\{a_i\\}_{i=1}^{k}%20\subset%20A). This worked for Case 1 where 41 is the answer. But this did not work for Case 2, where the the 21 term subsequence only added to 712 instead of 953.

The difference that I noticed was that if I had summed the primes from ![formula](https://render.githubusercontent.com/render/math?math=a_{4}=7) to ![formula](https://render.githubusercontent.com/render/math?math=a_{24}=89), I get 21 consecutive terms that sum to 953--which is the largest prime under 1000 for Case 2.

With that in mind, I will modify my definition of a subsequence to include the starting point as a parameter: ![formula](https://render.githubusercontent.com/render/math?math=A_{jk}=\\{a_i\\}_{i=j}^{k}). The starting point is ![formula](https://render.githubusercontent.com/render/math?math=j%20\in%20[1,2,...,k-1,k]). A successful solution will make sure ![formula](https://render.githubusercontent.com/render/math?math=j%20\ll%20k) since increasing *j* reduces the number of terms available in the sum.

If *j* reduces the number of terms for the partial sum, why increase it at all? For the case of the 24th partial sum ![formula](https://render.githubusercontent.com/render/math?math=s_{24}=963), the first 3 elements in the sequence are causing the partial sum to shoot above the target 953. So increasing *j*=1 to *j=4* finds a subsequence ![formula](https://render.githubusercontent.com/render/math?math=A_{jk}) that sums up to a prime. 

For notation's sake, I will represent this new partial sum as ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}=\sum_{i=j}^k%20a_i) .

### New Algorithm Intuition
Intuitively, the process is to start with the highest partial sum ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}%20\leq%20a_{max}). If ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}) is not already a prime (i.e. ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}%20\in%20A)), then increment *j* to recompute ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}). Continue this process until ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}) is prime or *j*=*k*. If the latter condition is true, there was no way to create a subsequence that sums to a prime. In that case, decrease *k* and search again. In the case where ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}) is prime, keep track of the result. There may be a lower partial sum that has a longer consecutive sum of elements that is prime. The goal is to find the largest sequence ![formula](https://render.githubusercontent.com/render/math?math=A_{jk}) whose length is *k-j+1*.  

I will develop the algorithm in code first and then capture the exact pseudocode here in the README. A couple of important things standout:

- Assuming a prime partial sum, ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}), exists for some *j*, it comes down to searching across values of j. Perhaps there is a cleaner search process than a linear sweep?
- Because each search step for *j* relies on recomputing ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}), it may be helpful to cache partial sum values. In fact, the partial sum ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}) can be composed of two partial sums--one for the entire sequence using 1 to *k* and another for 1 to *j-1*. The latter sum is thrown away as *j* increases. Hence, ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}=s_k-s_{j-1}) based on the initial definition of partial sums starting from *i*=1.

I will start with a linear sweep of *j*, though if it runs too slowly for large ![formula](https://render.githubusercontent.com/render/math?math=a_{max}), I will optimize it. Additionally, I will calculate and cache all partial sums ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\leq%20a_{max}) for easy lookup.

**Unit Testing Note:** I will not test the new algorithm on the Natural Numbers case since any sum of natural numbers is still a natural number. This represents a trivial case for the algorithm and it will not represent my algorithm's future success of a sequence of primes.

### New Algorithm Implementation:
The algorithm intuition above proved to be mostly correct! I will highlight any significant additions or deviations here, but please check the implementation of `consec_sum_solver2(a_max, A, verbose=False)` in the `pe50.solver` module.

- Added a `searched_k = []` list to store which values of *k* have been searched already. This search space fills up as the while loop runs
- I stored the current candidate solution as `best_prime` but only updated it when ![formula](https://render.githubusercontent.com/render/math?math=s_{jk}%20\in%20A) and the number of terms (*k-j+1*) was better than the current highest number of terms, `best_n_terms`.
- Initially, my algorithm stopped once it found the first value of k for which a subsequence *j*-->*k* was prime. This didn't necessarily imply that `best_n_terms` was the highest for all values of *k*!
    - Because 953 is so close to 1000, this algorithm heuristic worked well and Case 2's test passed
    - The example for Case 1 of `best_prime=41` and `best_n_terms=6` failed with this heuristic. This is because 83 could be written as 11+13+17+19+23, which is the highest value primes under 100, but it was composed of only 5 terms, instead of 6. 
- To correct the search-stopping heuristic, I simply let the while loop exhaust the search space for *k*. I shall see if this needs optimization for ![formula](https://render.githubusercontent.com/render/math?math=a_{max}=1000000)...

After finishing the implementation, I see the blessed 100% all green on the tests!

![](images/pytest_all_pass.png)






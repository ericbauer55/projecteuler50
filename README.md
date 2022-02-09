# Project Euler 50
I love Project Euler! It was one of the puzzle sites (besides Rosalind) I found early in my programming days. Especially in late High School and early college, I would work on various PE problems in C or C++ to try to learn algorithms. It is always a good idea to revisit them when you can. I have no idea if I have worked on problem 50 before, so it is fresh enough to try again in Python.

The full description of the problem can be found on the [problem page](https://projecteuler.net/problem=50) but essentially, I need to write a program that will do the following:

> Which prime number under 1,000,000 is the sum of the most consecutive primes? (Ex: under 100, the answer is 41 = 2 + 3 + 5 + 7 + 11 + 13) 

## Solution Checklist
- [ ] Draft algorithm pseudocode for README
- [ ] Write Unit tests for example solutions (*a*<sub>max</sub> = [100, 1000])
- [ ] Write algorithm code framework in Python 
- [ ] Test the framework using Triangular Sums 
- [ ] Create a Prime Number generator
- [ ] Run sample problem specific unit tests
- [ ] Run algorithm for *a*<sub>max</sub> = 1,000,000 and submit to PE

## Algorithm Pseudocode
Rather than doing this as my 2012 self would have, let me put "brute force" off the table for now. Sequences can be a pain mathematically, especially when evaluating the convergence of infinite sums of elements. Luckily, everything in this problem is finite. To start off, let us define some variables for the pseudocode:

- Let ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) represent the maximum value of the consecutive summation. For the test cases, it is 100 or 1000. For the final evaluation, it is 1000000.
- Let ![formula](https://render.githubusercontent.com/render/math?math=A=\\{a_i\\}_{i=1}^{N}) be the sequence of interest (primes for this problem), where *N* satisfies ![formula](https://render.githubusercontent.com/render/math?math=a_N%20\leq%20a_{max}).
- Define the partial sum of the first *k* elements in sequence *A* as ![formula](https://render.githubusercontent.com/render/math?math=s_k=\sum_{i=1}^k%20a_i). 
 
**Based on the definitions:** We want to find the largest partial sum satisfying ![formula](https://render.githubusercontent.com/render/math?math=s_k^*%20\leq%20a_{max}) and ![formula](https://render.githubusercontent.com/render/math?math=s_k^*%20\in%20A). Knowing the value of *k* will also tell us what subsequence of *A* was used! While not required for the problem, checking this subsequence will be useful for intuitive checking.

### Pseudocode

0. Initialize ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) to 100, 1000 or 1000000 depending on the test or evaluation scenario.
1. Initialize the sequence of interest, *A* for ![formula](https://render.githubusercontent.com/render/math?math=i^*%20\in%20[1,2,...,N]) and ![formula](https://render.githubusercontent.com/render/math?math=a_1=2) for the sequence of primes.
2. Initialize the highest partial sum ![formula](https://render.githubusercontent.com/render/math?math=s^*=2) for the case *k*=1. 
3. Initialize *k*=2 and ![formula](https://render.githubusercontent.com/render/math?math=s_k=2)
4. WHILE ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\leq%20a_{max}):
    1. Calculate the partial sum ![formula](https://render.githubusercontent.com/render/math?math=s_k)
    2. IF ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\in%20A) AND ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\leq%20a_{max}):
        - Reassign the largest valid partial sum with the *k*<sup>th</sup> partial sum ![formula](https://render.githubusercontent.com/render/math?math=s^*=s_k) 
    3. Increment *k* by 1

Assuming all elements of sequence *A* are positive (which is true for the primes) then the partial sum of *k* elements is always larger than for *j<k*. If ![formula](https://render.githubusercontent.com/render/math?math=s_k) and ![formula](https://render.githubusercontent.com/render/math?math=s^*=s_j) are valid elements in sequence *A*, then there is no need to check in the pseudocode if ![formula](https://render.githubusercontent.com/render/math?math=s_k%20\gt%20s^*) since that is implied.


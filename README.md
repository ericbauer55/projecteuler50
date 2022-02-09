# Project Euler 50
I love Project Euler! It was one of the puzzle sites (besides Rosalind) I found early in my programming days. Especially in late High School and early college, I would work on various PE problems in C or C++ to try to learn algorithms. It is always a good idea to revisit them when you can. I have no idea if I have worked on problem 50 before, so it is fresh enough to try again in Python.

The full description of the problem can be found on the [problem page](https://projecteuler.net/problem=50) but essentially, I need to write a program that will do the following:

> Which prime number under 1,000,000 is the sum of the most consecutive primes? (Ex: under 100, the answer is 41 = 2 + 3 + 5 + 7 + 11 + 13) 

## Solution Checklist
- [ ] Draft algorithm pseudo code for README
- [ ] Write Unit tests for example solutions (*a*<sub>max</sub> = [100, 1000])
- [ ] Write algorithm code framework in Python 
- [ ] Test the framework using Triangular Sums 
- [ ] Create a Prime Number generator
- [ ] Run sample problem specific unit tests
- [ ] Run algorithm for *a*<sub>max</sub> = 1,000,000 and submit to PE

## Algorithm Pseudocode
Rather than doing this as my 2012 self would have, let me put "brute force" off the table for now. Sequences can be a pain mathematically, especially when evaluating the convergence of infinite sums of elements. Luckily, everything in this problem is finite. To start off, let us define some variables for the pseudo code:

- Let ![formula](https://render.githubusercontent.com/render/math?math=a_{max}) represent the maximum value of the consecutive summation. For the test cases, it is 100 or 1000. For the final evaluation, it is 1000000.
- Let ![formula](https://render.githubusercontent.com/render/math?math=A=\{a_i\}_{i=1}^{N}) be the sequence of interest (primes for this problem), where *N* satisfies ![formula](https://render.githubusercontent.com/render/math?math=a_N\leqa_{max}).

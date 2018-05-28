# Taylor Series Estimation Tool for Basic Functions
Use Taylor Series Expansions to estimate sin(x), cos(x) and e^(x) to input precision

The motivation for this project is because Python's math module's e constant only contains 16 digits of precision, this program can easily estimate to over 1000 digits for e, sin and cos

The program uses memoization (Dynamic Programming) with Python dicitonaries (hash table) to optimize factorial calculations which occur VERY frequently in taylor series. It has nested loops however that reduce it's efficiency significantly and next steps on this would be to optimize the algorithm to prevent the use of inefficient loop structure.

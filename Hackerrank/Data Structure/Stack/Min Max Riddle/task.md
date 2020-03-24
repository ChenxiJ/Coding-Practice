Given an integer array of size n, find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.


For example, given arr = [6, 3, 5, 1, 12], consider window sizes of 1 through 5. Windows of size 1 are (6), (3), (5), (1), (12). 
The maximum value of the minimum values of these windows is 12. Windows of size 2 are (6, 3), (3, 5), (5, 1), (1, 12), and their minima are (3, 3, 1, 1). 
The maximum of these values is 3. Continue this process through window size 5 to finally consider the entire array. All of the answers are 12, 3, 3, 1, 1.

Complete the riddle function in the editor below. It must return an array of integers representing the maximum minimum value for 
each window size from 1 to n.


link: https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

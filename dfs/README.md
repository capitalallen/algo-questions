## Depth First Search (DFS)
- using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.
    - the space complexity of the algorithm will be O(H), where ‘H’ is the maximum height of the tree.
### Binary Tree Path Sum
- To recursively traverse a binary tree in a DFS fashion, we can start from the root and at every step, make two recursive calls one for the left and one for the right child.
1. Start DFS with the root of the tree.
2. If the current node is not a leaf node, do two things:
    - Subtract the value of the current node from the given number to get a new sum => S = S - node.value
    - Make two recursive calls for both the children of the current node with the new number calculated in the previous step.
3. At every step, see if the current node being visited is a leaf node and if its value is equal to the given number ‘S’. If both these conditions are true, we have found the required root-to-leaf path, therefore return true.
5. If the current node is a leaf but its value is not equal to the given number ‘S’, return false.

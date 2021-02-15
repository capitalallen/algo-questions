## Breadth First Search (BFS)
- Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. 
- use a Queue to keep track of all the nodes of a level before we jump onto the next level.
- O(W)O(W), where ‘W’ is the maximum number of nodes on any level.
### Binary Tree Level Order Traversal
- We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:
1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (let’s call it levelSize). We will have 4. these many nodes in the current level.
5. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
6. After removing each node from the queue, insert both of its children into the queue.
7. If the queue is not empty, repeat from step 3 for the next level.
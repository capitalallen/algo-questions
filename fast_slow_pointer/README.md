##  Fast & Slow pointer
- so known as the Hare & Tortoise algorithm
- a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds.
- useful when dealing with cyclic LinkedLists or arrays.
- By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.
### LinkedList Cycle
- have a slow and a fast pointer to traverse the LinkedList. In each iteration, the slow pointer moves one step and the fast pointer moves two steps.
    1. If the LinkedList doesn’t have a cycle in it, the fast pointer will reach the end of the LinkedList before the slow pointer to reveal that there is no cycle in the LinkedList.
    2. The slow pointer will never be able to catch up to the fast pointer if there is no cycle in the LinkedList.
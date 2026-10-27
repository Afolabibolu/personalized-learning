# Trees and Search Trees

## Terminology

A **tree** is a non-linear, hierarchical structure of nodes. The top node is the **root**; a node directly above another is its **parent**, and the node below is its **child**. Nodes with the same parent are **siblings**, and nodes with no children are **leaves**. The **level** of a node is its distance from the root (root at level 0), and the **degree** of a node is its number of children. A tree differs from a graph in having exactly one path between any two nodes and no cycles.

## Binary trees and traversal

In a **binary tree** each node has at most two children, left and right.

- **Preorder:** root, left, right.
- **Inorder:** left, root, right.
- **Postorder:** left, right, root.

An **expression tree** stores operators in internal nodes and operands in leaves; for (a − b) + 40 / x the root is +. Inorder traversal gives the infix expression, and postorder gives postfix.

## Binary search trees

In a **binary search tree (BST)**, every key in a node's left subtree is smaller than the node's key, and every key in the right subtree is larger. Inorder traversal therefore lists the keys in sorted order.

- **Search and insertion:** compare with the root and move left or right until the key or an empty place is found. Keys inserted in the order given build the tree.
- **Deletion** has three cases:
  1. a leaf is removed directly;
  2. a node with one child is replaced by that child;
  3. a node with two non-empty subtrees is replaced by its **inorder successor** (the smallest key in the right subtree) or inorder predecessor, which is then deleted.

## Balanced trees

- **AVL tree:** a BST in which the heights of each node's two subtrees differ by at most one (balance factor −1, 0 or +1). Rotations restore balance after an insertion, keeping searches O(log n).
- **Red-black tree:** a BST whose nodes are coloured red or black. The root is black, a red node has no red child, and every path from a node to its leaves has the same number of black nodes.
- **B-tree of order m:** a multi-way search tree in which each node has at most m children and m − 1 keys, and all leaves are on the same level. It suits disk storage.
- **B+ tree:** keeps all records in the leaves, which are linked together, and uses the internal nodes only as an index.
- **Trie:** a tree of characters in which each path from the root spells a prefix, which supports autocomplete.

Source: general knowledge, following the CSC 341 past papers (2020/21 to 2024/25 papers); the course notes do not cover trees

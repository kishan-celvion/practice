class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right
node = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)
node.left = node7
node.right = node15
node7.left = node3
node7.right = node8
node15.left = node14
node15.right = node19
node19.left = node18

# print("Q-1")
# def search_bst(root, val):
#     if root is None:
#         return None
#     if root.data == val:
#         return root
#     if val < root.data:
#         return search_bst(root.left, val)
#     return search_bst(root.right, val)
# res = search_bst(node, 8)
# print(res.data)


# print("Q-2")
# def insert_into_bst(root, val):
#     if root is None:
#         return TreeNode(val)
#     else:
#         if val < root.data:
#             root.left = insert_into_bst(root.left, val)
#         else:
#             root.right = insert_into_bst(root.right, val)
#     return root
# def printBST(root):
#     if root is None:
#         return 
#     printBST(root.left)
#     print(root.data, end=" ")
#     printBST(root.right)
# printBST(node)
# insert_into_bst(node, 10)
# printBST(node)


# print("Q-3")
# def find_min(root):
#     curr = root
#     while curr.left is not None:
#         curr = curr.left
#     return curr.data
# def find_max(root):
#     curr = root
#     while curr.right is not None:
#         curr = curr.right
#     return curr.data
# print(find_min(node))
# print(find_max(node))


# print("Q-4 Recursion")
# def inorder_traversal(root):
    # res = []
    # def travese(root):
    #     if root is None:
    #         return
    #     res.append(root.data)
    #     travese(root.left)
    #     travese(root.right)
    # travese(root)
    # return res
# print(inorder_traversal(node))


# print("Q-4 Iterative")
# def inorder_traversal(root):
#     res = []
#     st = []
#     while True:
#         while root:
#             st.append(root)
#             st.append(root)
#             root = root.left
#         if not st:
#             return res
#         root = st.pop()
#         if st and st[-1] == root:
#             root = root.right
#         else:
#             res.append(root.data)
#             root = None
# print(inorder_traversal(node))


# print("Q-5")
# def is_valid_bst(root):
#     def helper(root, traversal):
#         if root is None:
#             return
#         helper(root.left, traversal)
#         traversal.append(root.data)
#         helper(root.right, traversal)
#     traversal = []
#     helper(root, traversal)
#     for i in range(1, len(traversal)):
#         if traversal[i] <= traversal[i-1]:
#             return False
#     return True
# print(is_valid_bst(node))


# print("Q-6")
# def lowest_common_ancestor(root, p, q):
#     if root is None:
#         return
#     if root.data == p or root.data == q:
#         return root.data
#     leftLCA = lowest_common_ancestor(root.left, p, q)
#     rightLCA = lowest_common_ancestor(root.right, p, q)
#     if leftLCA and rightLCA:
#         return root
#     return rightLCA if rightLCA else leftLCA
# ans = lowest_common_ancestor(node, 3, 8)
# print(ans.data)


# print("Q-7")
# def newRoot(root):
#     curr = root
#     if root.left is not None:
#         curr = root.left
#     return curr
# def delete_node(root, key):
#     if root is None:
#         return
#     if key < root.data:
#         root.left = delete_node(root.left, key)
#     elif key > root.data:
#         root.right = delete_node(root.right, key)
#     else:
#         if not root.right:
#             temp = root.left
#             root = None
#             return temp
#         elif not root.left:
#             temp = root.right
#             root = None
#             return temp
#         root.data = newRoot(root.right).data
#         root.right = delete_node(root.right, root.data)
#     return root
# def printBST(root):
#     if root is None:
#         return 
#     printBST(root.left)
#     print(root.data, end=" ")
#     printBST(root.right)
# printBST(node)
# ans = delete_node(node, 7)
# print()
# printBST(ans)


# print("Q-8")
# def kth_smallest(root, k):
#     def inorderTraversal(r, values):
#         if r:
#             inorderTraversal(r.left, values)
#             values.append(r.data)
#             inorderTraversal(r.right, values)
#     values = []
#     inorderTraversal(root, values)
#     kth_smallest = values[k-1]
#     return kth_smallest
# ans = kth_smallest(node, 3)
# print(ans)


# print("Q-9")
# def sorted_array_to_bst(nums):
#     if len(nums) == 0:
#         return
#     mid = len(nums) // 2
#     root = TreeNode(nums[mid])
#     root.left = sorted_array_to_bst(nums[:mid])
#     root.right = sorted_array_to_bst(nums[mid+1:])
#     return root
# def printBST(root):
#     if root is None:
#         return
#     print(root.data, end=" ")
#     printBST(root.left)
#     printBST(root.right)
# arr = [-10, -3, 0, 5, 9]
# ans = sorted_array_to_bst(arr)
# printBST(ans)
# # Output [0, -3, 9, -10, 5]


# print("Q-10")
# class BSTIterator:
#     def __init__(self, root):
#         self.st = []
#         self.putinleft(root)
#     def putinleft(self, root):
#         while root:
#             self.st.append(root)
#             root = root.left
#     def next(self):
#         node = self.st.pop()
#         val = node.data
#         if node.right:
#             self.putinleft(node.right)
#         return val
#     def has_next(self):
#         return len(self.st) > 0
# obj = BSTIterator(node)
# print(obj.next())
# print(obj.next())
# print(obj.has_next())
# print(obj.next())
# print(obj.has_next())
# print(obj.next())
# print(obj.has_next())


# print("Q-11")
# def recover_tree(root):
#     almostsort = [] 
#     swap = None
#     def inorder(r):
#         if r is None:
#             return
#         inorder(r.left)
#         almostsort.append(r)
#         inorder(r.right)
#     inorder(root)
#     for i in range(len(almostsort) -1):
#         if almostsort[i].data > almostsort[i+1].data:
#             if swap is None:
#                 swap = [almostsort[i], almostsort[i+1]]
#             else:
#                 swap[1] = almostsort[i+1]
#     swap[0].data, swap[1].data = (swap[1].data, swap[0].data)
#     return root
# def printBST(root):
#     if root is None:
#         return
#     print(root.data, end=" ")
#     printBST(root.left)
#     printBST(root.right)
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n1.left = n3
# n3.right = n2
# printBST(n1)
# ans = recover_tree(n1)
# print()
# printBST(ans)


# print("Q-12")
# def range_sum_bst(root, low, high):
#     if root is None:
#         return 0
#     if root.data < low:
#         return range_sum_bst(root.right, low, high)
#     elif root.data > high:
#         return range_sum_bst(root.left, low, high)
#     left = range_sum_bst(root.left, low, high)
#     right = range_sum_bst(root.right, low, high)
#     return (root.data + left + right)
# print(range_sum_bst(node, 7, 15))


# print("Q-13")
# def bst_to_gst(root):
#     s = 0
#     def inorder(node, s):
#         if node is None:
#             return
#         inorder(node.right, s)
#         s += node.data
#         node.data = s
#         inorder(node.left, s)
#     inorder(root, s)
#     return root
# def inorder_traversal(root):
#     res = []
#     def travese(root):
#         if root is None:
#             return
#         res.append(root.data)
#         travese(root.left)
#         travese(root.right)
#     travese(root)
#     return res
# ans = bst_to_gst(node)
# print(inorder_traversal(ans))


# print("Q-14")
# def is_balanced(root):
#     if root is None:
#         return True
#     def height(root):
#         if not root:
#             return 0
#         left = height(root.left)
#         right = height(root.right)
#         if left == -1 or right == -1 or abs(left - right) > 1:
#             return -1
#         return 1 + max(left, right)
#     return height(root) != -1
# print(is_balanced(node))


# print("Q-15")
# from collections import deque
# class Codec:
#     def serialize(self, root):
#         if root is None:
#             return ""
#         res = ""
#         q = deque()
#         q.append(root)
#         while q:
#             curr_node = q.popleft()
#             if curr_node is None:
#                 res += "#,"
#             else:
#                 res += str(curr_node.data) + ","
#                 q.append(curr_node.left)
#                 q.append(curr_node.right)
#         return res
#     def deserialize(self, data):
#         if data is None:
#             return None
#         nodes = data.split(",")
#         newRoot = TreeNode(int(nodes[0]))
#         q = deque()
#         q.append(newRoot)
#         i = 1
#         while q and i < len(nodes) - 1:
#             curr = q.popleft()
#             if nodes[i] != "#":
#                 left = TreeNode(int(nodes[i]))
#                 curr.left = left
#                 q.append(left)
#             i += 1
#             if nodes[i] != "#":
#                 right = TreeNode(int(nodes[i]))
#                 curr.right = right
#                 q.append(right)
#             i += 1
#         return newRoot
# def inorder_traversal(root):
#     if not root:
#         return
#     inorder_traversal(root.left)
#     print(root.data, end = " ")
#     inorder_traversal(root.right)
# obj = Codec()
# inorder_traversal(node)
# ser = obj.serialize(node)
# des = obj.deserialize(ser)
# print()
# inorder_traversal(des)
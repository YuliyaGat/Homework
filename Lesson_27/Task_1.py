def binary_tree(r):
     return [r, [], []]

def insertLeft(root,newBranch):
     t = root.pop(1)
     if len(t) > 1:
         root.insert(1,[newBranch,t,[]])
     else:
         root.insert(1,[newBranch, [], []])
     return root

def insertRight(root,newBranch):
     t = root.pop(2)
     if len(t) > 1:
         root.insert(2,[newBranch,[],t])
     else:
         root.insert(2,[newBranch, [], []])
     return root

def insertLeftTree(root, NewTree):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [NewTree, t, []])
    else:
        root.insert(1, [NewTree, [], []])
    return root

def insertRightTree(root, NewTree):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [NewTree, [], t])
    else:
        root.insert(2, [NewTree, [], []])
    return root

def deleteSubtree(root, target):
    if root is None:
        return root
    if root[1] and root[1][0] == target[0]:
        root[1] = []
    else:
        root[1] = deleteSubtree(root[1], target)
    if root[2] and root[2][0] == target[0]:
        root[2] = []
    else:
        root[2] = deleteSubtree(root[2], target)
    return root

def get_root_value(root):
     return root[0]

def get_leftChild(root):
     return root[1]

def get_rightChild(root):
     return root[2]

my_tree = binary_tree(3)
insertLeft(my_tree,5)
print(my_tree)
insertLeft(my_tree,10)
print(my_tree)

insertRight(my_tree,4)
print(my_tree)
print(get_rightChild(my_tree))

print(get_leftChild(my_tree))
print(get_leftChild(get_leftChild(my_tree)))
insertRight(get_leftChild(get_leftChild(my_tree)), 23)
print(my_tree)

subtree = binary_tree(1)
insertLeft(subtree, 100)
insertRight(subtree, 200)
insertLeft(get_leftChild(subtree), 300)
print(subtree)

insertLeftTree(get_rightChild(my_tree),subtree)
print(my_tree)

deleteSubtree(my_tree, [200, [], []])
print(my_tree)
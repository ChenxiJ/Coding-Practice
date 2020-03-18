# pay attention that the index ned to go beyond the length of the array, for cases that the last element is a leaf

def decodeHuff(root, s):
    string = ''
    temp_root = root
    for i in range(len(s) + 1):
        if temp_root.left is None and temp_root.right is None:
            string += temp_root.data
            temp_root = root

        if i < len(s):
            if s[i] == '1':
                temp_root = temp_root.right
            elif s[i] == '0':
                temp_root = temp_root.left
    print(string)
# given index of each char, find the longest substring can be kept under the restriction of this char.
def calLength(position, gene):
    occur = len(gene) // 4
    # form the end of the string, keep the last occur of that char, then we can keep length of the string
    length = len(gene) - position[-occur]
    for i in range(occur - 1):
        # then compare all the combination of keeping occur of char from both end, take the maximum length kept
        new = position[i] + 1 + len(gene) - position[-occur + i + 1]
        length = max(length, new)
    return length


def steadyGene(gene):
    # in a steady gene, each char needs to occur exactly n/4 times
    occur = len(gene) // 4
    mapp = {}
    for i in range(len(gene)):
        if gene[i] in mapp:
            mapp[gene[i]].append(i)
        else:
            mapp[gene[i]] = [i]
    length = []
    for i in mapp:
        # char with more occurrence needs to be placed
        if len(mapp[i]) >= occur:
            # find the possible length of the string to keep under restriction of each char exceeds occur
            length.append(calLength(mapp[i], gene))
    lengthToKeep = min(length)
    return len(gene) - lengthToKeep
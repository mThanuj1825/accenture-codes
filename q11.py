input1 = "critical"
input2 = ["typical", "ant", "mental", "political"]
input3 = len(input2)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        t = self.root

        for c in string:
            idx = ord(c) - ord("a")
            if t.children[idx] is None:
                t.children[idx] = TrieNode()

            t = t.children[idx]

        t.isEnd = True

    def searchRhyme(self, string):
        t = self.root
        res = ""

        for c in string:
            idx = ord(c) - ord("a")

            if t.children[idx] is None:
                return self.helper(t, res)

            res += c
            t = t.children[idx]

        return self.helper(t, res)

    def helper(self, node, res):
        if node is None:
            return []

        results = []

        if node.isEnd:
            results.append(res[::-1])

        for i in range(26):
            if node.children[i] is not None:
                results.extend(self.helper(node.children[i], res + chr(ord("a") + i)))

        return results


trie = Trie()
for string in input2:
    trie.insert(string[::-1])

print(trie.searchRhyme(input1[::-1]))

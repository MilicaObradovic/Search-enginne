from parser import Parser

class Node(object):
    def __init__(self, char):
        self._char = char
        self._is_word = False
        self._counter = 0
        self._children = {}

    def __str__(self):
        return self._char

class Trie(object):
    def __init__(self):
        self._root = Node("")

    def insert(self, word):
        node = self._root
        for c in word:
            if c in node._children:
                node = node._children[c]
            else:
                new = Node(c)
                node._children[c] = new
                node = new
        node._is_word = True
        node._counter += 1

    def dfs(self, node, pre):
        if node._is_word:
            self.output.append({"word": (pre+node._char), "number": node._counter})
        
        # for child in node._children.values():
        #     self.dfs(child, pre + node._char)

    def search(self, word):
        node = self._root
        for c in word:
            if c in node._children:
                node = node._children[c]
            else:
                return 0

        self.output = []
        # print(node)
        self.dfs(node, word[:-1])
        dic = {"word": word , "number": 0}
        for i in self.output:
            if i["word"] == word:
                dic["number"] = i["number"]
        return dic

# t.insert("param")
# t.insert("par")
# t.insert("par")
# t.insert("1")
# t.insert("1")
# tt = t.search("1")
# print(tt)

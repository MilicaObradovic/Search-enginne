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
        
        for child in node._children.values():
            self.dfs(child, pre + node._char)

    def search(self, word):
        node = self._root
        for c in word:
            if c in node._children:
                node = node._children[c]
            else:
                return []

        self.output = []
        self.dfs(node, word[:-1])
        lista = []
        for i in self.output:
            if i["word"] == word:
                lista.append(i)
        return lista

# t = Trie("tt", "tt")
# t.insert("param")
# t.insert("par")
# t.insert("par")
# tt = t.search("par")
# print(tt)

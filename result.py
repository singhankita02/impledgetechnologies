from collections import deque
import time

class Node:
    def __init__(self,character = None, isTerminal : bool = False) -> None:
      self.character = character
      self.children = {}
      self.isTerminal = isTerminal

class Handeler:
    def __init__(self) -> None:
        self.root = Node('')
    
    def insert(self,word:str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
        curr.isTerminal=True
    
    def __contains__(self,word:str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isTerminal
    
    def getPrefixes(self,word) -> list:
        prefix = ''
        prefixes = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                return prefixes
            curr = curr.children[char]
            prefix += char
            if curr.isTerminal:
                prefixes.append(prefix)
        return prefixes






class Result:
    def __init__(self) -> None:
      self.handel = Handeler()
      self.queue = deque()

    def buildFile(self,filePath : str = None) -> None:
        try:
            with open(filePath, mode = 'r') as f:
                for line in f:
                    word=line.rstrip('\n')
                    prefixes = self.handel.getPrefixes(word)
                    for prefix in prefixes:
                        self.queue.append((word, word[len(prefix):]))
                    self.handel.insert(word)
        except:
            print('Exception')
            exit(0)
    
    def findLongestCompoundWords(self) -> tuple:
        longest_word = ''
        longest_length = 0
        second_longest = ''
        while self.queue:
            
            word, suffix = self.queue.popleft()
            if suffix in self.handel and len(word) > longest_length:
                second_longest = longest_word
                longest_word = word
                longest_length = len(word)
            else:                                  
                prefixes = self.handel.getPrefixes(suffix)
                for prefix in prefixes:
                    self.queue.append((word, suffix[len(prefix):]))

        return (longest_word,second_longest)

if __name__ == "__main__":
    sol = Result()
    start = time.time()
    sol.buildFile("Input_01.txt")
    first,second = sol.findLongestCompoundWords()
    end = time.time()
    print("Longest Compound Word:",first)
    print("Second Longest Compound Word:",second)
    print("Time taken: ",str(end - start), "seconds")


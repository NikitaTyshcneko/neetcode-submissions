class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        neighbours = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' +word[j+1:]
                neighbours[pattern].append(word)
        
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        count = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' +word[j+1:]
                    for v in neighbours[pattern]:
                        if v not in visited:
                            queue.append(v)
                            visited.add(v)
            
            count += 1

        return 0


        
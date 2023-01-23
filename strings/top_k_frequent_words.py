from heapq import heappop, heapify, heappush

class MyKey:
    def __init__(self, num, word):
        self.num = num
        self.word = word

    def __lt__(self, other):
        return self.num > other.num or (self.num == other.num and self.word < other.word)

class MyKey2:
    def __init__(self, num, word):
        self.num = num
        self.word = word

    def __lt__(self, other):
        return self.num < other.num or (self.num == other.num and self.word > other.word)


def topKFrequent(words, k):
    score = dict()
    for i in range(len(words)):
        if words[i] not in score:
            score[words[i]] = 1
        else:
            score[words[i]] += 1
    heap = []
    heapify(heap)
    for x in score:
        if len(heap) < k:
            heappush(heap, (score[x], x))
        else:
            heap.sort(key=lambda pair: MyKey2(pair[0], pair[1]))
            curr = heappop(heap)
            if curr[0] > score[x] or (curr[0] == score[x] and curr[1] < x):
                heappush(heap, curr)
            else:
                heappush(heap, (score[x], x))
    heap.sort(key=lambda pair: MyKey(pair[0], pair[1]))
    for i in range(len(heap)):
        heap[i] = heap[i][1]
    return heap



# words = ["aaa","aa","a"]
# k = 2

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(topKFrequent(words, k))
# heap = [(1, 'aa'), (1, 'aaa')]
# heap.sort(key=lambda pair: MyKey2(pair[0], pair[1]))
# print(heap)
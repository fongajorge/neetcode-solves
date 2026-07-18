class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count, key=count.get)

        print(list(sorted_count))

        answer = []

        for i in range(k):
            answer.append(list(sorted_count)[-i - 1])

        return answer
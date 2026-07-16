class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = dict()

        for stn in strs:
            current = "".join(sorted(stn))

            if current in hashmap:
                hashmap[current].append(stn)
            else:
                hashmap[current] = [stn]

        answer = []
        
        for element in hashmap.values():
            answer.append(element)

        return answer

            
        
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> answer = new ArrayList<>();

        for (String str : strs) {
            char[] currentChar = str.toCharArray();
            Arrays.sort(currentChar);
            String current = new String(currentChar);

            if(map.containsKey(current)) {
                map.get(current).add(str);
            } else {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(current, list);
            }
        }

        for (List<String> list : map.values()) {
            answer.add(list);
        }

        return answer;
    }
}

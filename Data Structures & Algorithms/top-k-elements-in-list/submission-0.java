class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    // Step 1: count frequencies
    Map<Integer, Integer> count = new HashMap<>();
    for (int n : nums) {
        count.put(n, count.getOrDefault(n, 0) + 1);
    }

    // Step 2: bucket where index = frequency
    List<Integer>[] buckets = new List[nums.length + 1];
    for (int i = 0; i < buckets.length; i++) {
        buckets[i] = new ArrayList<>();
    }
    for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
        int freq = entry.getValue();
        buckets[freq].add(entry.getKey());
    }

    // Step 3: walk from highest frequency down, collecting k elements
    int[] result = new int[k];
    int idx = 0;
    for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
        for (int num : buckets[i]) {
            result[idx] = num;
            idx++;
            if (idx == k) break;
        }
    }
    return result;
}

}

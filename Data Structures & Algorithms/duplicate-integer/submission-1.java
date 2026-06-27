class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap <Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            if(hashmap.containsKey(nums[i])){
                return true;
            } else {
                hashmap.put(nums[i], 1);
            }
        }
        return false;
    }
}
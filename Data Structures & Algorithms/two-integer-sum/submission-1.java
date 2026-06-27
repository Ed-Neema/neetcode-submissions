class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> hashmap = new HashMap<>();
        
        int[] solution = new int [2];

        for(int i=0; i<nums.length; i++){
            if(hashmap.containsKey(target-nums[i])){
                solution[0] = hashmap.get(target-nums[i]);
                solution[1] = i;                
            } else {
                hashmap.put(nums[i],i);
            }
        }
        return solution;
    }
}
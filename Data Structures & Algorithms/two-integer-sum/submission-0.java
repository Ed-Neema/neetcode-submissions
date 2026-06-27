class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        HashMap <Integer, Integer> array_values = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if(array_values.containsKey(target - nums[i])){
                solution[0] = array_values.get(target - nums[i]);
                solution[1] = i; 
            } else {
                array_values.put(nums[i], i);
            }
        }
        return solution;
        
    }
}
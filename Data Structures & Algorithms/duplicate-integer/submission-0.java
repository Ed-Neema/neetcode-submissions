class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap <Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            //need to check if the number already exists. 
            if(map.containsKey(nums[i])){
                return true;
            } else {
                map.put(nums[i], 0);
            }
        }
        return false;
    }
}
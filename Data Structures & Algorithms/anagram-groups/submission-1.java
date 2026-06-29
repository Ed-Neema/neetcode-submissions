class Solution {
    public static String sortString(String toBeSorted){
        char[] chars = toBeSorted.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        return sorted;
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hashmap = new HashMap<>(); 
        for(int i=0; i<strs.length; i++){
            String s = sortString(strs[i]);
            if(hashmap.containsKey(s)){
                List <String> temp =  hashmap.get(s);
                temp.add(strs[i]);
                hashmap.put(s,temp);
            } else{
                List<String> list = new ArrayList<>();
                list.add(strs[i]);
                hashmap.put(s,list);
            }
        }
        return new ArrayList<>(hashmap.values());           
    }
}

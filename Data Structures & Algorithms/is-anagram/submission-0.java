class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hashmapS = new HashMap<>();
        HashMap<Character, Integer> hashmapT = new HashMap<>();

        //quick check
        if(s.length() != t.length()){
            return false;
        }

        for(int i=0; i<s.length(); i++){
            if(hashmapS.containsKey(s.charAt(i))){
                hashmapS.put(s.charAt(i), hashmapS.get(s.charAt(i))+1);
            } else {
                hashmapS.put(s.charAt(i), 1);         
            }
            if(hashmapT.containsKey(t.charAt(i))){
                hashmapT.put(t.charAt(i), hashmapT.get(t.charAt(i))+1);
            } else {
                hashmapT.put(t.charAt(i), 1);         
            }
        }
        
        
        return hashmapS.equals(hashmapT) ? true : false;

    }
}

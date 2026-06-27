class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freq = new int[26];
        if(s.length() != t.length()){
            return false;
        }

        //subtract  "a" from any lowercase letter to normalize it to between 0-25, and increase frequency for that position        

        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }

        for (int count : freq) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] chars = s.toCharArray();
        char[] chars2 = t.toCharArray();
        Arrays.sort(chars);
        Arrays.sort(chars2);

        if (chars.length != chars2.length) {
            return false;
        }
        
        for(int i = 0; i < chars.length; i++){
            if (chars[i] != chars2[i]) {
                return false;
            }
        }
        return true;
    }
}

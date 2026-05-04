class Solution {
    public boolean isAnagram(String s, String t) {

        // 1. check if lengths are the same. if not, they arent anagrams
        // 2. turn both strings into char arrays. 
        // 3. use s as the base
        // 4. if a letter is found, remove it from the second list and continue. if its not found, its not an anagram. keep going until the end of s

        int sLen = s.length();
        int tLen = t.length();

        if (sLen != tLen) {
            return false;
        }

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        boolean found = false;

        for (int i = 0; i < sLen; i++) {

            for (int j = 0; j < tLen; j++) {
                if (tChars[j] == sChars[i]) {
                    tChars[j] = ' ';
                    found = true;
                    break;
                }
            }

            if (!found) {
                return false;
            }
            found = false;
        }

        return true;
    }
}

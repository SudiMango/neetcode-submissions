class Solution {
    public boolean isPalindrome(String s) {
        // Make it into one word all lower case 
        String replaced = s.toLowerCase().replaceAll(" ", "").replaceAll("[^A-Za-z0-9]", "");

        int l = 0;
        int r = replaced.length() - 1;

        while (l < r) {
            if (replaced.charAt(l) == replaced.charAt(r)) {
                l++;
                r--;
            } else {
                return false;
            }
        }

        return true;
    }
}

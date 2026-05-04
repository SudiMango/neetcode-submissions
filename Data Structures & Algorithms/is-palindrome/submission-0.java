class Solution {
    public boolean isPalindrome(String s) {
        String proper = s.replaceAll(" ", "").trim().toLowerCase();
        char[] characters = proper.toCharArray();
        List<Character> newCharacters = new ArrayList<>();

        for (char c : characters) {
            if (Character.isLetterOrDigit(c)) {
                newCharacters.add(c);
            }
        }

        char[] backwards = new char[newCharacters.size()];
        char[] forwards = new char[newCharacters.size()];

        int backwardsIndex = 0;
        for (int i = newCharacters.size() - 1; i >= 0; i--) {
            backwards[backwardsIndex] = newCharacters.get(i);
            backwardsIndex++;
        }

        for (int i = 0; i < newCharacters.size(); i++) {
            forwards[i] = newCharacters.get(i);
        }

        String compare = new String(backwards);
        String compare2 = new String(forwards);
        if (compare.equals(compare2)) {
            return true;
        } else {
            return false;
        }
    }
}

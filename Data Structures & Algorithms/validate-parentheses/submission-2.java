class Solution {
    public boolean isValid(String s) {
        char[] sChars = s.toCharArray();
        Stack<Character> tracker = new Stack<>();

        for (Character c : sChars) {
            if (c == '(' || c == '{' || c == '[') {
                tracker.push(c);
            }

            if (c == ')' || c == '}' || c == ']') {
                if (tracker.isEmpty()) {
                    return false;
                }

                if (tracker.peek() == '(' && c == ')') {
                    tracker.pop();
                    continue;
                } else if (c == ')' && tracker.peek() != '(') {
                    return false;
                }

                if (tracker.peek() == '{' && c == '}') {
                    tracker.pop();
                    continue;
                } else if (c == '}' && tracker.peek() != '{') {
                    return false;
                }

                if (tracker.peek() == '[' && c == ']') {
                    tracker.pop();
                    continue;
                } else if (c == ']' && tracker.peek() != '[') {
                    return false;
                }
            }
        }

        return tracker.isEmpty();
    }
}

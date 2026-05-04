class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Checking all rows
        for (int i = 0; i < board.length; i++) {
            List<Character> seen = new ArrayList<>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] != '.') {
                     if (!seen.contains(board[i][j])) {
                        seen.add(board[i][j]);
                    } else {
                        return false;
                    }
                }
            }
        }

        // Checking all cols
        for (int i = 0; i < board.length; i++) {
            List<Character> seen = new ArrayList<>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[j][i] != '.') {
                     if (!seen.contains(board[j][i])) {
                        seen.add(board[j][i]);
                    } else {
                        return false;
                    }
                }
            }
       }

        // Checking 3x3 boxes

        // Row 1
        for (int k = 0; k < 3; k++) {
            List<Character> seen = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                    for (int j =  (3*k); j < 3*(k+1); j++) {
                        if (board[j][i] != '.') {
                            if (!seen.contains(board[j][i])) {
                                seen.add(board[j][i]);
                            } else {
                                return false;
                            }
                        }
                    }
            }
        }

        // Row 2
        for (int k = 0; k < 3; k++) {
            List<Character> seen = new ArrayList<>();
            for (int i = 3; i < 6; i++) {
                    for (int j =  (3*k); j < 3*(k+1); j++) {
                        if (board[j][i] != '.') {
                            if (!seen.contains(board[j][i])) {
                                seen.add(board[j][i]);
                            } else {
                                return false;
                            }
                        }
                    }
            }
        }

         // Row 3
        for (int k = 0; k < 3; k++) {
            List<Character> seen = new ArrayList<>();
            for (int i = 6; i < 9; i++) {
                    for (int j =  (3*k); j < 3*(k+1); j++) {
                        if (board[j][i] != '.') {
                            if (!seen.contains(board[j][i])) {
                                seen.add(board[j][i]);
                            } else {
                                return false;
                            }
                        }
                    }
            }
        }

        return true;
    }
}

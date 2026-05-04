class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int[] ret = new int[2];
        
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers.length; j++) {
                if (i == j) {
                    continue;
                }

                if (numbers[i] != numbers[j] && numbers[i] + numbers[j] == target) {
                    if (numbers[i] < numbers[j]) {
                        ret[0] =  i + 1;
                        ret[1] =  j + 1;
                    } else {
                        ret[0] = j + 1;
                        ret[1] = i + 1;
                    }
                    break;
                }
            }
        }

        return ret;

    }
}

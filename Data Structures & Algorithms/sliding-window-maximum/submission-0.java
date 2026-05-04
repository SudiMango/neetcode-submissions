class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int outSize = nums.length - (k-1);
        int[] outArr = new int[outSize];

        for (int i = 0; i < outSize; i++) {
            int upperBound = i + k;
            int currMax = nums[i];

            for (int j = i+1; j < upperBound; j++) {
                if (nums[j] > currMax) {
                    currMax = nums[j];
                }
            }
            outArr[i] = currMax;
        }

        return outArr;
    }
}

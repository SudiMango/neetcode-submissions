class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numToFreq = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numToFreq.containsKey(nums[i])) {
                int curr = numToFreq.get(nums[i]);
                curr = curr + 1;
                numToFreq.put(nums[i], curr);
            } else {
                numToFreq.put(nums[i], 1);
            }
        }

        int[] ret = new int[k];
        for (int i = 0; i < k; i++) {
            int currHighestNum = -1001;
            int currHighestFreq = 0;

            for (var entrySet : numToFreq.entrySet()) {
                int num = entrySet.getKey();
                int freq = entrySet.getValue();
                if (freq > currHighestFreq) {
                    currHighestFreq = freq;
                    currHighestNum = num;
                }
            }
            ret[i] = currHighestNum;
            numToFreq.remove(currHighestNum);
        }

        return ret;
    }
}

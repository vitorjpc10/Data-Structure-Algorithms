package OneDimensionDynamicProgramming;

import java.util.Arrays;
import java.util.Collections;

public class LongestIncreasingSubsequence {

     public static int lengthOfLIS(int[] nums) {

          if (nums.length <= 1)
               return nums.length;

          int[] dp = new int[nums.length];
          Arrays.fill(dp, 1);

          int max = -1;

          for (int i = 1; i < nums.length; i++) {

               for (int j = 0; j < i; j++) {

                    if (nums[j] < nums[i]) {

                         dp[i] = Math.max(dp[i], dp[j] + 1);
                    }

                    System.out.println(Arrays.toString(dp) + " max:| " + max + "|j:| " + j + " |i:| " + i + "\n"
                              + Arrays.toString(nums));

               }

          }

          return Arrays.stream(dp).max().getAsInt();

     }

     public static void main(String[] args) {

          int[] arg1 = { 0, 1, 0, 3, 2, 3 };
          System.out.println(lengthOfLIS(arg1));

          int[] arg2 = { 10, 9, 2, 5, 3, 7, 101, 18 };
          System.out.println(lengthOfLIS(arg2));

     }

}

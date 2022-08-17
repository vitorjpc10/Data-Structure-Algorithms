package OneDimensionDynamicProgramming;

public class ClimbingStairs {

     public static int stairsCount(int stepsTotal) {

          if (stepsTotal == 0)
               return 0;
          else if (stepsTotal == 1)
               return 1;
          else if (stepsTotal == 2)
               return 2;

          int[] dp = new int[stepsTotal + 1];

          // At 0 steps, 0 possibilities
          dp[0] = 0;

          // At 1 steps, 1 possibilities (1 step)
          dp[1] = 1;

          // At 2 steps, 2 possibilities (2 step & 1 and 1 steps)
          dp[2] = 2;

          for (int i = 3; i < dp.length; i++) {

               dp[i] = dp[i - 1] + dp[i - 2];

          }

          return dp[stepsTotal];

     }

     public static void main(String[] args) {

          System.out.println("total possibilities: " + stairsCount(3));

     }

}

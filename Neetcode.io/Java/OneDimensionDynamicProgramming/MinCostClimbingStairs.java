package OneDimensionDynamicProgramming;

import java.util.Arrays;

public class MinCostClimbingStairs {

     public static int minCost(int[] costArray) {

          if (costArray.length == 1) {
               return costArray[0];
          }

          for (int i = 2; i < costArray.length; i++) {

               costArray[i] += Math.min(costArray[i - 1], costArray[i - 2]);

               System.out.println("dp Array: " + Arrays.toString(costArray) + " i " + i);
          }

          return Math.min(costArray[costArray.length - 1], costArray[costArray.length - 2]);

     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 };
          System.out.println(minCost(arg1));
     }

}

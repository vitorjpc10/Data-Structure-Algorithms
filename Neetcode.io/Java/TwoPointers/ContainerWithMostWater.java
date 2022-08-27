public class ContainerWithMostWater {

     //! https://leetcode.com/problems/container-with-most-water/discuss/1915172/JavaC%2B%2B-Easiest-Explanations

     public static int maxArea(int[] height) {

          int maxArea = 0;

          // edge cases
          if (height.length == 2) {
               return Math.min(height[0], height[1]);
          }

          int leftPointer = 0;
          int rightPointer = height.length - 1;

          while (leftPointer < rightPointer) {

               // Math.min because you don't want the water to Overflow
               // (j-i) so that width is always a positive number
               int currentArea = Math.min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer);

               if (currentArea > maxArea)
                    maxArea = currentArea;

               if (height[leftPointer] < height[rightPointer]) {
                    leftPointer++;
               } else {
                    rightPointer--;
               }

          }

          return maxArea;

     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
          int[] arg2 = { 1, 1 };
          System.out.println(maxArea(arg1));

     }

}

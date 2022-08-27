import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {

     public static List<List<Integer>> threeSum(int[] nums) {

          List<List<Integer>> result = new ArrayList<List<Integer>>();

          Arrays.sort(nums);

          //!Edge Cases
          //* in nums length is < 3 impossible to have addition of 3 elements */
          //* If min > 0, impossible for the addition to reach 0 */
          //* If max < 0, impossible for the addition to reach 0 */
          if(nums.length < 3 || nums[0] > 0 || nums[nums.length - 1] < 0)
               return result;

          // System.out.println(Arrays.toString(nums));

          for (int i = 0; i < nums.length - 2; i++) {

               if(i > 0 && nums[i] == nums[i-1])
                    continue;

               int leftPointer = i + 1;
               int rightPointer = nums.length - 1;

               List<Integer> singleSolution = new ArrayList<Integer>();

               while (leftPointer < rightPointer) {

                    // System.out.println(nums[i] + nums[leftPointer] + nums[rightPointer] == 0);
                    // System.out.println(
                    // "total addition " + String.valueOf(nums[i] + nums[leftPointer] +
                    // nums[rightPointer]));

                    if (nums[i] + nums[leftPointer] + nums[rightPointer] == 0) {
                         singleSolution.add(nums[i]);
                         singleSolution.add(nums[leftPointer]);
                         singleSolution.add(nums[rightPointer]);

                         // System.out.println("single solution " + singleSolution.toString());

                         if (!result.contains(singleSolution))
                              result.add(singleSolution);

                         singleSolution = new ArrayList<Integer>();

                         // System.out.println("result " + result.toString());

                         leftPointer++;
                         continue;
                    }

                    if (nums[i] + nums[leftPointer] + nums[rightPointer] < 0) {

                         leftPointer++;
                    }

                    if (nums[i] + nums[leftPointer] + nums[rightPointer] > 0) {

                         rightPointer--;

                    }

               }

          }

          return result;

     }

     public static void main(String[] args) {

          int[] arg1 = { -1, 0, 1, 2, -1, -4 };
          int[] arg2 = { 0, 1, 1 };

          System.out.println(threeSum(arg1));

     }

}

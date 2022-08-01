import java.util.Arrays;

/**
 * TwoSum
 */
public class TwoSum {

     public static int[] twoSum1(int[] array, int target) {

          int[] result = new int[2];

          for (int i = 0; i < array.length; i++) {

               // By doing "j= i+1", we can skip over some sum checks that were done
               // previously as the two pointers move down the array
               //
               // *This way ensuring unique sum checks as it moves down the array */
               for (int j = i + 1; j < array.length; j++) {

                    if (array[i] + array[j] == target) {
                         result[0] = i;
                         result[1] = j;
                         return result;
                    }

               }

          }

          System.out.println("Unable to find indexes that sum to the given target value");
          return null;

     }

     public static int[] twoSum2(int[] array, int target) {

          int[] result = new int[2];

          for (int i = 0; i < array.length; i++) {

               for (int j = 0; j < array.length; j++) {

                    if (i == j) {
                         continue;
                    }

                    if (array[i] + array[j] == target) {
                         result[0] = i;
                         result[1] = j;
                         return result;
                    }

               }

          }

          System.out.println("Unable to find indexes that sum to the given target value");
          return null;

     }

     public static void main(String[] args) {

          int[] arg1 = { 2, 7, 11, 15 };
          int target1 = 9;

          int[] arg2 = { 3, 2, 4 };
          int target2 = 6;

          int[] arg3 = { 3, 3 };
          int target3 = 6;

          System.out.println(Arrays.toString(twoSum1(arg1, target1)));
          System.out.println(Arrays.toString(twoSum1(arg2, target2)));
          System.out.println(Arrays.toString(twoSum1(arg3, target3)) + "\n\n");

          System.out.println(Arrays.toString(twoSum2(arg1, target1)));
          System.out.println(Arrays.toString(twoSum2(arg2, target2)));
          System.out.println(Arrays.toString(twoSum2(arg3, target3)) + "\n\n");

     }
}
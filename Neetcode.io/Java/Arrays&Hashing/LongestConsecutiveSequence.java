import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LongestConsecutiveSequence {

     public static int longestConsecutive(int[] nums) {

          Set<Integer> set = new HashSet<Integer>();

          for (int num : nums) {

               set.add(num);
          }

          // System.out.println(set.toString());

          List<Integer> list = new ArrayList<Integer>(set);

          Collections.sort(list);

          if (list.size() <= 1) {
               return list.size();
          }

          int largestSum = 0;
          int runningWindowSum = 1;

          // System.out.println(list.toString());

          for (int i = 0; i < list.size() - 1; i++) {


               if (list.get(i + 1) == list.get(i) + 1) {
                    runningWindowSum++;
               } else {

                    runningWindowSum = 1;
               }

               if (largestSum < runningWindowSum)
                    largestSum = runningWindowSum;

          }

          return largestSum;

     }

     public static void main(String[] args) {

          int[] arg1 = { 100, 4, 200, 1, 3, 2 };
          int[] arg2 = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };
          int[] arg3 = { 0, 0 };
          int[] arg4 = { 4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3 };

          System.out.println(longestConsecutive(arg4));

     }
}

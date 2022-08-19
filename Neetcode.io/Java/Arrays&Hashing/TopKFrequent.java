import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

//https://leetcode.com/problems/top-k-frequent-elements/discuss/1927715/Easy-to-Understand-Solution-MaxHeap()

public class TopKFrequent {

     public static int[] topKFrequent(int[] nums, int k) {

          int[] result = new int[k];
          Map<Integer, Integer> map = new HashMap<Integer, Integer>();

          for (int i = 0; i < nums.length; i++) {

               if (!map.containsKey(nums[i]))
                    map.put(nums[i], 1);
               else
                    map.put(nums[i], map.get(nums[i]) + 1);

          }

     //     for (int n : nums) {

     //      map.put(n,map.getOrDefault(n, 0) + 1);
          
     //     }

          System.out.println(map.toString());

          for (int i = 0; i < k; i++) {

               int mostFrequentKey = 0;
               int mostFrequentValue = 0;

               for (Map.Entry<Integer, Integer> entry : map.entrySet()) {

                    // System.out.println("entryKey" + entry.getKey() + " entryValue: " +
                    // entry.getValue());

                    if (entry.getValue() > mostFrequentValue) {

                         mostFrequentKey = entry.getKey();
                         mostFrequentValue = entry.getValue();

                         // System.out.println("mostFrequentKey " + +entry.getKey());
                    }

               }

               result[i] = mostFrequentKey;
               map.remove(mostFrequentKey);

          }

          return result;

     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 1, 1, 2, 2, 3 };

          System.out.println(Arrays.toString(topKFrequent(arg1, 2)));

     }
}

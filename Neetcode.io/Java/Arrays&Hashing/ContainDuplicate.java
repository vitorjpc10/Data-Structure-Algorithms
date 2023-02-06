import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ContainDuplicate {

     public boolean containsDuplicate(int[] nums) {
          // Create a HashSet to store the elements in the array
          Set<Integer> set = new HashSet<>();

          // Iterate through each element in the array
          for (int num : nums) {
               // Check if the set already contains the current element
               if (set.contains(num)) {
                    // If it does, it means that the element has appeared at least twice in the
                    // array, so return true
                    return true;
               }
               // If not, add the element to the set
               set.add(num);
          }
          // If all elements in the array are distinct, return false
          return false;
     }

     public static boolean containDuplicate2(int[] num) {

          int firstPointer = 0;

          for (int i = 0; i < num.length; i++) {

               for (int j = firstPointer + 1; j < num.length; j++) {

                    int point1 = num[firstPointer];
                    int point2 = num[j];

                    if (num[firstPointer] == num[j]) {
                         return true;
                    }

               }

               firstPointer++;

          }

          return false;

     }

     public static void main(String[] args) {

          int[] num1 = { 1, 2, 3, 4 };
          int[] num2 = { 2, 1, 3, 4, 5, 1 };

          System.out.println(containsDuplicate(num1));
          System.out.println(containsDuplicate(num2));

          System.out.println(containDuplicate2(num1));
          System.out.println(containDuplicate2(num2));
     }
}
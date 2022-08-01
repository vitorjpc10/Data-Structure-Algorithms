import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ContainDuplicate {

     public static boolean containDuplicate(int[] num) {

          Set<Integer> set = new HashSet<Integer>();

          for (Integer integer : num) {

               set.add(Integer.valueOf(integer));
          }

          return !(set.size() == (num.length));
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

          System.out.println(containDuplicate(num1));
          System.out.println(containDuplicate(num2));

          System.out.println(containDuplicate2(num1));
          System.out.println(containDuplicate2(num2));
     }
}
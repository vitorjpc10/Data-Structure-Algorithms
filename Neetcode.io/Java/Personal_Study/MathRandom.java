import java.util.Arrays;
import java.util.Random;

public class MathRandom {
     public static void main(String[] args) {

          int[] array = new int[10];

          for (int i = 0; i < array.length; i++) {

               // generates numbers from 1 to 11
               array[i] = (int) (Math.random() * 11) + 1;
          }

          System.out.println(Arrays.toString(array));
     }

}

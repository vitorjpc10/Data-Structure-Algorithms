package SortingAlgorithms;

import java.util.Arrays;

public class BubbleSort {

     public static int[] bubbleSort1(int[] array) {

          boolean sorted = false;

          while (!sorted) {

               int swapNumber = 0;

               for (int i = 0; i < array.length - 1; i++) {

                    if (array[i + 1] < array[i]) {
                         swapNumber++;

                         int temp = array[i + 1];
                         array[i + 1] = array[i];
                         array[i] = temp;
                    }

               }

               System.out.println(Arrays.toString(array));
               System.out.println("Swap Number total: " + swapNumber + "\n");

               if (swapNumber > 0) {
                    sorted = false;
               } else {
                    sorted = true;
               }

          }

          return array;

     }

     public static void main(String[] args) {

          int[] arg1 = { 5, 1, 4, 2, 8 };

          System.out.println("final sort: " + Arrays.toString(bubbleSort1(arg1)));

     }

}

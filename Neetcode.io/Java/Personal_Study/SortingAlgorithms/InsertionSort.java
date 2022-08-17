package SortingAlgorithms;

import java.util.Arrays;

public class InsertionSort {

     public static void insertionSort1(int[] array) {

          for (int i = 1; i < array.length; i++) {

               // Pointer1 is the pointer to the first element and Pointer2 is the pointer of
               // the next element being compared
               int pointer1 = i - 1;
               int keyValue = array[i];

               System.out.println("Pointer1 index : " + pointer1 + " keyValue : " + keyValue + "\n"
                         + Arrays.toString(array));

               // while pointer1 is not out of bounds AND the value at index pointer1 is >
               // pointer2
               while ((pointer1 > -1) && (array[pointer1] > keyValue)) {
                    array[pointer1 + 1] = array[pointer1];
                    pointer1--;
                    System.out.println("SWAP Pointer1 index : " + pointer1 + " keyValue : " + keyValue + "\n"
                              + Arrays.toString(array));

               }

               array[pointer1 + 1] = keyValue;
               System.out.println("INSERT Pointer1 index : " + pointer1 + " keyValue : " + keyValue + "\n"
                         + Arrays.toString(array));

          }

     }

     public static void main(String[] args) {

          InsertionSort obj = new InsertionSort();

          int[] arg1 = { 12, 11, 13, 5, 6 };
          insertionSort1(arg1);

          System.out.println(Arrays.toString(arg1));

     }
}

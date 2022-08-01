package SortingAlgorithms;

import java.util.Arrays;

public class SelectionSort {

     public static int[] selectSort(int[] array) {

          int min = array[0];
          int minIndex = 0;

          for (int i = 0; i < array.length; i++) {

               for (int j = i + 1; j < array.length; j++) {

                    if (array[j] < array[i]) {

                         min = array[j];
                         array[j] = array[i];
                         array[i] = min;

                         System.out.println(Arrays.toString(array));

                    }

               }

          }

          return array;

     }

     public static int[] selectSort2(int[] arr) {

          for (int i = 0; i < arr.length - 1; i++) {

               int lowIndex = i;

               for (int j = i + 1; j < arr.length; j++) {

                    // int ivalue = arr[i];
                    // int jvalue = arr[j];

                    if (arr[j] < arr[lowIndex]) {
                         lowIndex = j;// searching for lowest index
                    }
               }

               System.out.println("Index of min is: " + lowIndex);

               int smallestValue = arr[lowIndex];
               arr[lowIndex] = arr[i];
               arr[i] = smallestValue;

               System.out.println("current array: " + Arrays.toString(arr));

          }

          return arr;

     }

     public static void main(String[] args) {

          int[] arr = { 64, 25, 12, 22, 11 };

          System.out.println(Arrays.toString(selectSort2(arr)));

     }

}

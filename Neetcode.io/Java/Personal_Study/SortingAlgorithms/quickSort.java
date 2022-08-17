package SortingAlgorithms;

import java.util.Arrays;

public class quickSort {

     public static void quickSort(int[] array, int lowIndex, int highIndex) {

          if (lowIndex >= highIndex) {
               return;
          }

          int pivotIndex = highIndex;

          int leftPointer = lowIndex;
          int rightPointer = highIndex;

          while (leftPointer < rightPointer) {

               while (array[leftPointer] <= pivotIndex && leftPointer < rightPointer) {
                    leftPointer++;
               }

               while (array[rightPointer] >= pivotIndex && rightPointer > leftPointer) {
                    rightPointer--;
               }

               // Swap left and right pointers
               int temp = array[leftPointer];
               array[leftPointer] = array[rightPointer];
               array[rightPointer] = temp;

          }

          // given that left and right pointers are equal, swap left pointer and pivot
          int temp = array[leftPointer];
          array[leftPointer] = array[pivotIndex];
          array[pivotIndex] = temp;

          quickSort(array, lowIndex, leftPointer - 1);
          quickSort(array, rightPointer + 1, highIndex);

     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 5, 2, 6, 8, 45, 3, 5, 8, 4, 9, 6 };
          System.out.println("Before: " + Arrays.toString(arg1));

          quickSort(arg1, 0, arg1.length - 1);
          System.out.println("After: " + Arrays.toString(arg1));

     }

}

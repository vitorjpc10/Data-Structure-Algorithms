package CompanyProblems;

import java.util.Arrays;
import java.util.Collections;

// https://www.educative.io/blog/crack-amazon-coding-interview-questions

public class AmazonTestProblems {

     // problem 1
     public static int findMissingNumbers(int[] array) {

          int totalSum = 0;


          for (int i = 0; i < array.length + 2; i++) {

               

               totalSum += i;
          }

          int partialSum = 0;

          for (int element : array) {

               partialSum += element;

          }

          return totalSum - partialSum;

     }

     public static void main(String[] args) {

          int[] arg1 = { 3, 7, 1, 2, 8, 4, 5 };
          System.out.println(findMissingNumbers(arg1));

     }
}

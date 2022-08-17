package CompanyProblems;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class WalmartCodeTest1 {

     /**
      * Write code to merge two arrays and sort in non-descending order.
      * Write code to display all the characters occuring in a string.
      * How do you find the occurence of each character?
      * Write SQL to display maximum salaries by department.
      * 
      * 
      */

     // Write code to merge two arrays and sort in non-descending order.
     public static int[] mergeAndSort(int[] a, int[] b) {

          int[] array = new int[a.length + b.length];

          int arrayHead = -1;

          for (int i : a) {

               arrayHead++;
               array[arrayHead] = i;

          }

          for (int i : b) {

               arrayHead++;
               array[arrayHead] = i;

          }

          for (int i = 0; i < array.length - 1; i++) {

               int greatestIndex = i;

               for (int j = i + 1; j < array.length; j++) {

                    if (array[j] >= array[greatestIndex]) {
                         greatestIndex = j;
                    }

               }

               int temp = array[greatestIndex];
               array[greatestIndex] = array[i];
               array[i] = temp;

          }

          return array;
     }

     // Write code to display all the characters occuring in a string.
     public static void charDisplay(String string) {

          HashSet<Character> chars = new HashSet<Character>();

          char[] array = string.toCharArray();

          for (char c : array) {

               chars.add(c);
          }

          System.out.println(chars.toString());

     }

     // How do you find the occurence of each character?
     public static void charOccurance(String string) {

          HashMap<Character, Integer> map = new HashMap<Character, Integer>();

          char[] array = string.toCharArray();

          for (char c : array) {

               if (map.containsKey(c) == false) {
                    map.put(c, 1);
               } else {
                    map.put(c, map.get(c) + 1);
               }

          }

          System.out.println(map.toString());

     }

     // maximum subarray
     public static int maxSubArray(int[] nums) {

          int maximumSubArraySum = Integer.MIN_VALUE;
          int start = 0;
          int end = 0;

          for (int left = 0; left < nums.length; left++) {

               int runningWindowSum = 0;

               for (int right = left; right < nums.length; right++) {
                    runningWindowSum += nums[right];

                    if (runningWindowSum > maximumSubArraySum) {
                         maximumSubArraySum = runningWindowSum;
                         start = left;
                         end = right;
                    }
               }
          }

          System.out.println("start: " + start + " end: " + end);
          return maximumSubArraySum;

     }

     // 3Sum, find triplets that sum to a specific numbers
     public static boolean sumTriplets(int[] array, int target) {

          for (int i = 0; i < array.length - 2; i++) {

               for (int j = 0; j < array.length - 1; j++) {

                    for (int k = 0; k < array.length; k++) {

                         if (array[i] + array[j] + array[k] == target) {
                              System.out.print("Triplet is " + array[i] + ", " + array[j] + ", " + array[k]
                                        + " target is: " + target);
                              return true;
                         }

                    }

               }

          }

          return false;
     }

     // what is the min number of coins that can be used from a given coin array to
     // reach the given amount
     public static int coinCount(int[] coinArray, int amount) {

          // create a dp array and fill it with values where total coin amount is
          // unaccessible
          int[] dp = new int[amount + 1];
          Arrays.fill(dp, amount + 1);

          // if amount is 0 = there are 0 coins that would result in the min of the amount
          dp[0] = 0;

          for (int i = 0; i < amount + 1; i++) {

               for (int j = 0; j < coinArray.length; j++) {

                    // If the coin we are looking at fits (is <=) to the amount value of i
                    if (coinArray[j] <= i) {

                         // * */ insert at dp[i] the smallest value of whatever was already there OR 1+
                         // (+1
                         // given you are considering that coinDenomitation at hand) the value at dp[i] -
                         // the coin demonitation you are looking at
                         // * */ This way if there is the possibility that only 1 coin is needed to meet
                         // the amount requested then it returns that

                         dp[i] = Math.min(dp[i], 1 + dp[i - coinArray[j]]);
                         // System.out.println(Arrays.toString(dp));
                    }

               }

          }

          if (dp[amount] > amount) {
               return -1;
          } else {
               return dp[amount];
          }
     }

     public static boolean areBracketsBalanced(String bracketString) {

          char[] bracketArray = bracketString.toCharArray();

          Stack<Character> stack = new Stack<Character>();

          for (char c : bracketArray) {

               if (c == '[' || c == '{' || c == '(') {

                    stack.push(c);

               }

               if (stack.isEmpty()) {
                    System.out.println("Stack is empty... No opening bracket found in stack");
                    return false;
               }

               switch (c) {
                    case ']':

                         if (stack.pop() != '[') {
                              return false;
                         }
                         break;

                    case '}':

                         if (stack.pop() != '{') {
                              return false;
                         }
                         break;

                    case ')':

                         if (stack.pop() != '(') {
                              return false;
                         }
                         break;

                    default:
                         break;
               }

          }

          if (!stack.isEmpty()) {
               System.out.println("Stack is not empty");
               return false;
          } else
               return true;

     }

     public static int validPalindrome(String string) {

          int count = 0;

          for (int i = 0; i < string.length(); i++) {

               // For odd length palindromes
               count += (findPalindrome(string, i, i));

               // for even length palindromes
               count += (findPalindrome(string, i, i + 1));
          }

          return count;

     }

     public static int findPalindrome(String string, int lowIndex, int highIndex) {

          int count = 0;

          while (lowIndex >= 0 && highIndex < string.length() && string.charAt(lowIndex) == string.charAt(highIndex)) {

               count++;
               lowIndex--;
               highIndex++;

          }

          return count;

     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 3, 5, 5, 7 };
          int[] arg2 = { 1, 2, 6, 4, 5, 8 };

          System.out.println(Arrays.toString(mergeAndSort(arg1, arg2)));

          String arg3 = "potatosdshrsjdfjbaaa";

          charDisplay(arg3);

          charOccurance(arg3);

          int[] arg4 = { -3, 1, -8, 4, -1, 2, 1, -5, 5 };
          System.out.println("max subarray total: " + maxSubArray(arg4));

          int[] arg5 = { 1, 4, 45, 6, 10, 8 };
          sumTriplets(arg5, 22);

          System.out.println("\nremainder is: " + 10 % 11);

          int[] arg6 = { 1, 2, 5 };

          System.out.println("minimum amount of coins: " + coinCount(arg6, 11));

          String arg7 = "(([{}]))";

          System.out.println("Is balanced: " + areBracketsBalanced(arg7));

          String arg8 = "abc";
          System.out.println(validPalindrome(arg8));

     }

}

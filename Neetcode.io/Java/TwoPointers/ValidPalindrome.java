import java.util.Arrays;

public class ValidPalindrome {

     public static boolean isValidPalindrome(String input) {

          // todo: Converting to lowercase
          input = input.toLowerCase();
          // System.out.println("To Lowercase: " + input);

          // todo: Removing non-alphanumeric characters
          input = input.replaceAll("[^a-zA-Z0-9]", "");
          // System.out.println("Removed all non-alphanumeric characters: " + input);

          // ! An empty string is considered a Palindrome
          if (input.length() == 0)
               return true;

          char[] inputArray = input.toCharArray();

          // System.out.println("Value of char array is: " + String.valueOf(inputArray));
          // System.out.println("Value of char array is: " + Arrays.toString(inputArray));

          int endPos = inputArray.length - 1;

          for (int i = 0; i < inputArray.length; i++) {

               if (inputArray[i] != inputArray[endPos])
                    return false;

               if (i > inputArray.length / 2)
                    break;

               endPos--;

          }

          return true;
     }

     public static void main(String[] args) {

          String arg1 = "A man, a plan, a canal: Panama";
          String arg2 = "race a car";
          String arg3 = " ";

          System.out.println(arg1 + " : " + isValidPalindrome(arg1));
          System.out.println(arg2 + " : " + isValidPalindrome(arg2));
          System.out.println(arg3 + " : " + isValidPalindrome(arg3));

     }

}

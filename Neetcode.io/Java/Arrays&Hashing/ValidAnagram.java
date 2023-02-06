import java.util.Arrays;

public class ValidAnagram {

     public static boolean isAnagram1(String arg1, String arg2) throws Exception {

          if (arg1.length() != arg2.length()) {
               throw new Exception("String input arguments to not match in length");
          }

          for (int i = 0; i < arg1.length(); i++) {

               // Making copies so that the replace() won't use arg1 and arg2 destructively
               String copyArg1 = arg1;
               String copyArg2 = arg2;

               char queryChar = arg1.charAt(i);

               int instancesOfChar1 = copyArg1.length() - copyArg1.replace(Character.toString(queryChar), "").length();
               int instancesOfChar2 = copyArg2.length() - copyArg2.replace(Character.toString(queryChar), "").length();

               if (instancesOfChar1 != instancesOfChar2) {
                    return false;
               }

          }

          return true;
     }

     public static boolean isAnagram2(String arg1, String arg2) throws Exception {

          if (arg1.length() != arg2.length()) {
               throw new Exception("String input arguments to not match in length");
          }

          for (int i = 0; i < arg1.length(); i++) {

               int charCount1 = 0;
               int charCount2 = 0;

               for (int j = 0; j < arg1.length(); j++) {

                    if (Character.toString(arg1.charAt(i)).equals(Character.toString(arg1.charAt(j)))) {
                         // System.out.println(
                         // Character.toString(arg1.charAt(i)) + " and " +
                         // Character.toString(arg1.charAt(j)));
                         charCount1++;
                    }

                    if (Character.toString(arg1.charAt(i)).equals(Character.toString(arg2.charAt(j)))) {
                         // System.out.println(
                         // Character.toString(arg2.charAt(i)) + " and " +
                         // Character.toString(arg2.charAt(j)));
                         charCount2++;
                    }

               }

               if (charCount1 != charCount2) {
                    return false;
               }

          }

          return true;

     }

     public static boolean isAnagram3(String s, String t) {
          // If the lengths of the strings are not equal, they cannot be anagrams
          if (s.length() != t.length()) {
              return false;
          }
          
          // Sort both strings
          char[] sChars = s.toCharArray();
          char[] tChars = t.toCharArray();
          Arrays.sort(sChars);
          Arrays.sort(tChars);
          
          // Compare the sorted strings, if they are not equal, the strings are not anagrams
          return Arrays.equals(sChars, tChars);
      }

     public static void main(String[] args) throws Exception {

          System.out.println("1a: " + isAnagram1("cat", "rat"));
          System.out.println("2a: " + isAnagram1("anagram", "nagaram"));

          System.out.println("1b: " + isAnagram2("cat", "rat"));
          System.out.println("2b: " + isAnagram2("anagram", "nagaram"));

          System.out.println("3b: " + isAnagram3("cat", "rat"));
          System.out.println("3b: " + isAnagram3("anagram", "nagaram"));

     }

}

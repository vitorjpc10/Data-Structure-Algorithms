package Stack;

import java.util.Stack;

public class ValidParentheses {

     public static boolean isValid(String s) {

          // edge case: if string is null or empty
          if (s == null || s.length() == 0)
               return false;

          char[] array = s.toCharArray();
          Stack<Character> stack = new Stack<Character>();

          for (char c : array) {

               if (c == '(' || c == '{' || c == '[') {
                    stack.push(c);
                    continue;
               }

               if (c == ')' || c == '}' || c == ']') {

                    char topStack;

                    // if extra closing brackets
                    if (stack.isEmpty())
                         return false;
                    else {
                         topStack = stack.pop();
                    }

                    switch (c) {

                         case ')':

                              if (topStack != '(')
                                   return false;
                              continue;

                         case '}':

                              if (topStack != '{')
                                   return false;
                              continue;

                         case ']':

                              if (topStack != '[')
                                   return false;
                              continue;

                         default:
                              continue;

                    }
               }

               System.out.println(stack.toString());

          }

          // if extra opening brackets
          if (!stack.isEmpty())
               return false;

          return true;
     }

     public static void main(String[] args) {

          String arg1 = "[{()}]";

          System.out.println(isValid(arg1));

     }
}

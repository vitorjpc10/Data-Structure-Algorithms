import java.util.Arrays;

public class StackImp {

     private int[] arr;
     private int top;

     // Constructor to initialize the stack
     StackImp(int size) {
          arr = new int[size];
          top = -1;
     }

     // Utility function to add an element `x` to the stack
     public void push(int x) {
          if (isFull()) {
               System.out.println("Overflow\nProgram Terminated\n");
               System.exit(-1);
          }

          System.out.println("Inserting " + x);
          arr[++top] = x;
     }

     // Utility function to pop a top element from the stack
     public int pop() {
          // check for stack underflow
          if (isEmpty()) {
               System.out.println("Underflow\nProgram Terminated");
               System.exit(-1);
          }

          System.out.println("Removing " + peek());

          // decrease stack size by 1 and (optionally) return the popped element
          arr[top] = 0;
          return arr[top--];
     }

     // Utility function to return the top element of the stack
     public String peek() {
          if (!isEmpty()) {
               return "Top Element on Stack: " + arr[top];
          } else {
               System.exit(-1);
               return "Stack is empty";
          }

     }

     // Utility function to return the size of the stack
     public int size() {
          return top + 1;
     }

     // Utility function to check if the stack is empty or not
     public boolean isEmpty() {
          return top == -1; // or return size() == 0;
     }

     // Utility function to check if the stack is full or not
     public boolean isFull() {
          return top == arr.length - 1; // or return size() == capacity;
     }

     public String getStack() {

          return Arrays.toString(arr);

     }

     public static void main(String[] args) {

          StackImp obj = new StackImp(5);
          System.out.println(obj.getStack());

          obj.push(1);
          System.out.println(obj.getStack());
          obj.push(3);
          System.out.println(obj.getStack());

          System.out.println(obj.peek());

          obj.pop();

          System.out.println(obj.peek());

          System.out.println(obj.getStack());

          obj.push(1);
          obj.push(1);
          obj.push(1);
          obj.push(1);
          System.out.println(obj.getStack());
          System.out.println("Full Stack: " + obj.isFull());

     }
}

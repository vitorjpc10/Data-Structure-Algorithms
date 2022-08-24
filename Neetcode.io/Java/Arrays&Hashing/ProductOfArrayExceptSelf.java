import java.util.Arrays;

public class ProductOfArrayExceptSelf {

     public static int[] productExceptSelf(int[] nums) {

          int[] result = new int[nums.length];

          for (int i = 0; i < nums.length; i++) {

               int leftPointer = i - 1;
               int rightPointer = i + 1;

               int totalProduct = 1;
               int leftProduct = 1;
               int rightProduct = 1;

               while (leftPointer >= 0 || rightPointer <= nums.length - 1) {

                    // System.out.println("leftPointer " + leftPointer + " rightPointer " +
                    // rightPointer);

                    if (leftPointer >= 0) {
                         leftProduct = nums[leftPointer] * leftProduct;
                         leftPointer--;
                    }

                    if (rightPointer <= nums.length - 1) {
                         rightProduct = nums[rightPointer] * rightProduct;
                         rightPointer++;
                    }

                    // System.out.println("i: " + i + " rightPointer: " + rightPointer + "
                    // leftPointer: " + leftPointer
                    // + " rightProduct: " + rightProduct + " leftProduct: " + leftProduct);
                    // System.out.println(Arrays.toString(nums));

               }

               totalProduct = leftProduct * rightProduct;
               result[i] = totalProduct;
               // System.out.println("\n Result array: " + Arrays.toString(result));

          }

          return result;
     }

     public static int[] productExceptSelf2(int[] nums) {
          int N = nums.length;

          int[] left_products = new int[N];
          int[] right_products = new int[N];

          int[] output_arr = new int[N];

          left_products[0] = 1;
          right_products[N - 1] = 1;

          for (int i = 1; i < N; i++) {
               left_products[i] = nums[i - 1] * left_products[i - 1];
          }

          for (int i = N - 2; i >= 0; i--) {
               right_products[i] = nums[i + 1] * right_products[i + 1];
          }

          for (int i = 0; i < N; i++) {
               output_arr[i] = left_products[i] * right_products[i];
          }

          return output_arr;
     }

     public static void main(String[] args) {

          int[] arg1 = { 1, 2, 3, 4 };
          System.out.println(Arrays.toString(productExceptSelf2(arg1)));

     }

}

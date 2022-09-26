package SlindingWindow;

import java.util.Arrays;
import java.util.Collections;

public class BestTimeToBuyAndSellStocks {

     public static int maxProfit(int[] prices) {

          if (prices == null || prices.length == 0)
               return 0;

          int minStockPrice = Integer.MAX_VALUE;
          int maxDiff = 0;

          for (int i = 0; i < prices.length; i++) {

               int profit = prices[i] - minStockPrice;

               maxDiff = Math.max(profit, maxDiff);

               minStockPrice = Math.min(minStockPrice, prices[i]);
          }
          return maxDiff;

     }

     public static void main(String[] args) {

          int[] arg1 = { 7, 1, 5, 3, 6, 4 };
          int[] arg2 = { 7, 6, 4, 3, 1 };

          System.out.println(maxProfit(arg1));

     }

}

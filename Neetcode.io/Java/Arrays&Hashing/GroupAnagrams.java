import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagrams {

     public static List<List<String>> groupAnagrams(String[] strs) {

          List<List<String>> result = new ArrayList<List<String>>();

          if (strs.length == 0 || strs == null) {
               return result;
          } else if (strs.length == 1) {
               List<String> list = new ArrayList<String>();
               list.add(strs[0]);
               result.add(list);
               return result;
          }

          Map<String, List<String>> map = new HashMap<String, List<String>>();

          for (String word : strs) {

               char[] array = word.toCharArray();
               Arrays.sort(array);

               String key = String.valueOf(array);

               if (!map.containsKey(key))
                    map.put(key, new ArrayList<>());

               map.get(key).add(word);

               

          }

          // ! all of this can be achieved with the below return statement
          // for (Map.Entry<String, List<String>> entry : map.entrySet()) {

          // result.add(entry.getValue());

          // }

          // return result;

          return new ArrayList<>(map.values());

     }

     public static void main(String[] args) {

          String[] arg1 = { "eat", "tea", "tan", "ate", "nat", "bat" };

          System.out.println(groupAnagrams(arg1).toString());

     }

}

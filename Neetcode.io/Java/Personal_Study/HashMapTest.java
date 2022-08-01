import java.util.HashMap;

public class HashMapTest {

     public static HashMap<Integer, Integer> add3Dummy() {

          HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();

          for (int i = 0; i < 3; i++) {

               result.put(i, i * 2);

          }

          return result;
     }

     public static void main(String[] args) {

          HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

          map = add3Dummy();

          // Reading all of the hashmap
          System.out.println(map);

          // reading all keys
          System.out.println(map.keySet());

          // reading all values
          System.out.println(map.values());

          // Replacing all values from hashmap with new values
          for (Integer key : map.keySet()) {

               map.replace(key, map.get(key) * 3);
          }
          System.out.println(map);

          System.out.println(map.entrySet());

          map.replace(1, 2);

          for (Integer key : map.keySet()) {

               boolean condition = false;

               if (map.get(key) > 3) {
                    condition = true;
                    System.out.println("Is value > 3 for key " + key + " : " + condition);
               } else {
                    System.out.println("Is value > 3 for key " + key + " : " + condition);
               }

          }

     }

}

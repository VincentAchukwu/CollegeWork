import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class MakeMap{


    public static Map<String, Integer> makeMap(Scanner s){

        Map<String, Integer> map = new HashMap<>();
        while(s.hasNext()){
            String input = s.nextLine();
            String [] lst = input.split(" ");
            String name = lst[0];
            int num = Integer.parseInt(lst[1]);
            map.put(name, num);
        }
        return map;
    }

   public static void main(String [] args)
   {
      Map<String, Integer> map = MakeMap.makeMap(new Scanner(System.in));

      List<String> names = new ArrayList<String>(map.keySet());
      Collections.sort(names);
      for(String name : names)
         System.out.println(name + " has number " + map.get(name));
   }
}
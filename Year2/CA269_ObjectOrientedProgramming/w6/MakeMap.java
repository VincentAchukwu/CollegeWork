import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class MakeMap
{
    // No main method required.
    public static Map<String, Integer> makeMap(Scanner in){

        Map<String, Integer> map = new HashMap<>();
        // List<String> names = new ArrayList<>();
        while(in.hasNext()){
            String input = in.nextLine();
            String [] lst = input.split(" ");
            String name = lst[0];
            int mark = Integer.parseInt(lst[1]);
            map.put(name, mark);
        }
        return map;
    }

   public static void main(String [] args)
   {
        Map<String, Integer> students = MakeMap.makeMap(new Scanner(System.in));
        List<String> names = new ArrayList<String>(students.keySet());
        Collections.sort(names);
        for(String name : names)
            System.out.println(name + " has mark " + students.get(name));
   }
}
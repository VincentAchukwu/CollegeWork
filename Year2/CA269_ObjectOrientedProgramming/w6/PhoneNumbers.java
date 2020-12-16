import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class PhoneNumbers
{
    public static void main(String [] args)
    {
        System.out.println("Enter a name and number, or a name and ? to query (!! to exit)");
        
        Map<String,String> phoneNums = new HashMap<>();
        
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();
        while(!input.equals("!!")){
            
            String [] info = input.split(" ");
            String name = info[0];
            String query = info[1];
            
            if(!query.equals("?")){
                phoneNums.put(name, query);
            }
            if(phoneNums.containsKey(name) && (query.equals("?"))) {
                System.out.printf("%s has number %s\n", name, phoneNums.get(name));
            }
            else if(!phoneNums.containsKey(name) && query.equals("?")){
                System.out.printf("Sorry, there is no %s\n", name);
            }
            input = in.nextLine();
        }
        System.out.println("Bye");
    }
}
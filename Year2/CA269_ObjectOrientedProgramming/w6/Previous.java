import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Previous
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter some numbers (-1 to end)");
        Set<Integer> numset = new HashSet<Integer>();
        int num = in.nextInt();
        System.out.println("Previous:");
        while(num != -1){
            if(numset.add(num) == false){
                System.out.println(num);
            }
            num = in.nextInt();
        }
        
    }
}
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class ListSort
{
    public static void main(String [] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter numbers: ");
        List<Integer> numlist = new ArrayList<Integer>();
        int num = in.nextInt();
        while(num != -1){
            numlist.add(num);
            num = in.nextInt();
        }
        Collections.sort(numlist);
        System.out.println("Sorted: " + numlist);
    }
}
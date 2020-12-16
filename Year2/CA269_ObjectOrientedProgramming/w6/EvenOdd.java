import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class EvenOdd{
    
    public static void main(String [] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter numbers: ");
        List<Integer> odds = new ArrayList<Integer>();
        List<Integer> evens = new ArrayList<Integer>();
        int num = in.nextInt();
        while(num != -1){
            // int num = in.nextInt();
            if(num%2 == 1){
                odds.add(num);
            }
            else{
                evens.add(num);
            }
            num = in.nextInt();
        }
        System.out.println("Odd:");
        for(int odd:odds){
            System.out.print(" " + odd);
        }
        System.out.println();
        System.out.println("Even:");
        for(int even:evens){
            System.out.print(" " + even);
        }
    }
}
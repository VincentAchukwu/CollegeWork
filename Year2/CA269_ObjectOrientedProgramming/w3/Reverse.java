import java.util.Scanner;

public class Reverse
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.print("How many numbers: ");
        // Read in the numbers
        int nums =  in.nextInt();

        int[] lst = new int[nums];
        System.out.printf("Enter %d numbers: ", nums);
        for(int i = 0; i < nums; i++){
            int values = in.nextInt();
            lst[i] = values;
        }
        // reverse the numbers
        int[] reversed = new int[nums];
        for(int i = 0; i < lst.length; i++){
            reversed[i] = lst[lst.length - i - 1];
        }
        
        // print them out
        System.out.print("The numbers reversed are:");
        for(int num = 0; num < lst.length; num++){
            System.out.print(" " + reversed[num]);
        }
        
        System.out.println();
    }
}
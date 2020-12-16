/*
    This code is supplied and may be used to solve this problem.
    
    Note that the output matching is exact (down to spaces and newlines)
    It will be easier to get full marks if you use the supplied 
    System.out.print statements
*/
import java.util.Scanner;

public class StringReproduction
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter an integer and a string: ");
        // Read in the number ... 
        int num = in.nextInt();
        // ... and the string
        String word = in.next();
        for(int i = 0; i < num; i++){
            System.out.print(word);
        }

        // shorter way:
        // System.out.println(word.repeat(num));

        // work out what to print
        // YOUR CODE HERE
        System.out.println();
    }
}
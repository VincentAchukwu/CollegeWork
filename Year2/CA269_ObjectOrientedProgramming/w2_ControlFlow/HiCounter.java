/*
    This code is supplied and may be used to solve this problem.
    
    Note that the output matching is exact (down to spaces and newlines)
    It will be very difficult to get this correct if you do not use the supplied 
    System.out.print statements
*/
import java.util.Scanner;

public class HiCounter
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a phrase: ");
        // Read in the phrase (actually the whole line)
        String phrase = in.nextLine();
        int count = 0;
        for(int i = 0; i < phrase.length() - 1; i++){
            String sub = phrase.substring(i,i+2);
            if (sub.equals("hi")){
                count++;
            }
        }
        System.out.print(count);

        // count how many times "hi" occurs.
        // YOUR CODE HERE
        System.out.println();
    }
}
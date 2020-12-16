/*
    This code is supplied and may be used to solve this problem.
    
    Note that the output matching is exact (down to spaces and newlines)
    It will be difficult to get this correct if you do not use the supplied 
    System.out.print statements
*/
import java.util.Scanner;

public class FindMatchingLetters
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter two lines:");
        // Read in the two lines
        String line1 = in.nextLine();
        String line2 = in.nextLine();

        int numMatching = 0;

        for(int i = 0; i < line1.length(); i++){
            if(line1.charAt(i) == line2.charAt(i)){
                numMatching ++;
            }
        }
        // Print out the solution
        System.out.println("There are " + numMatching + " corresponding characters.");
    }
}
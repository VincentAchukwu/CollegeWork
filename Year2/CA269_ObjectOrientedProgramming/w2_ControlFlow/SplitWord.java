/*
    This code is supplied and may be used to solve this problem.
*/
import java.util.Scanner;

public class SplitWord
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a word: ");
        // Read in the word
        String word = in.next();
        // int j = 1;
        for(int i = 0; i < word.length() - 1; i++){
            System.out.println(word.substring(i, i + 2));
        }
        //Hello

        // YOUR CODE HERE
        
    }
}
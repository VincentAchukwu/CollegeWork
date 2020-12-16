public class Test
{
    // This method returns a String and receives a String
    public static String firstShallBeLast(String word)
    {
        // Reorganise the string.  Remember the '+' operator concatenates strings.
        // Needs to return the correct string.

        String first = word.substring(0,1);
        String middle = word.substring(1,word.length() - 1);
        String last = word.substring(word.length() - 1);
        return (last + middle + first);
    }

    public static int largest(int a, int b, int c)
    {
        // Write the code to find the largest of these three numbers
        if (a > b && a > c){
            return a;
        }
        else if (b > a && b > c){
            return b;
        }
        return c;
        
        // You will need a return statement to return the largest number
    }
}

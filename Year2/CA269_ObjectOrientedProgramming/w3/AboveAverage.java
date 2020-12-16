import java.util.Scanner;
public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        double [] numbers = new double[num];	// num user enters is our list length
        
        System.out.print("Enter " + num + " numbers: ");
        double sum = 0;
        
        for(int i = 0; i < num; i++){
        	double user_in = in.nextDouble();
        	numbers[i] = user_in;
        	sum += user_in;
        }
        double avg = sum / num;
        // Now read in the numbers
        System.out.println("list " + Arrays.toString(numbers));
        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");
        // You can use the following code to print out one number
        // You may want to put this in a loop.
        for(int nums = 0; nums < numbers.length; nums++){
        	if(numbers[nums] > avg){
		        System.out.print(" " + numbers[nums]);
        	}
        }

        System.out.println(); // Should finish with a new line
    }
}
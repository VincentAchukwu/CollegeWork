import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadNames
{
    public static void main(String [] args) throws FileNotFoundException
    {
        System.out.println("Enter the file name: ");

        Scanner input = new Scanner(System.in);
        String filename = input.next();
        input = new Scanner(new File(filename));

        int numNames = input.nextInt();
        String [] names = new String[numNames];

        for(int i = 0; i < numNames; i++){
            names[i] = input.next();
        }

        System.out.println("The names in reverse order are:");

        for(int i = numNames - 1; i >= 0; i--){
            System.out.print(names[i] + " ");
        }
        System.out.println();
    }
}
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Senti1
{
    public static void main(String [] args)
    {
        if(args.length < 1){
            System.out.println("Usage: java ReadNames <filename>");
        }
        else{
            Scanner file = null;
            try{
                String word = args[0];
                int count = 0;
                file = new Scanner(new File(args[1]));
                while(file.hasNext()){
                    int rating = file.nextInt();
                    String review = file.nextLine();
                    if(review.contains(word)){
                        count++;
                    }
                }
                System.out.printf("The word %s occurs %d times.\n", word, count);
            }
            catch(FileNotFoundException e){
                System.out.println("File not found");
            }
        }
    }
}
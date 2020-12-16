import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Senti2
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
                double rating_sum = 0;
                while(file.hasNext()){
                    int rating = file.nextInt();
                    String review = file.nextLine();
                    if(review.contains(word)){
                        count++;
                        rating_sum += rating;
                    }
                }
                double avg = (rating_sum/count);
                System.out.printf("%s appears %d times.\n", word, count);

                if(count == 0){
                    System.out.printf("The average score of the reviews containing %s is 0.00\n", word);
                }
                else{
                    System.out.printf("The average score of the reviews containing %s is %.02f\n", word, avg);
                }
            }
            catch(FileNotFoundException e){
                System.out.println("File not found");
            }
        }
    }
}
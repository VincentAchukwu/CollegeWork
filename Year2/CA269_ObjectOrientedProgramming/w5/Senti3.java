import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Senti3
{
    public static void main(String [] args)
    {
        if(args.length < 1){
            System.out.println("Usage: java ReadNames <filename>");
        }
        else{
            Scanner wordfile = null;
            Scanner reviewfile = null;
            try{
                wordfile = new Scanner(new File(args[0]));
                String [] word_lst = wordfile.nextLine().split(" ");
                for(String word:word_lst){  // reading through word LIST
                    int count = 0;
                    double rating_sum = 0;
                    reviewfile = new Scanner(new File(args[1]));
                    while(reviewfile.hasNext()){    // reading through review FILE
                        int rating = reviewfile.nextInt();
                        String review = reviewfile.nextLine();
                        String [] rev = review.substring(1).split(" ");
                        for(String w:rev){  // reading through review LIST
                            if(word.equals(w)){
                                count++;
                                rating_sum+=rating;
                                break;
                            }
                        }
                    }
                    double avg = rating_sum/count;
                    if(count == 0){
                        System.out.printf("The score of %s is 0.00.\n", word);
                    }
                    else{
                        System.out.printf("The score of %s is %.2f.\n", word, avg);
                    }
                }
            }
            catch(FileNotFoundException e){
                System.out.println("File not found");
            }
        }
    }
}
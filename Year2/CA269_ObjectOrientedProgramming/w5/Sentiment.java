import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class Sentiment
{
    public static double sentiment(String review, String reviewFilename) throws FileNotFoundException
    {
        double ratingsum = 0;
        int count = 0;
        String [] newReview = review.split(" ");
        for(String word:newReview){
            double check = score(reviewFilename, word);
            if(check < 1.8 || check > 2.2){
                if(check != -1){
                    ratingsum += check;
                    count++;
                }
            }
        }
        if(count == 0){
            return -1;
        }
        return ratingsum/count;
    }

    public static double score(String fileName, String word) throws FileNotFoundException
    {
        Scanner revScanner = new Scanner(new File(fileName));

        double incRating = 0;
        int counter = 0;
        while(revScanner.hasNext()){
            String current_Rev = revScanner.nextLine();
            int rating = Integer.parseInt(current_Rev.substring(0,1));
            if(word.equals(".") || word.equals(",")){
                if(current_Rev.contains(word)){
                    incRating+=rating;
                    counter++;
                }
            }
            else{
                if(contains(current_Rev, word)){
                    incRating+=rating;
                    counter++;
                }   
            }
        }
        revScanner.close();
        if(counter == 0){
            return -1;
        }
        return incRating/counter;
    }


    static boolean contains(String reviewText, String word)
    {
        String [] words = reviewText.split(" ");

        for(String w : words)
            if(word.equals(w))
                return true;

        return false;
    }

    public static void main(String[] args){
        System.out.println(Sentiment.sentiment("The increasingly diverse French director has created a film that one can honestly describe as looking , sounding and simply feeling like no other film in recent history . ", "movieReviews.txt"));
    }
}
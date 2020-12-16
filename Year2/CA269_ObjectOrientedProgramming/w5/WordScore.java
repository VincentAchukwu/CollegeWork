import java.util.Scanner;
import java.io.FileNotFoundException;
public class WordScore
{
    public String word;
    public int score;

    public WordScore(String word){
        this.word = word;
    }

    public int score(String review){
        int score = -1;
        String [] rev = review.substring(1).split(" ");
        for(String w:rev){
            if(w.equals(word)){
                score = Integer.parseInt(review.substring(1,2));
                break;
            }
            else{
                score = - 1;
            }
        }
        return score;
    }

    public static void main(String [] args) throws FileNotFoundException
    {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter a word and a review.");

        String word = in.next();
        String review = in.nextLine();
        WordScore wordScore = new WordScore(word);

        if(wordScore.score(review) == -1)
            System.out.println(word + " does not appear in this review.");
        else
            System.out.println(word + " gets a score of " + wordScore.score(review) + ".");
    }
}
    // Write your Hangman class here
import java.util.Scanner;

public class Hangman
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // First get the word
        int wordSeed = in.nextInt();

        String word = Word.getWord(wordSeed);

        // Now you have the word ... encourage the user to guess.
        
        String tracker = "";
        for(int i = 0; i < word.length(); i++){
            tracker = tracker + "_";
        }
        System.out.println("The word is");
        System.out.println(tracker);
        
        char guess;
        String guesses = "";
        while(Word.allDone(word, guesses) == false){
                System.out.println("Guess a letter:");
                guess = in.next().charAt(0);
                guesses += guess;
                tracker = Word.showLetters(word, guesses);
                System.out.println(tracker);
        }
        System.out.println("Well Done, the word was " + word + ".");
    }
}
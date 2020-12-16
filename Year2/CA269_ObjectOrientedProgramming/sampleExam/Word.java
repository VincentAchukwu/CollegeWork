import java.util.Scanner;

public class Word{

    public static String showLetters(String word, String chars){

        String updated = "";
        for(int j = 0; j < word.length(); j++){
            updated = updated + "_";
        }

        for(int i = 0; i < word.length(); i++){
            for(int j = 0; j < chars.length(); j++){
                if(word.charAt(i) == chars.charAt(j)){
                    updated = updated.substring(0,i) + chars.charAt(j) + updated.substring(i+1);
                }
            }
        }
        return updated;
    }

    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        // Ask the user for a word and some guesses
        System.out.print("Enter a word and some guesses: ");
        String word = in.next();
        String guesses = in.next();
        
        String show = Word.showLetters(word, guesses);
        System.out.println(show);
    }

}
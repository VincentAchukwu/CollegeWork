import java.util.Scanner;

public class FirstMiddleLast
{
    public static void main(String [] args){
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter a word: ");
        String word = in.nextLine();
        System.out.println(word.substring(0,1));
        System.out.println(word.substring(1,word.length() - 1));
        System.out.println(word.substring(word.length() - 1));
    }
}
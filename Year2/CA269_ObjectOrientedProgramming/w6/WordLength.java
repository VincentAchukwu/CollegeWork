import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class WordLength
{
    public static void main(String [] args)
    {
        Map<Integer, Integer> map = new HashMap<>();
        Scanner in = new Scanner(System.in);

        while(in.hasNext()){

            String input = in.nextLine();
            String [] words = input.split(" ");
            for(String word: words){

                if(map.containsKey(word.length())){
                    int count = map.get(word.length());
                    map.put(word.length(), count + 1);
                }
                else{
                    map.put(word.length(), 1);
                }
            }
        }
        List<Integer> wordLengths = new ArrayList<>(map.keySet());
        Collections.sort(wordLengths);

        for(int num:wordLengths){
            System.out.println(num + ": " + map.get(num));
        }
    }
}
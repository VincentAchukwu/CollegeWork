import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.io.File;
import java.io.FileNotFoundException;

public class Suspicious{

    public static void main(String [] args){
        try{
            Scanner students = new Scanner(new File(args[0]));
            Scanner delinquents = new Scanner(new File(args[1]));

            Set<String> possibeJuveniles = new HashSet<>();

            while(students.hasNext()){
                String student = students.nextLine();
                possibeJuveniles.add(student);
            }
            students.close();

            int juvenileNo = 1;
            while(delinquents.hasNext()){
                String delinquent = delinquents.nextLine();
                if(possibeJuveniles.contains(delinquent))
                    System.out.printf("%s. %s\n", juvenileNo, delinquent);
                    juvenileNo++;
                // }
            }
        }
        catch(FileNotFoundException e){
            System.out.println("File ain't found ting");
        }
    }
}
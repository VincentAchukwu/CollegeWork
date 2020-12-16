import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class GroupStudents
{
   public static void main(String [] args)
   {
        if(args.length < 1){
            System.out.println("Usage: java ReadNames <filename>");
        }
        else{
            Scanner input = null;
            try{
                input = new Scanner(new File(args[0]));
                int numNames = input.nextInt();

                Student [] group = new Student[numNames];

                for(int i = 0; i < numNames; i++){
                    String name = input.next();
                    int mark = input.nextInt();
                    group[i] = new Student(name, mark);
                }
                Student.print(group);
            }
            catch(FileNotFoundException e){
                System.out.println("File not found");
            }
        }
    }
}
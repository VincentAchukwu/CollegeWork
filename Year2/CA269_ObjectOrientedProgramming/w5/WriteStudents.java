import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class WriteStudents
{
	//Creates a list of Students.
	public static void main(String [] args)
	{
	    if(args.length < 1){
            System.out.println("Usage: java ReadNames <filename>");
	    }
	    else{
	        Scanner input = null;
	        try{
         		//arg[0] is file name
        		input  = new Scanner(new File(args[0]));
        		int lenOfFile = input.nextInt();
                PrintWriter outFile = new PrintWriter(args[1]);
        
        		String [] group = new String[lenOfFile];
        		for (int i = 0; i < lenOfFile; i++)
        		{
        			String name = input.next();
        			int mark = input.nextInt();
        			group[i] = name + " " + (mark + 1);
        		}

        		outFile.println(lenOfFile);
        		for(int j = 0; j < lenOfFile; j++)
        		{
        			outFile.println(group[j]);
        		}
        		outFile.close();
	        }
	        catch(FileNotFoundException e){
	            System.out.println("File not found");
	        }
	    }
	}	
}
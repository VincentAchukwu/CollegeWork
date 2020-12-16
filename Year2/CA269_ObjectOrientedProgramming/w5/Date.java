// import java.util.Scanner;
public class Date
{
    private int day;
    private int month;
    private int year;
    
    public Date(int d, int m, int y){
        day = d;
        month = m;
        year = y;
    }

    public Date(){
        day = 1;
        month = 1;
        year = 2000;
    }

    public Date(String input){
        String[] split = input.split(" ");
        day = Integer.parseInt(split[0]);
        month = Integer.parseInt(split[1]);
        year = Integer.parseInt(split[2]);
    }

    public boolean isOnOrAfter(Date other){
        if((this.year >= other.year) && (this.month >= other.month) && (this.day >= other.day)){
            return true;
        }
        return false;
    }

    public boolean isAfter(Date other){
        if((this.year > other.year) || ((this.year == other.year) && (this.month > other.month)) || ((this.year == other.year) && (this.month == other.month) && (this.day > other.day))){
            return true;
        }
        return false;
    }

    public String toString()
    {
        return day + "/" + month + "/" + year;
    }

    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        Date current = new Date(in.nextLine());
        String line;
        while(in.hasNextLine())
        {
           line = in.nextLine();
           if(line.length() != 0)
           {
              Date date = new Date(line);
              // Do what you want with the date.
              if(!(current.isOnOrAfter(date)))
                 current = date;
           }

        }
        System.out.println(current); // Print the latest date
    }
}
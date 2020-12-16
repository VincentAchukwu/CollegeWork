import java.util.Scanner;

public class Time
{
    // Private variables
    private String hour;
    private String minutes;

    // Constructor (with a String parameter)
    public Time(String time){
        this.hour = time.substring(0,2);
        this.minutes = time.substring(2,4);
    }

    // isLater(Time otherTime) // boolean method to compare two times
    public boolean isLater(Time time2){
        if(Integer.parseInt(this.hour) > Integer.parseInt(time2.hour)){
            return true;
        }
        else if(Integer.parseInt(this.hour) < Integer.parseInt(time2.hour)){
            return false;
        }
        if(Integer.parseInt(this.minutes) > Integer.parseInt(time2.minutes)){
            return true;
        }
        else if(Integer.parseInt(this.minutes) < Integer.parseInt(time2.minutes)){
            return false;
        }
        return false;
    }

    // String toString() // return a String representation of the time (hh:mm)
    public String toString(){
        return String.format("%s:%s",this.hour,this.minutes);
    }

   public static void main(String [] args)
   {
        Scanner in = new Scanner(System.in);
        String line1 = in.nextLine();
        String line2 = in.nextLine();

        Time time1 = new Time(line1);
        Time time2 = new Time(line2);

        if(time1.isLater(time2))
            System.out.println(time1 + " is later than " + time2);
        else
            System.out.println(time1 + " is not later than " + time2);
   }
}
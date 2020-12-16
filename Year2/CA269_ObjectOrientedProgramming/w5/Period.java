import java.util.Scanner;
public class Period{

    private Time start;
    private Time finish;

    public Period(Time time1, Time time2){
        this.start = time1;
        this.finish = time2;
    }

    public boolean overlaps(Period p2){

        if(this.start.isLater(p2.start) && (p2.finish.isLater(this.start))){
            return true;
        }
        else if(p2.start.isLater(this.start) && this.finish.isLater(p2.start)){
            return true;
        }
        return false;
    }

    public String toString(){
        return String.format("%s -> %s",this.start,this.finish);
    }

    public static void main(String [] args)
   {
        Scanner in = new Scanner(System.in);
        String line1 = in.nextLine();
        String line2 = in.nextLine();

        Time time1 = new Time(line1);
        Time time2 = new Time(line2);
        Period p1 = new Period(time1, time2);
        System.out.println("Period 1 is " + p1);


        // Read a new set of times
        line1 = in.nextLine();
        line2 = in.nextLine();

        time1 = new Time(line1);
        time2 = new Time(line2);

        Period p2 = new Period(time1, time2);

        System.out.println("Period 2 is " + p2);
        if(p1.overlaps(p2))
            System.out.println("They overlap");
        else
            System.out.println("They do not overlap");
   }
}

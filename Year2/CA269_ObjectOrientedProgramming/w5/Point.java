import java.util.Scanner;
public class Point
{
   private double x;
   private double y;

   public Point(double newX, double newY)
   {
      x = newX;
      y = newY;
   }

   public Point midPoint(Point p2){
      return new Point(((this.x + p2.y) / 2), (this.y + p2.y) / 2); 
   }

   public String toString()
   {
      return "(" + x + ", " + y + ")";
   }

   public static void main(String [] args)
   {
      Scanner in = new Scanner(System.in);

      // Declare and read in two sets of coordinates
      double x1 = in.nextDouble(), y1 = in.nextDouble();
      double x2 = in.nextDouble(), y2 = in.nextDouble();

      // Now create two points from these coordinates
      Point p1 = new Point(x1, y1);
      Point p2 = new Point(x2, y2);

      Point middle = p1.midPoint(p2);

      System.out.println("The midpoint of " + p1 + " and " + p2 + " is " + middle);
   }
}
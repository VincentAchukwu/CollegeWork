import java.util.Scanner;

public class Point implements Order
{
    private double x, y;
    
    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }

    public boolean lessThan(Order other){
        Point otherPoint = (Point)other;
        if((this.x < otherPoint.x)){
            return true;
        }
        else if((this.x == otherPoint.x) && (this.y < otherPoint.y)){
            return true;
        }
        return false;
    }

    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }

    public static Point getPoint(Scanner in)
    {
        double x = in.nextDouble(), y = in.nextDouble();
        return new Point(x, y);
    }

    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        Point p1 = getPoint(in);
        Point p2 = getPoint(in);
        
        System.out.println("p1 = " + p1);
        System.out.println("p2 = " + p2);
        System.out.println("p1.lessThan(p2) = " + p1.lessThan(p2));
    }
}
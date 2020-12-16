public class Point1 implements Order
{
    private double x, y;
    
    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }
    
    public boolean lessThan(Order other){
        Point otherPoint = (Point)other;
        if((this.x ** 2) + (this.y ** 2)) < ((otherPoint.x ** 2) + (otherPoint.y ** 2)){
            return true;
        }
        return false;
    }
    public boolean lessThanv2(Order other){
        Point otherPoint = (Point)other;
        if((Math.pow(this.x,2) + Math.pow(this.y, 2)) < (Math.pow(otherPoint.x, 2) + Math.pow(otherPoint.y, 2))){
            return true;
        }
        return false;
    }
    
    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }
}
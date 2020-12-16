public class Triangle extends Shape
{
   private double a, b, c; // lengths of sides

   public Triangle(String s, double x, double y, double z)
   {
      super(s);
      a = x; b = y; c = z;
   }

   double area()
   {
      double s = (a+b+c)/2.0;
      return Math.sqrt(s*(s-a)*(s-b)*(s-c));
   }
}
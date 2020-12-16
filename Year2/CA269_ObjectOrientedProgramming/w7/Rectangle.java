public class Rectangle extends Shape
{
   private double width, height; // name inherited

   public Rectangle(String s, double w, double h)
   {
      super(s); // use Shape constructor; effect is name=s;
      width = w;
      height = h;
   }

   double area()
   {
      return width * height;
   }
}
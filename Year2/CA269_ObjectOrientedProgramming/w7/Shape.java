public abstract class Shape
{
   private String name; // will occur in all extensions

   public Shape(String name)
   {
      this.name = name;
   }

   abstract double area(); // no body, note abstract

   public String toString()
   {
      return name + " with area " + area();
   }
}
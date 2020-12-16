public class Circle extends Shape
{
    private double radius;

    public Circle(String name, double radius){
        super(name);
        this.radius = radius;
    }

    double area(){
        return Math.PI * this.radius * this.radius;
    }
}
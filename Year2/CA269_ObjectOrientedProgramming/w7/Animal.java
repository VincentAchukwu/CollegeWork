// An abstract Animal class
// and a method called greeting which returns a String.
public abstract class Animal{

    public Animal(String n)
    {
        this.name = n;
    }

    abstract String hello();
    
    public String greeting()
    {
        return hello() + ", je m'appelle " + name;
    }
    // private
    private String name;
}
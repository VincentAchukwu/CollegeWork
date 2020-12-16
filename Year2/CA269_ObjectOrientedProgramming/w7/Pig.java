public class Pig extends Animal
{
    // since Animal has an abstract method greeting(), Pig needs to implement greeting.
    public Pig(String name){
        super(name);
    }

    public String greeting()
    {
        return "Oink";
    }

    public String hello(){
        return "Oink";
    }
}
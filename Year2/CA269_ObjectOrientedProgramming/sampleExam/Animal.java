import java.util.Scanner;

public abstract class Animal
{
    // private
    private String name;

    public Animal(String n)
    {
        name = n;
    }

    abstract String hello();
    
    public String greeting()
    {
        return hello() + ", je m'appelle " + name;
    }


    public static Animal [] makeSomeNoise()
    {
        Animal [] animals = {new Cat("Angel"), new Pig("Babe"), new Dog("Buster"), new Pig("Sty"), new Dog("Fido"), new Cat("Lassie")};
        return animals;
    }

    public static void main(String [] args)
    {
        Animal [] animals = makeSomeNoise();
        for(Animal animal : animals)
            System.out.println(animal.greeting());
    }
}
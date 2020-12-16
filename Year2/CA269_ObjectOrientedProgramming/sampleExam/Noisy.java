public class Noisy
{
    public static Animal [] makeSomeNoise()
    {
        Animal [] animals = {new Cat("Angel"), new Cat("Cheesire"), new Dog("Buster"), new Dog("Fido"), new Cat("Lassie")};
        System.out.println("Woof!, I am Devil");
        return animals;
    }
}
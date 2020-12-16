// This class cant do much. It can be created and printed.
public class Cat implements Polite
public class Cat implements Order
{
    private String name;
    // 🐈
    public Cat(String n)
    {
        name = n;
    }

    public void hello(){
        System.out.println();
    }

    // for implementing Order interface
    // public boolean lessThan(Order p){
    //     Cat otherP = (Cat)p;
    //     return this.name.length() < otherP.name.length();
    // }
    

    public String toString()
    {
        return "cat: " + name;
    }
}
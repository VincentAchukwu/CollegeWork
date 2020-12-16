public class TotalArgs
{
    public static void main(String [] args)
    {
        int total = 0;
        for(String i:args){
            total += Integer.parseInt(i);
        }
        System.out.printf("The sum of all the args is %d.\n", total);
    }
}
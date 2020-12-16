public class Catch
{
    public static void main(String [] args)
    {
        Broken broke = new Broken();
        System.out.println("Testing");
        
        try
        {
            broke.cracked();
        }
        
        catch (ArrayIndexOutOfBoundsException)
        {
            System.out.println("ArrayIndexOutOfBoundsException");
        }

        catch (NullPointerException)
        {
            System.out.println("NullPointerException");
        }

        catch (ArithmeticException)
        {
            System.out.println("ArithmeticException");
        }

        finally
        {
            System.out.println("Finally");
        }

    }
}
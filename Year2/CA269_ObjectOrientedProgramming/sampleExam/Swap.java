public class Swap{
    public static <T> void swap(T [] nums, int i, int j){
        T tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

       // Generic method to reverse an array.
   public static <T>void reverse(T [] a)
   {
      for(int i = 0; i < a.length / 2; i++)
         Swap.swap(a, i, a.length - 1 - i);
   }

   // Check that an array is the reverse of another
   public static <T> boolean check(T [] a1, T [] a2)
   {
      if(a1.length != a2.length)
         return false;
      for(int i = 0; i < a1.length; i++)
         if(a1[i] != a2[a1.length - 1 - i])
            return false;

      return true;
   }

   public static void main(String []args)
   {
      String [] names = {"abe", "babe", "strobe"};
      Integer [] intObjs = {1, 2, 3, 4, 5, 6, 7, 8}; // Autoboxing.

      // Check the swap method via the reverse method.
      String [] rNames = names.clone(); // first copy the array
      reverse(rNames); // reverse the copy
      System.out.println(check(names, rNames)); // check that it's properly reversed
      System.out.println(check(rNames, names)); // check the other way cos we're paranoid.

       // Check with an array of Integers
      Integer [] rIntObjs = intObjs.clone();
      reverse(rIntObjs);
      System.out.println(check(rIntObjs, intObjs));
      System.out.println(check(intObjs, rIntObjs));
   }
}
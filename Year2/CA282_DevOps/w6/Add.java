public class Add {
    public static void main(String[] args) {
       int total = 0;
       int i;
       for (i = 0; i < args.length; i += 1)
       {
          total += Integer.parseInt(args[i]);
       }
       System.out.println(total);
    }
}

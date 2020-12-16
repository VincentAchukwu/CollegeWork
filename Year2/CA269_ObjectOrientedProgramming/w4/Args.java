public class Args
{
	public static void main(String [] args)
	{
		for(int i = args.length - 1; i >= 0; i--){
			System.out.printf("args[%d] = %s\n", i, args[i]);
		}
	}
}
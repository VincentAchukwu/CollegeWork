public class Test
{
    public static int getSum(int[] lst){
    	int sum = 0;
    	for(int i = 0; i < lst.length; i++){
    		sum += lst[i];
    	}
    	// System.out.println(sum);
    	return sum;
    }

    public static int countFives(int[] lst){
		int count = 0;
		for(int i = 0; i < lst.length; i++){
			if (lst[i] == 5){
				count++;
			}
		}
		// System.out.println(count);
	return count;
	}

    public static int countEven(int[] lst){
    	int count = 0;
    	for(int i = 0; i < lst.length; i++){
    		if(lst[i] % 2 == 0){
    			count++;
    		}
    	}
    	// System.out.println(count);
    	return count;
    }

    // Create a static void method called reverse which takes an array of ints
	public static int[] reverse(int[] nums){
		for(int i = 0; i < nums.length/2; i++){
			int tmp = nums[i];
			nums[i] = nums[nums.length - i - 1];
			nums[nums.length - i - 1] = tmp;
		}
		return nums;
	}

}
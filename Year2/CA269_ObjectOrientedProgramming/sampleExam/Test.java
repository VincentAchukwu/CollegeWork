import java.util.Scanner;

public class Test
{

    // for Student.java and GroupStudent.java
    public static void print(Student [] students){
        for(Student student:students){
            if(student.getMark() >= 55){
                System.out.printf("%d (%s)\n", student.getMark(), student.getName());
            }
        }
    }


    // Create a static void method called reverse which takes an array of ints
    public static void reverse(int [] nums){

        for(int i = 0; i < nums.length/2; i++){
            int tmp = nums[i];
            nums[i] = nums[nums.length - i - 1];
            nums[nums.length - i - 1] = tmp;
        }
    }

    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int len = in.nextInt();
        
        int [] num = new int[len];
        System.out.print("Enter " + len + " numbers: ");
        for(int i = 0; i < num.length; i++)
            num[i] = in.nextInt();
            
        Test.reverse(num);

        System.out.print("The numbers reversed are:");
        for(int i = 0; i < num.length; i++)
            System.out.print(" " + num[i]);
            
        System.out.println();
    }
}
public class Student
{
   String name;
   int mark;

   public Student(String n, int m)
   {
      name = n;
      mark = m;
   }
   public String toString()
   {
      return name + " " + mark;
   }
   public static void print(Student [] group)
   {
       for(int i = 0; i < group.length; i++)
           System.out.println(group[i]);
   }
}
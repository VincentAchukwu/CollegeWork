public class Test
{
    public static void print(Student [] student)
    {
        for(int i = 0; i < student.length; i++)
            if(student[i].getMark() >= 55){
                System.out.printf("%d (%s)\n", student[i].getMark(), student[i].getName());
        }
    }

    public static void printForties(Student [] student)
    {
        for(int i = 0; i < student.length; i++){
            if((student[i].getMark() >= 40) && (student[i].getMark() <= 49)){
                System.out.printf("%d (%s)\n", student[i].getMark(), student[i].getName());
            }
      }
   }

   public static int numberPasses(Student [] student)
   {
        int count = 0;
        for(int i = 0; i < student.length; i++)
        {
            if(student[i].getMark() >= 40)
            {
                count++;
            }
        }
        return count;
   }

   public static Student getBestStudent(Student [] student)
   {
        Student bestStudent = student[0];
        int bestMark = 0;
        for(int i = 0; i < student.length; i++)
        {
            if(student[i].getMark() > bestMark)
            {
                bestMark = student[i].getMark();
                bestStudent = student[i];
            }
        }
        return bestStudent;
   }

   public static double getPassingAverage(Student [] student)
   {
        double sum = 0;
        double count = 0;
        for(int i = 0; i < student.length; i++)
        {
            if(student[i].getMark() >= 40)
            {
                sum += student[i].getMark();
                count++;
            }
        }
        return sum / count;
   }

}
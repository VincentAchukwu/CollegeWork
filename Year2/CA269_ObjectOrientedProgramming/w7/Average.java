public class Average
{
    public static double averageArea(Shape [] shapes){
        double sum = 0;
        int count = 0;
        for(Shape s : shapes){
            sum+=s.area();
            count++;
        }

        return sum/count;
    }
}
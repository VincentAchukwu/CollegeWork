public class Swap{
    static <T> void swap(T [] numbers, int i, int j){
        T tmp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = tmp;
    }
}
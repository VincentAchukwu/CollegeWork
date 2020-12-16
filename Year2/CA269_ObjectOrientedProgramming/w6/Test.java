public class Test{
    static <T extends Order> T max(T a, T b){
        if(a.greaterThan(b)){
            return a;
        }
        return b;
    }
}
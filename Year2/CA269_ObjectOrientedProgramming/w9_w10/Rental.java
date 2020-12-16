import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Rental {

    private Movie _movie;
    private int _daysRented;

    public Rental(Movie movie, int daysRented) {
        _movie = movie;
        _daysRented = daysRented;
    }

    public double getCharge() {
        return _movie.getCharge(_daysRented);
    }

    public int getDaysRented() {
        return _daysRented;
    }

    public Movie getMovie() {
        return _movie;
    }

    public String toString(){
        return _movie + String.format(" [%d]", _daysRented);
    }

    public int getFrequentRenterPoints() {
        return _movie.getFrequentRenterPoints(_daysRented);
    }
}

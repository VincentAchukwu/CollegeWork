class NewReleasePrice extends Price {

    int getPriceCode() {
        return Price.NEW_RELEASE;
    }

    public double getCharge(int daysRented) {
        return daysRented * 3;
    }

    public int getFrequentRenterPoints(int daysRented) {
        return (daysRented > 1) ? 2:1;
    }
}
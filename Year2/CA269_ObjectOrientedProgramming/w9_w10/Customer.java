import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Customer {

    private String _name;
    private List<Rental> _rentals;

    public Customer (String name, List<Rental> rentals){
        _name = name;
        _rentals = rentals;
    };

    public void addRental(Rental arg) {
        _rentals.add(arg);
    }

    public String getName (){
        return _name;
    };

    public List<Rental> getRentals(){
        return _rentals;
    };

    public String toString(){
        return String.format("%s: %s",_name, getRentals());
    }

    public double getTotal(Rental aRental) {
        double result = 0;
        switch (aRental.getMovie().getPriceCode()) {
            case Movie.REGULAR:
                result += 2;
                if (aRental.getDaysRented() > 2)
                    result += (aRental.getDaysRented() - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += aRental.getDaysRented() * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (aRental.getDaysRented() > 3)
                    result += (aRental.getDaysRented() - 3) * 1.5;
                break;
        }
        return result;
    }
    
    public double getTotalCharge(){
        double result = 0;
        for(Rental rental:_rentals){
            result += rental.getCharge();
        }
        return result;
    }

    public int getFrequentRenterPoints(Rental rental) {
        if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) && rental.getDaysRented() > 1)
            return 2;
        else
            return 1;
    }
    
    public int getTotalFrequentRenterPoints(){
        int result = 0;
        for(Rental rental:_rentals){
            result+=rental.getFrequentRenterPoints();
        }
        return result;
    }


    public String statement() {
        String output = "Statement for " + getName()  + "\n";

        for(Rental rental : getRentals())
            output += "  " + rental.getMovie().getTitle() + "  " + rental.getCharge() + "\n";

        output += "Amount owed is " + getTotalCharge() + "\n";
        output += "You earned " + getTotalFrequentRenterPoints()  + " frequent renter points\n";
        return output;
    }
    
    public String htmlStatement(){
        String output = "<h1>Statement for " + _name + "</h1>\n<ol>\n";
        for(Rental rental:_rentals){
            output+="  <li>" + rental.getMovie().getTitle() + "  " + rental.getCharge() + "</li>\n";
        }
        
        output += "</ol>\n<p>Amount owed is " + getTotalCharge() + "</p>\n";
        output += "<p>You earned " + getTotalFrequentRenterPoints()  + " frequent renter points.</p>\n";
        return output;
    }



   public static void main(String [] args)
   {
        Movie [] movies = { new Movie("James Bond does Java", Movie.NEW_RELEASE),
                 new Movie("Mickey Mouse", Movie.CHILDRENS),
                 new Movie("The Pointer Sisters", Movie.REGULAR),
                 new Movie("The Dointer Sisters", Movie.NEW_RELEASE),
                        };
        Rental [] rentalsArray = { new Rental(movies[0], 3),
                            new Rental(movies[1], 10),
                            new Rental(movies[2], 2),
                            new Rental(movies[3], 1),
                                };

        List<Rental> rentals = new ArrayList<Rental>(Arrays.asList(rentalsArray));

        // now printing htmlStatements for Donald and Bernie
        Customer donald = new Customer("Donald", rentals);

        System.out.println(donald.getName());
        System.out.println(donald.getRentals());
        System.out.println(donald); // test the toString() method.
        DummyTester bernie = new DummyTester("Bernie", rentals);


        System.out.println("\nYour statement:");
        System.out.print(donald.statement());  // NB "\n" in the statement() function so not in println!
        System.out.print(donald.htmlStatement());  // NB "\n" in the statement() function so not in println!

        System.out.println("Bernie's statement:");
        System.out.println(bernie.htmlStatement());
   }
}


// A class just to test that the statement and htmlStatement methods use these methods:
        // getTotal()
        // getTotalCharge()
        // getFrequentRenterPoints()
        // getTotalFrequentRenterPoints() 
class DummyTester extends Customer
{
    public DummyTester(String name, List rentals)
    {
        super(name, rentals);
    }

    // Note that we can only do this if getTotal exists in the parent class (Customer)
    public double getTotal(Rental rental)
    {
        return super.getTotal(rental) * 2;  // Just double the charge!
    }

    // Note that we can only do this if getTotalCharge exists in the parent class (Customer)
    public double getTotalCharge()
    {
        return super.getTotalCharge() * 2;  // Just double the charge!
    }

    // Note that we can only do this if getFrequentRenterPoints exists in the parent class (Customer)
    public int getFrequentRenterPoints(Rental rental)
    {
        return super.getFrequentRenterPoints(rental) * 2;  // Just double the rental points!
    }

    // Note that we can only do this if getTotalFrequentRenterPoints exists in the parent class (Customer)
    public int getTotalFrequentRenterPoints(){
        return super.getTotalFrequentRenterPoints() * 2;   // Just double the rental points!
    }
}
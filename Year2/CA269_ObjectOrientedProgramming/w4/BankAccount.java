public class BankAccount{
	double balance;

	public BankAccount(){
		balance = 100.00;
	}

    public BankAccount(double b){
    	balance = b;
    }

    public void setBalance(double newBalance){
    	balance = newBalance;
    }

    public double getBalance(){
    	return newBalance;
    }

    public void withdraw(double amount){
    	balance = balance - amount;
    }

    public void deposit(double amount){
    	balance = balance + amount;
    }

    public String toString(){
    	return String.format("The balance is %.2f", balance);
    }

    public static void main(String [] args){
    	BankAccount ac1 = new BankAccount();
    	BankAccount ac2 = new BankAccount(200);
    	System.out.println(ac2);
    }
}
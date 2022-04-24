import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

// imports for reading file
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

// imports for creating dictionary
import java.util.HashMap;
import java.util.Map;

// import for writing to dat file
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOError;
import java.io.IOException;
import java.io.Writer;

// import for random numbers with threads
import java.util.concurrent.ThreadLocalRandom;

public class CarPaintingAutomation{

    private final Map<String, Integer> config = new HashMap<String, Integer>();
    private final String pathToConfig;

    public CarPaintingAutomation(String pathToConfig){
        this.pathToConfig = pathToConfig;
        this.readFile();
    }

    public void writeData(String text) {
        try{
            Writer output;
            output = new BufferedWriter(new FileWriter("output.dat", true));
            output.append(text);
            output.close();
        } catch (Exception e){
            System.out.println("Failed to write to file");
        }
    }

    private void readFile() {
        try {
            File myObj = new File(this.pathToConfig);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] d = data.split(" ", 2);
                //System.out.println(d[0] + " " + d[1]);
                config.put(d[0], Integer.parseInt(d[1]));
                //System.out.println("VARIABLES DICTIONARY");
                // System.out.println(config);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public Map<String, Integer> getConfig(){
        return this.config;
    }    

    public static void main(String[] args) throws InterruptedException, IOException{

        CarPaintingAutomation painter = new CarPaintingAutomation("config.txt");
        // System.out.println(paintner.getConfig());
        Map<String, Integer> configuration = painter.getConfig();

        // clearing the output.dat file prior to overwriting it
        Writer fileClearer;
        fileClearer = new BufferedWriter(new FileWriter("output.dat"));
        fileClearer.close();

        // for now, we could have a list of car objects here and pass them to the dealership for customer to select from
        // could also have a list of customers who order at random intervals
        List<Car> carModels = new ArrayList<>();

        // Create array of cars of length given in the config file 
        int modelCount = configuration.get("modelCount");
        int basePrice = 1000;
        int priceIncrement = 200;
        for(int i = 1;i <= modelCount;i++){
            carModels.add(new Car(String.format("Tesla Model %d", i), basePrice));
            basePrice += priceIncrement;
        }

        // Create array of dealerships of length given in the config file
        List<Dealership> dealerships = new ArrayList<>();
        int dealerCount = configuration.get("dealershipCount");
        for(int i = 1;i <= dealerCount;i++){
            dealerships.add(new Dealership(String.format("Location %d", i), configuration.get("trailerCap")));
        }

        // Object of a class that has both produce() and consume() methods
        final Warehouse warehouse = new Warehouse();

        // Create producer thread
        Thread t1 = new Thread(new Runnable(){

            public void run(){
                try{
                    warehouse.produce(carModels);
                }
                catch(Exception e){
                }
            }
        });

        // Create consumer thread
        Thread t2 = new Thread(new Runnable(){

            public void run(){
                try{
                    warehouse.consume(carModels, dealerships);
                }
                catch(Exception e){
                }
            }
        });

        // Start both threads
        t1.start();
        t2.start();

        // t1 finishes before t2
        t1.join();
        t2.join();
    }
}

class Warehouse implements Runnable{

    CarPaintingAutomation painter = new CarPaintingAutomation("config.txt");
    Map<String, Integer> configuration = painter.getConfig();

    int warehouseCapacity = configuration.get("warehouseCap");
    static List<Car> warehouseCarStorage = new ArrayList<>();
    List<String> colourOptions = Arrays.asList("Blue", "Red", "Green", "Orange", "White", "Black", "Pink", "Yellow", "Grey");

    int activePools = 0;
    int maxPools = configuration.get("maxPools");
    int trailerCapacity = configuration.get("trailerCap");

    // list of cars waiting to get painted (if production-line/pool limit is reached)
    List<Car> waitingToPaint = new ArrayList<>();

    public void produce(List<Car> carModels) throws InterruptedException{
        // produce car while warehouse capacity not reached
        while(true){
            synchronized(this){
                // producer thread waits while list is full
                while(warehouseCarStorage.size() == warehouseCapacity){
                    wait();
                }

                Car nextCar = carModels.get(ThreadLocalRandom.current().nextInt(carModels.size()));
                String msg = String.format("Producing and storing car in warehouse: %s\n", nextCar.getModelName()); 
                painter.writeData(msg);
                System.out.printf(msg);

                // to insert the jobs in the list (i.e once a car is produced, add it to storage)
                warehouseCarStorage.add(nextCar);

                // notifies the consumer thread that now it can start consuming
                notify();

                // makes the working of program easier to understand
                Thread.sleep(1000);
            }
        }
    }

    // this somewhat acts like a dealership - customers "consume" cars
    public void consume(List<Car> carModels, List<Dealership> dealerships) throws InterruptedException{
        // consume cars and bring to painting ONLY when customer orders
        while(true){
            synchronized(this){
                // consumer thread waits while list is empty
                while(warehouseCarStorage.size() == 0){
                    wait();
                }

                Dealership nextOrder = dealerships.get(ThreadLocalRandom.current().nextInt(dealerships.size())); 

                int randomCarIndex = ThreadLocalRandom.current().nextInt(warehouseCarStorage.size());
                Car carSelection = warehouseCarStorage.get(randomCarIndex);

                int randomColourIndex = ThreadLocalRandom.current().nextInt(colourOptions.size());
                String colour = colourOptions.get(randomColourIndex);
                carSelection.setColour(colour);
                String msg = String.format("%s dealership has sold a %s and selected colour %s.\n", nextOrder.getName(), carSelection.getModelName(), colour);
                painter.writeData(msg);
                System.out.printf(msg);

                // to retrieve the first job in the list (ideally this would be triggered by customer,
                // then their selected car would enter painting process)
                warehouseCarStorage.remove(carSelection);

                // checking if no. active pools hasn't reached no. max pools
                // if not, increment no. pools so we know that the painting process will start in a pool
                if(activePools < maxPools){
                    activePools += 1;
                    carSelection.setProdLine(activePools);
                    // if there are any cars waiting to enter the pool due to pool limit being reached, pop the first one
                    if(waitingToPaint.size() > 0){
                        Car waitingCar = waitingToPaint.remove(0);
                        msg = String.format("No. of Pools active: (%d), painting %s from queue...\n", activePools, waitingCar.getModelName());
                        painter.writeData(msg);
                        System.out.printf(msg);
                        // then initiate paintingo process for that car (prioritising waiting cars first)
                        new Thread(() -> {
                            try {
                                paintCar(nextOrder, waitingCar);
                            }
                            catch (InterruptedException e){
                            }
                        }).start();
                    }
                    // else there are no cars waiting in the queue, proceed with painting as usual
                    else{
                        msg = String.format("No. of Pools active: (%d), painting %s...\n", activePools, carSelection.getModelName());
                        painter.writeData(msg);
                        System.out.printf(msg);
                        new Thread(() -> {
                            try {
                                paintCar(nextOrder, carSelection);
                            }
                            catch (InterruptedException e){
                            }
                        }).start();
                    }
                }
                // else pool limit has been reached, add selected car to the queue for it to be painted later
                else{
                    msg = String.format("Pool limit reached! Adding %s to painting queue\n", carSelection.getModelName());
                    painter.writeData(msg);
                    System.out.printf(msg);
                    waitingToPaint.add(carSelection);
                }

                // Wake up producer thread
                notify();

                // and sleep
                Thread.sleep(1000);
            }
        }
    }

    // given the car model and the dealer who made the order, paint car in the selected colour
    public void paintCar(Dealership nextOrder, Car carSelection) throws InterruptedException{

        String msg = String.format("%s now in painting process for %s in %s (Production line %d)\n", carSelection.getModelName(), nextOrder.getName(), carSelection.getColour(), carSelection.getProdLine());
        painter.writeData(msg);
        System.out.printf(msg);
        // System.out.printf("%s dealership is waiting on these cars: %s", nextOrder.getName(), nextOrder.getWaiting());

        Thread washing = new Thread(new Runnable(){

            public void run(){
                try{
                    paintingProcess("Washing", configuration.get("washing"), carSelection);
                }
                catch(Exception e){
                }
            }
        });
        Thread electro = new Thread(new Runnable(){

            public void run(){
                try{
                    paintingProcess("Electrodipping", configuration.get("electro"), carSelection);
                }
                catch(Exception e){
                }
            }
        });
        Thread sanding = new Thread(new Runnable(){

            public void run(){
                try{
                    paintingProcess("Sanding", configuration.get("sanding"), carSelection);
                }
                catch(Exception e){
                }
            }
        });
        Thread priming = new Thread(new Runnable(){

            public void run(){
                try{
                    paintingProcess("Priming", configuration.get("priming"), carSelection);
                }
                catch(Exception e){
                }
            }
        });
        Thread painting = new Thread(new Runnable(){

            public void run(){
                try{
                    paintingProcess("Painting", configuration.get("painting"), carSelection);
                }
                catch(Exception e){
                }
            }
        });

        washing.start();
        washing.join();

        electro.start();
        electro.join();
        
        sanding.start();
        sanding.join();
        
        priming.start();
        priming.join();
        
        painting.start();
        painting.join();

        msg = "Finished all threads";
        painter.writeData(msg);
        System.out.println(msg);
        activePools -= 1;

        // moved this here since I think it makes more sense for trailer to deliver cars after the painting steps
        // need check to see if waiting >= 3 and if so then 'send' trailer to dealership and start again at 0
        nextOrder.waiting.add(carSelection);
        if (nextOrder.waiting.size() >= trailerCapacity) {
            msg = String.format("%s trailer full!\n", nextOrder.getName());
            painter.writeData(msg);
            System.out.printf(msg);
            for (int i=0; i<nextOrder.waiting.size(); i++) {
                Car currentCar = nextOrder.getWaiting().get(i);
                msg = String.format("%s %s delivered to %s\n", currentCar.getColour(), currentCar.getModelName(), nextOrder.getName());
                painter.writeData(msg);
                System.out.printf(msg);
            }
            nextOrder.waiting = new ArrayList<>();
        }
    }

    // avoiding long repetitive code by creating function for sleep
    public void paintingProcess(String currentProcess, int processTime, Car carSelection){
        String msg = String.format("%s Started %s: %s (Production line %d)\n", Thread.currentThread().getName(), currentProcess, carSelection.getModelName(), carSelection.getProdLine());
        painter.writeData(msg);
        System.out.printf(msg);
        try{
            Thread.sleep(processTime + carSelection.getPrice());
        }
        catch(InterruptedException e){
            e.printStackTrace();
        }
        msg = String.format("%s Finished %s: %s (Production line %d)\n", Thread.currentThread().getName(), currentProcess, carSelection.getModelName(), carSelection.getProdLine());
        painter.writeData(msg);
        System.out.printf(msg);//prints thread name
    }

    public void run(){
    }
}

class Dealership {

    String name;
    int carrierCap;
    List<Car> waiting = new ArrayList<>();
    
    public Dealership(String name, int carrierCap) {
        this.name = name;
        this.carrierCap = carrierCap;
    }

    public String getName() {
        return this.name;
    }

    public int getCarrierCap() {
        return this.carrierCap;
    }

    public int amountWaiting() {
        return this.waiting.size();
    }

    public List<Car> getWaiting() {
        return this.waiting;
    }
}

class Car {

    String modelName;
    String colour;
    int price;
    int productionLine;

    public Car(String modelName, int price) {
        this.modelName = modelName;
        this.price = price;
    }

    public String getModelName() {
        return this.modelName;
    }

    public int getPrice() {
        return this.price;
    }
 
    public void setColour(String colour) {
        this.colour = colour;
    }

    public String getColour() {
        return this.colour;
    }

    public void setProdLine(int productionLine) {
        this.productionLine = productionLine;
    }

    public int getProdLine() {
        return this.productionLine;
    }
}

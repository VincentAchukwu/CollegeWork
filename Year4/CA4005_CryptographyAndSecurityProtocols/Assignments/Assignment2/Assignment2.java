import java.math.BigInteger;
import java.util.Random;
// java.io
import java.io.FileWriter;
import java.io.IOException;
// java.nio
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
// java.security
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Assignment2 implements Assignment2Interface{

    // static field for passing the calculated multInverse from main() to generateR()
    static BigInteger multInverse;

    /* Method generateY returns the public key y and is generated from the given generator, secretKey and modulus */
    public BigInteger generateY(BigInteger generator, BigInteger secretKey, BigInteger modulus){
        return generator.modPow(secretKey, modulus);
    }

    /* Method generateR generates the first part of the ElGamal signature from the given generator, random value k and modulus */
    public BigInteger generateR(BigInteger generator, BigInteger k, BigInteger modulus){

        // r = g^k (mod p)
        BigInteger digitalSignature_R = generator.modPow(k, modulus);
        return digitalSignature_R;
    }

    /* Method generateS generates the second part of the ElGamal signature from the given plaintext, secretKey, first signature part r, random value k and modulus */
    public BigInteger generateS(byte[] plaintext, BigInteger secretKey, BigInteger r, BigInteger k, BigInteger modulus){

        // first calculate xr: private key * r
        BigInteger xr = secretKey.multiply(r);
        // then calculate H(m) - xr
        BigInteger hashedFile = new BigInteger(1, plaintext);

        // s = (H(m) - xr)^(k - 1) (mod p - 1)
        BigInteger digitalSignature_S = ((hashedFile.subtract(xr)).multiply(multInverse).mod(modulus.subtract(BigInteger.ONE)));

        return digitalSignature_S;
    }

    /* Method calculateGCD returns the GCD of the given val1 and val2 */
    public BigInteger calculateGCD(BigInteger val1, BigInteger val2){

        // using recursion to calculate gcd(val1, val2)
        if(val2.equals(BigInteger.ZERO)){
            return val1;
        }

        return calculateGCD(val2, val1.mod(val2));
    }

    public static BigInteger[] extendedEuclidean(BigInteger val1, BigInteger modulus){

        BigInteger[] result = new BigInteger[3];

        if(modulus.equals(BigInteger.ZERO)){
            result[0] = val1;
            result[1] = BigInteger.ONE;
            result[2] = BigInteger.ZERO;
        }

        else{
            result = extendedEuclidean(modulus, val1.mod(modulus));
            BigInteger tmpY = result[1].subtract(result[2].multiply(val1.divide(modulus)));
            result[1] = result[2];
            result[2] = tmpY;
        }

        return result;
        
    }

    /* Method calculateInverse returns the modular inverse of the given val using the given modulus */
    public BigInteger calculateInverse(BigInteger val, BigInteger modulus){

        BigInteger[] result = extendedEuclidean(val, modulus);

        if(!result[0].equals(BigInteger.ONE)){
            return BigInteger.ZERO;
        }

        return result[1].mod(modulus);
    }

    // generates random value for private key
    public static BigInteger randomValueGenerator(BigInteger primeMod, int minVal){

        BigInteger randValue;
        Random random = new Random();

        do{
            randValue = new BigInteger(primeMod.bitLength(), random);
        } while (
                    randValue.compareTo(primeMod.subtract(BigInteger.ONE)) != 1
                    && randValue.compareTo(BigInteger.valueOf(minVal)) != 1
                );

        return randValue;
    }

    // hashes the given file via SHA256
    public static byte[] hashFile(byte[] fileInBytes) throws NoSuchAlgorithmException{

        // creating MD via SHA256
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hashedFile = md.digest(fileInBytes);

        return hashedFile;
    }

    // helper method to avoid code repetition for saving r, s, and y to their files
    public void saveToFile(BigInteger output, String outputFile) throws IOException{
        FileWriter outputWriter = new FileWriter(outputFile);
        outputWriter.write(output.toString(16));
        outputWriter.close();
    }

    public static void main(String [] args) throws NoSuchAlgorithmException, IOException{

        // creating instance to access ElGamal Signature methods
        Assignment2 elGamalSignature = new Assignment2();

        // specifying filenames for file to sign, r, s, and y
        String classFile = "Assignment2.class";
        String publicKeyFile = "y.txt";
        String rFile = "r.txt";
        String sFile = "s.txt";

        // prime modulus p, and generator g
        BigInteger primeModulus = new BigInteger(
                                    "b59dd79568817b4b9f6789822d22594f376e6a9abc0241846de426e5dd8f6eddef00b465f38f509b2b18351064704fe75f012fa346c5e2c442d7c99eac79b2bc8a202c98327b96816cb8042698ed3734643c4c05164e739cb72fba24f6156b6f47a7300ef778c378ea301e1141a6b25d48f1924268c62ee8dd3134745cdf7323",
                                    16
                                );

        BigInteger generator = new BigInteger(
                                "44ec9d52c8f9189e49cd7c70253c2eb3154dd4f08467a64a0267c9defe4119f2e373388cfa350a4e66e432d638ccdc58eb703e31d4c84e50398f9f91677e88641a2d2f6157e2f4ec538088dcf5940b053c622e53bab0b4e84b1465f5738f549664bd7430961d3e5a2e7bceb62418db747386a58ff267a9939833beefb7a6fd68",
                                16
                            );

        // initiating public/private ElGamal key pairs
        // random secret key x (1 < x < p - 1 (to be hardcoded))
        // BigInteger privateKey = randomValueGenerator(primeModulus, 1);
        // private key (x) hardcoded after generating via randomValueGenerator(primeModulus, 1)
        BigInteger privateKey = new BigInteger(
                                "d4346ebbe20b23648052119d4b5c538fa3f5bebdecbfec22d38e723c480909825518fc2da5f12644006bba0726d9ce9b5db5f454fcb51265c0dc2f6e3725ab083e3c5a06fc66b7b5985bee9120d961cb9968716e858e0ce180878c40a9be502d66036f5e3e48cb08c515342ed332a48081f4089eca4e9f732f2851762f987900",
                                16
                            );

        // public key y (g^x (mod p))
        BigInteger publicKey = elGamalSignature.generateY(generator, privateKey, primeModulus);

        // specifying file to digitally sign and converting to bytes
        Path classFilePath = Paths.get(System.getProperty("user.dir") + "/" + classFile);
        byte[] fileInBytes = Files.readAllBytes(classFilePath);

        // hashing message
        byte[] hashedFileBytes = hashFile(fileInBytes);

        // signing the message by:
        //      - generating a random k
        //      - computing r
        //      - computing s via Extended EGCD
        //      - r||s becomes digital signature of m

        // choosing random value k where 0 < k < p-1 and gcd(k, p - 1) = 1
        // (hardcoded after generating via randomValueGenerator(primeModulus, 0))
        BigInteger k = new BigInteger(
                        "1f5f025e503ff26d68a84231ed32f3afc668d91924729975decb5f87a97f699a8917453cbd1e3959eee068bf01a812c570bfc97fa7e9eeaf9f17e6941826c04997c8786d43cfd29067d01d9437ba97ff79f0211ab7054384140955e9e09f86b570db80d1258ab7f4ef33afbf22800a407cbaf3bb1ecd249f1edd11552fb5e6a7",
                        16
                    );
        BigInteger r = null;
        BigInteger s = BigInteger.ZERO;
        while(s.compareTo(BigInteger.ZERO) == 0){

            multInverse = BigInteger.valueOf(-1);            
            while(multInverse.compareTo(BigInteger.valueOf(-1)) == 0){
                multInverse = elGamalSignature.calculateInverse(k, primeModulus);
            }

            // r = generator^k (mod primeModulus)
            r = elGamalSignature.generateR(generator, k, primeModulus);

            // s = (H(m) - xr)^(k - 1) (mod primeModulus - 1), if s == 0 restart
            s = elGamalSignature.generateS(hashedFileBytes, privateKey, r, k, primeModulus);
        }

        // printing private key (x) and random value (k) -> both are hardcoded after generation
        System.out.printf("Private key (x): %s\n\n", privateKey.toString(16));
        System.out.printf("Random value (k): %s\n\n", k.toString(16));
        
        // printing and saving public key (y), and digital signatures (r and s) to their files
        System.out.printf("Public key (y): %s\n\n", publicKey.toString(16));
        elGamalSignature.saveToFile(publicKey, publicKeyFile);

        System.out.printf("R: %s\n\n", r.toString(16));
        elGamalSignature.saveToFile(r, rFile);

        System.out.printf("S: %s\n\n", s.toString(16));
        elGamalSignature.saveToFile(s, sFile);
    }
}

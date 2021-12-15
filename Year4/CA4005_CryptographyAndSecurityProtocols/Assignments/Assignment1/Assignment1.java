import java.math.BigInteger;
import java.util.Random;
// java.io
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.OutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
// javax.crypto
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
// java.security
import java.security.Key;
import java.security.MessageDigest;
import java.security.SecureRandom;
import java.security.GeneralSecurityException;
import java.security.NoSuchAlgorithmException;
// java.nio files
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
// used for converting datatype
import javax.xml.bind.DatatypeConverter;

/*
    - Password encoded via UTF-8, salt randomly generated (128-bit), then concatenated (p||s)
    - (p||s) hashed 200x -> becomes AES key
    - AES via CBC on input binary file using AES key and IV, padding done in the end
    - password encrypted given exponent and public modulus with modular exponentiation
*/
public class Assignment1 implements Assignment1Interface{

    // Method generateKey returns the key as an array of bytes and is generated from the given password and salt.
    public byte[] generateKey(byte[] password, byte[] salt){

        try{
            // password and key concatenated (p||s)
            byte[] key = new byte[password.length + salt.length];
            System.arraycopy(password, 0, key, 0, password.length);
            System.arraycopy(salt, 0, key, password.length, salt.length);

            // now the key gets hashed 200 times
            byte[] keyDigest = keyDigester(key);

            return keyDigest;
        }
        catch(GeneralSecurityException e){
            System.out.println("generateKey() -> GeneralSecurityException caught");
            return password;
        }
    }

    // hashes the key 200 times
    public static byte[] keyDigester(byte[] key) throws NoSuchAlgorithmException{

        // creating MD via SHA256
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hashedKey = key;

        // hashing 200 times
        for(int i = 0; i < 200; i++){
            hashedKey = digest.digest(hashedKey);
        }

        return hashedKey;
    }

    // Method encryptAES returns the AES encryption of the given plaintext as an array of bytes using the given iv and key.
    public byte[] encryptAES(byte[] plaintext, byte[] iv, byte[] key){

        try{
            SecretKeySpec aesKey = new SecretKeySpec(key, "AES");
            IvParameterSpec IV = new IvParameterSpec(iv);
            // allows for encryption via CBC mode
            Cipher encoder = Cipher.getInstance("AES/CBC/NoPadding");
            encoder.init(Cipher.ENCRYPT_MODE, aesKey, IV);

            // initialising padding format
            int filePadding = 16 - (plaintext.length % 16);
            byte[] unencodedPaddedFile = new byte[plaintext.length + filePadding];
            System.arraycopy(plaintext, 0, unencodedPaddedFile, 0, plaintext.length);

            // if final part of message < block size: append a 1-bit and fill the rest of block with 0-bits.
            // else if final part of message == block size: append extra block starting with 1-bit and fill the rest of block with 0-bits.
            unencodedPaddedFile[plaintext.length] = (byte) 128;
            for(int i = plaintext.length + 1; i < unencodedPaddedFile.length; i++){
                unencodedPaddedFile[i] = (byte) 0;
            }

            // encrypting the final block of data
            byte[] encryptionBytes = encoder.doFinal(unencodedPaddedFile);

            return encryptionBytes;
        }
        catch(GeneralSecurityException e){
            System.out.println("encryptAES() -> GeneralSecurityException caught");
            return plaintext;
        }
    }

    // Method decryptAES returns the AES decryption of the given ciphertext as an array of bytes using the given iv and key.
    public byte[] decryptAES(byte[] ciphertext, byte[] iv, byte[] key){

        try{
            // reverse of encryptAES
            SecretKeySpec aesKey = new SecretKeySpec(key, "AES");
            IvParameterSpec IV = new IvParameterSpec(iv);
            // allows for decryption via CBC mode
            Cipher decoder = Cipher.getInstance("AES/CBC/NoPadding");
            decoder.init(Cipher.DECRYPT_MODE, aesKey, IV);
            byte[] decryptionBytes = decoder.doFinal(ciphertext);

            return decryptionBytes;
        }
        catch(GeneralSecurityException e){
            System.out.println("decryptAES() -> GeneralSecurityException caught");
            return ciphertext;
        }
    }

    // Method encryptRSA returns the encryption of the given plaintext using the given encryption exponent and modulus.
    public byte[] encryptRSA(byte[] plaintext, BigInteger exponent, BigInteger modulus){

        BigInteger bigIntPassword = new BigInteger(plaintext);
        return modExp(bigIntPassword, exponent, modulus).toByteArray();
    }

    // Method modExp returns the result of raising the given base to the power of the given exponent using the given modulus.
    public BigInteger modExp(BigInteger base, BigInteger exponent, BigInteger modulus){

        // modExp via right-to-left approach
        // converting exponent to binary string to perform right-to-left method (using guide from the notes)
        String exponentBytes = Integer.toBinaryString(exponent.intValue());
        BigInteger encryptedPassword = BigInteger.ONE;
        for(int i = 0; i < exponentBytes.length(); i++){
            // if bit is set: encryptedPassword = encryptedPassword * base (mod modulus)
            if(exponentBytes.charAt(i) == '1'){
                encryptedPassword = (encryptedPassword.multiply(base)).mod(modulus);
            }
            // for every new bit: base = base * base (mod modulus)
            base = (base.multiply(base).mod(modulus));
        }

        return encryptedPassword;
    }

    // encoding password
    public static BigInteger encPassword(String password) throws UnsupportedEncodingException{

        // encoding then converting password to BigInteger
        BigInteger encodedPassword = new BigInteger(password.getBytes("UTF-8"));
        return encodedPassword;
    }

    // used for generating random 128-bit IV/salt
    public static byte[] rand16ByteValue(){

        // converting 16 bytes to 128 bits
        byte[] ivBytes = new byte[16];
        Random random = new SecureRandom();
        random.nextBytes(ivBytes);

        return ivBytes;
    }

    public static void main(String [] args) throws GeneralSecurityException, IOException{

        // creating instance to access methods, initialising aesCipher
        Assignment1 aesCipher = new Assignment1();
        String fileName = args[0];

        // encoding password
        String password = "`m8>*5?=m.Cz,k]z";
        byte[] encodedPassword = password.getBytes("UTF-8");

        // salt generator
        byte[] salt = rand16ByteValue();

        // IV generator
        byte[] IV = rand16ByteValue();

        // key generator (p||s on password and salt), then hashed 200 times
        byte[] encryptionKey = aesCipher.generateKey(encodedPassword, salt);

        // encrypting the binary file (reading file given the path (Assignment.class))
        Path path = Paths.get(System.getProperty("user.dir") + "/" + fileName);
        byte[] fileInBytes = Files.readAllBytes(path);
        byte[] encryptedFile = aesCipher.encryptAES(fileInBytes, IV, encryptionKey);
        // decrypting the encrypted file (for testing)
        byte[] decryptedFile = aesCipher.decryptAES(encryptedFile, IV, encryptionKey);

        // encrypting password via RSA
        BigInteger exponent = new BigInteger("65537");
        BigInteger publicModulus = new BigInteger(
                                    "c406136c12640a665900a9df4df63a84fc855927b729a3a106fb3f379e8e4190ebba442f67b93402e535b18a5777e6490e67dbee954bb02175e43b6481e7563d3f9ff338f07950d1553ee6c343d3f8148f71b4d2df8da7efb39f846ac07c865201fbb35ea4d71dc5f858d9d41aaa856d50dc2d2732582f80e7d38c32aba87ba9",
                                    16
                                );
        // encrypting the password with modExp given exponent and modulus
        byte[] encryptedPassword = aesCipher.encryptRSA(encodedPassword, exponent, publicModulus);

        // writing password, salt, IV, and encryption to their corresponding files
        OutputStream passwordOutputFile = new FileOutputStream("Password.txt");
        passwordOutputFile.write(DatatypeConverter.printHexBinary(encryptedPassword).getBytes());
        passwordOutputFile.close();

        OutputStream saltOutputFile = new FileOutputStream("Salt.txt");
        saltOutputFile.write(DatatypeConverter.printHexBinary(salt).getBytes());
        saltOutputFile.close();

        OutputStream ivOutputFile = new FileOutputStream("IV.txt");
        ivOutputFile.write(DatatypeConverter.printHexBinary(IV).getBytes());
        ivOutputFile.close();

        OutputStream encryptedOutputFile = new FileOutputStream("Encryption.txt");
        encryptedOutputFile.write(DatatypeConverter.printHexBinary(encryptedFile).getBytes());
        encryptedOutputFile.close();

        // for testing, outputting decrypted file to Decryption.txt by converting it to a UTF-8 string
        String decryptedText = new String(decryptedFile, "UTF-8");
        // removing the zero-valued bytes from byte array
        String trimmedLeadingZeros = decryptedText.replaceAll("\0", "");
        BufferedWriter decryptedOutputFile = new BufferedWriter(new FileWriter("Decryption.txt"));
        decryptedOutputFile.write(trimmedLeadingZeros);
        decryptedOutputFile.close();

        // System.out.println("Encoded Password: " + DatatypeConverter.printHexBinary(encodedPassword));
        // System.out.println("Salt: " + DatatypeConverter.printHexBinary(salt));
        // System.out.println("IV: " + DatatypeConverter.printHexBinary(IV));
        // System.out.println("AES Key: " + DatatypeConverter.printHexBinary(encryptionKey));
        // System.out.println("Encrypted password: " + DatatypeConverter.printHexBinary(encryptedPassword));
        // System.out.println("Encrypted File: " + DatatypeConverter.printHexBinary(encryptedFile));
    }
}

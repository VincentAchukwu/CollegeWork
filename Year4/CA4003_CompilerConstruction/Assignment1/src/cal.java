import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.antlr.v4.runtime.CharStreams;
import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.file.Path;
import java.nio.file.Paths;

public class cal {

    public static void main (String[] args) throws Exception {

        // reading in cal input file
        String inputFile = null;
        if (args.length > 0) {
            inputFile = args[0];
        }

        InputStream is = System.in;
        if (inputFile != null) {
            is = new FileInputStream(inputFile);
        }
            
        // removeErrorListeners() is for removing default error listeners to create custom error handling
        // lexer
        calLexer lexer = new calLexer(CharStreams.fromStream(is));
        lexer.removeErrorListeners();

        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // parser
        calParser parser = new calParser(tokens);
        parser.removeErrorListeners();

        // obtaining filename for output of syntax checker
        String fileName = getFileName(inputFile);

        // setting up the syntax error listener with our own custom error message
        CalErrorListener errorHandling = new CalErrorListener(fileName);
        parser.addErrorListener(errorHandling);

        ParseTree tree = parser.prog();

        // if no errors (i.e: the error count == 0), print message that the cal file(s) parsed successfully
        if(errorHandling.errorCount == 0) {
            System.out.printf("%s parsed successfully!\n", fileName);
        }
    }

    // getting the file name for the output message rather than having the path included for the output
    private static String getFileName(String inputFile) {
        if (inputFile == null) {
            return "input";
        }

        Path path = Paths.get(inputFile);
        // converts file path to the name of the file itslef via string
        return path.getFileName().toString();
    }
}

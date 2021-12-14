import org.antlr.v4.runtime.ANTLRErrorListener;
import org.antlr.v4.runtime.atn.ATNConfigSet;
import org.antlr.v4.runtime.Parser;
import org.antlr.v4.runtime.Recognizer;
import org.antlr.v4.runtime.RecognitionException;
import org.antlr.v4.runtime.dfa.DFA;
import java.util.BitSet;

public class CalErrorListener implements ANTLRErrorListener {

    // storing file name and count
    private String fileName;
    // public to allow cal.java to access variable for checking if no errors were caught
    public Integer errorCount;

    // initialising filename variable for error output
    public CalErrorListener(String fileName) {
        this.fileName = fileName;
        this.errorCount = 0;
    }
    
    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object o, int i, int i1, String s, RecognitionException e) {
        // if we encounter the syntax error, we print the message and increment the count to prevent
        // the "parsed successfully" message from printing.
        System.out.printf("%s did not parse successfully.\n", this.fileName);
        errorCount += 1;
    }

    @Override
    public void reportAmbiguity(Parser parser, DFA dfa, int i, int i1, boolean b, BitSet bitSet, ATNConfigSet atnConfigSet) {
        // System.out.println("Report ambiguity");
    }

    @Override
    public void reportAttemptingFullContext(Parser parser, DFA dfa, int i, int i1, BitSet bitSet, ATNConfigSet atnConfigSet) {
        // System.out.println("Report attempting full context");
    }

    @Override
    public void reportContextSensitivity(Parser parser, DFA dfa, int i, int i1, int i2, ATNConfigSet atnConfigSet) {
        // System.out.println("Report context sensitivity");
    }
}

import java.util.*;

public class SymbolTable {

    // undo stack and hashtable
    private Stack<String> undoStack;
    public Map<String, Symbol> symbolTable;

    // initiating empty stack
    public SymbolTable() {
        undoStack = new Stack<String>();
        symbolTable = new HashMap<String, Symbol>();
    }

    // using stack starting with dollar sign to identify local scope
    // new scope entered prior to adding elements to table
    public void intoScope() {
        undoStack.push("$");
    }

    // popping off elements from stack until dollar sign is reached (local scope)
    public List<String> exitScope() {

        List<String> idElements = new ArrayList<>();

        // while the stack is not empty, pop elements off and save to list
        while(undoStack.size() > 0) {
            // get current element in stack
            String element = undoStack.pop();
            // if we come across the special symbol, break the loop
            if(element == "$") {
                break;
            }
            symbolTable.remove(element);
            idElements.add(element);
        }
        return idElements;
    }

    // adding to symbol table
    public void addId(String id, String type, String scope, String kind) {
        type = type.toLowerCase();
        Symbol symbol = new Symbol(id, type, scope, kind);
        symbolTable.put(id, symbol);
        // then pushing to stack
        undoStack.push(id);
    }

    // obtain symbol via id
    public Symbol getId(String id) {
        return symbolTable.get(id);
    }

    // obtain symbol type via id
    public String getIdType(String id) {
        return getId(id).type;
    }

    // comparing a type with the identifier
    public boolean compareIdType(String id, String type) {
        Symbol symbol = getId(id);
        return symbol.type == type;
    }

    // since constant cannot be changed once declared, we check it
    public boolean checkConstantError(String id){
        Symbol symbol = getId(id);
        boolean isConstant = (symbol.kind == "constant");
        // if it's not a constant
        if(!isConstant){
            return true;
        }
        // else it's a constant, error thrown
        throw new RuntimeException("Error...the constant " + id + " cannot be updated after declaration. Use a variable.");
    }

    // comparing declaration type to the value type being assigned
    public boolean compTypeValue(String type, String val) throws RuntimeException {

        // initiate matching to false for the last case
        boolean isMatching = false;

        // checking id
        if (getId(val) != null) {
            isMatching = type.equalsIgnoreCase(getId(val).type);
        }

        // checking boolean
        else if(
                (val.equalsIgnoreCase("true") || val.equalsIgnoreCase("false")) && 
                (type.equalsIgnoreCase("boolean"))
            ) {
            // set as true if matched
            isMatching = true;
        }

        // checking integers
        else if(val != null && type.equalsIgnoreCase("integer")) {
            isMatching = true;
        }

        if (isMatching)
            return true;

        // for non-matching types
        throw new RuntimeException("Error...the constant and value types do not match. Value must be assigned to the correct type.");
    }
}

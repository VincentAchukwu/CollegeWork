import java.util.*;

public class EvalVisitor extends calBaseVisitor<Integer> {

    Map<String, Integer> memory = new HashMap<String, Integer>();

    // initialising symbol table
	SymbolTable symbolTable = new SymbolTable();

    // initialising inFunction to false, scope initially global
    private boolean inFunction = false;

    @Override
    public Integer visitVarDecl(calParser.VarDeclContext ctx) {

        String varID = ctx.ID().getText();
        String varType = ctx.type().getText();
        Integer varValue = null;

        if(varType.equalsIgnoreCase("void")) {
            throw new RuntimeException("Error...variable " + varID + " cannot be void.");
        }

        // if it's in a function it's local, else it's global
        if(inFunction) {
            // since it's local, we include the special marker
            varID = '$' + varID;
            // if it already contains this, var is already defined
            if(memory.containsKey(varID)) {
                throw new RuntimeException("Error...variable " + varID + " already defined.");
            }
            symbolTable.addId(varID, varType, "local", "variable");
        }

        else {
            // since it's global, we check again if it contains the special marker
            if (memory.containsKey(varID)) {
                throw new RuntimeException("Error...variable " + varID + " already defined.");
            }
            symbolTable.addId(varID, varType, "global", "variable");
        }

        // update memory then return value
        memory.put(varID, varValue);
        return varValue;
    }

    @Override
    public Integer visitConstDecl(calParser.ConstDeclContext ctx){

        // obtaining the constant ID and type
        String constID = ctx.ID().getText();
        String constType = ctx.type().getText();
        
        // cannot have void constant
        if(constType.equalsIgnoreCase("void")) {
            throw new RuntimeException("Error...constant " + constID + " cannot be void.");
        }

        Integer constValue = visit(ctx.expression());
        String expression = ctx.expression().getText().split("\\(")[0];
        symbolTable.compTypeValue(constType, expression);

        // if it's in a function it's local
        if(inFunction) {
            constID = '$' + constID;
            if (memory.containsKey(constID)) {
                throw new RuntimeException("Error...constant " + constID + " is already defined.");
            }
            symbolTable.addId(constID, constType, "local", "constant");
        }

        // else it's global
        else {
            if(memory.containsKey(constID)) {
                throw new RuntimeException("Error...constant " + constID + " is already defined.");
            }
            symbolTable.addId(constID, constType, "global", "constant");
        }

        memory.put(constID, constValue);
        return constValue;
    }
}

// properties of the symbol table

public class Symbol {

    String id, type, scope, kind;

    // "kind" could be a function, variable, or constant
    public Symbol (String id, String type, String scope, String kind) {
        this.id = id;
        this.type = type;
        this.scope = scope;
        this.kind = kind;
    }
}

grammar cal;

// parser rules
prog:                     (decList functionList main)
                        | EOF
                        ;

decList:                (decl SEMI decList)?;

decl:                     varDecl
                        | constDecl
                        ;

varDecl:                VAR ID COLON type;

constDecl:              CONST ID COLON type ASSIGN expression;

functionList:           (function functionList)?;

function:               type ID LBRACK parameterList RBRACK
                        LBRACE
                        decList
                        statementBlock
                        RETURN LBRACK expression? RBRACK SEMI
                        RBRACE;

type:                     INTEGER
                        | BOOLEAN
                        | VOID
                        ;

parameterList:          nempParameterList?;

nempParameterList:        ID COLON type
                        | ID COLON type COMMA nempParameterList
                        ;

main:                   MAIN LBRACE decList statementBlock RBRACE;

statementBlock:         (statement statementBlock)?;

statement:                ID ASSIGN expression SEMI
                        | ID LBRACK argList RBRACK SEMI
                        | LBRACE statementBlock RBRACE
                        | IF condition LBRACE statementBlock RBRACE
                        | ELSE LBRACE statementBlock RBRACE
                        | WHILE condition LBRACE statementBlock RBRACE
                        | SKIPPING SEMI
                        ;

// using frag instead of fragment since fragment is a reserved keyword in antlr
expression:               frag binaryArithOp frag
                        | LBRACK expression RBRACK
                        | ID LBRACK argList RBRACK
                        | frag
                        ;

binaryArithOp:            PLUS
                        | MINUS
                        ;

// eliminated indirect left recursion by removing the additional expression present in the CAL language definition
frag:                     ID
                        | MINUS ID
                        | NUMBER
                        | TRUE
                        | FALSE
                        ;

condition:                NEG condition
                        | LBRACK condition RBRACK
                        | expression compOp expression
                        | condition (OR
                        | AND) condition
                        ;

compOp:                   EQUAL
                        | NOTEQUAL
                        | LT
                        | LTE
                        | GT
                        | GTE
                        ;

argList:                nempArgList?;

nempArgList:              ID
                        | ID COMMA nempArgList;

// lexer rules
// creating fragments for defining keywords via alphabet of lowercase and uppercase letters
fragment A:             ('a' | 'A');
fragment B:             ('b' | 'B');
fragment C:             ('c' | 'C');
fragment D:             ('d' | 'D');
fragment E:             ('e' | 'E');
fragment F:             ('f' | 'F');
fragment G:             ('g' | 'G');
fragment H:             ('h' | 'H');
fragment I:             ('i' | 'I');
fragment J:             ('j' | 'J');
fragment K:             ('k' | 'K');
fragment L:             ('l' | 'L');
fragment M:             ('m' | 'M');
fragment N:             ('n' | 'N');
fragment O:             ('o' | 'O');
fragment P:             ('p' | 'P');
fragment Q:             ('q' | 'Q');
fragment R:             ('r' | 'R');
fragment S:             ('s' | 'S');
fragment T:             ('t' | 'T');
fragment U:             ('u' | 'U');
fragment V:             ('v' | 'V');
fragment W:             ('w' | 'W');
fragment X:             ('x' | 'X');
fragment Y:             ('y' | 'Y');
fragment Z:             ('z' | 'Z');

// letters and digits
fragment Letter:        [a-zA-Z];
fragment Digit:         [0-9];
fragment UnderScore:     '_';

// tokens definitions for the language
// initialising words (SKIP is a reserved word in ANTLR so I changed it to SKIPPING)
VAR:                    V A R;
CONST:                  C O N S T;
INTEGER:                I N T E G E R;
BOOLEAN:                B O O L E A N;
TRUE:                   T R U E;
FALSE:                  F A L S E;
MAIN:                   M A I N;
WHILE:                  W H I L E;
IF:                     I F;
ELSE:                   E L S E;
RETURN:                 R E T U R N;
VOID:                   V O I D;
SKIPPING:               S K I P;

// operators
ASSIGN:                 '=';
PLUS:                   '+';
MINUS:                  '-';
NEG:                    '~';
OR:                     '||';
AND:                    '&&';
EQUAL:                  '==';
NOTEQUAL:               '!=';
LT:                     '<';
LTE:                    '<=';
GT:                     '>';
GTE:                    '>=';

// separators
COMMA:                  ',';
SEMI:                   ';';
COLON:                  ':';
LBRACE:                 '{';
RBRACE:                 '}';
LBRACK:                 '(';
RBRACK:                 ')';

// integers and identifiers
NUMBER:                 '0' | (MINUS? [1-9] Digit*);
ID:                     Letter (Letter | Digit | UnderScore)*;

// ignoring whitespaces and comments
WS:                     [ \t\n\r]+ -> skip;
COMMENT:                '//' .*? '\n' -> skip;
NESTED_COMMENT:         '/*' (NESTED_COMMENT|.)*? '*/' -> skip;

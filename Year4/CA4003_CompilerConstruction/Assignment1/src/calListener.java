// Generated from cal.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link calParser}.
 */
public interface calListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link calParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(calParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(calParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#decList}.
	 * @param ctx the parse tree
	 */
	void enterDecList(calParser.DecListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#decList}.
	 * @param ctx the parse tree
	 */
	void exitDecList(calParser.DecListContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(calParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(calParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(calParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(calParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#constDecl}.
	 * @param ctx the parse tree
	 */
	void enterConstDecl(calParser.ConstDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#constDecl}.
	 * @param ctx the parse tree
	 */
	void exitConstDecl(calParser.ConstDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#functionList}.
	 * @param ctx the parse tree
	 */
	void enterFunctionList(calParser.FunctionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#functionList}.
	 * @param ctx the parse tree
	 */
	void exitFunctionList(calParser.FunctionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(calParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(calParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(calParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(calParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(calParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(calParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#nempParameterList}.
	 * @param ctx the parse tree
	 */
	void enterNempParameterList(calParser.NempParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#nempParameterList}.
	 * @param ctx the parse tree
	 */
	void exitNempParameterList(calParser.NempParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(calParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(calParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void enterStatementBlock(calParser.StatementBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#statementBlock}.
	 * @param ctx the parse tree
	 */
	void exitStatementBlock(calParser.StatementBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(calParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(calParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(calParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(calParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#binaryArithOp}.
	 * @param ctx the parse tree
	 */
	void enterBinaryArithOp(calParser.BinaryArithOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#binaryArithOp}.
	 * @param ctx the parse tree
	 */
	void exitBinaryArithOp(calParser.BinaryArithOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#frag}.
	 * @param ctx the parse tree
	 */
	void enterFrag(calParser.FragContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#frag}.
	 * @param ctx the parse tree
	 */
	void exitFrag(calParser.FragContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(calParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(calParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#compOp}.
	 * @param ctx the parse tree
	 */
	void enterCompOp(calParser.CompOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#compOp}.
	 * @param ctx the parse tree
	 */
	void exitCompOp(calParser.CompOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(calParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(calParser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link calParser#nempArgList}.
	 * @param ctx the parse tree
	 */
	void enterNempArgList(calParser.NempArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link calParser#nempArgList}.
	 * @param ctx the parse tree
	 */
	void exitNempArgList(calParser.NempArgListContext ctx);
}
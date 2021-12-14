// Generated from cal.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link calParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface calVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link calParser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProg(calParser.ProgContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#decList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecList(calParser.DecListContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecl(calParser.DeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#varDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDecl(calParser.VarDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#constDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstDecl(calParser.ConstDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#functionList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionList(calParser.FunctionListContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#function}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction(calParser.FunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(calParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#parameterList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterList(calParser.ParameterListContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#nempParameterList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNempParameterList(calParser.NempParameterListContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#main}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMain(calParser.MainContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#statementBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatementBlock(calParser.StatementBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(calParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(calParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#binaryArithOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryArithOp(calParser.BinaryArithOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#frag}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFrag(calParser.FragContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#condition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondition(calParser.ConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#compOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompOp(calParser.CompOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#argList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgList(calParser.ArgListContext ctx);
	/**
	 * Visit a parse tree produced by {@link calParser#nempArgList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNempArgList(calParser.NempArgListContext ctx);
}
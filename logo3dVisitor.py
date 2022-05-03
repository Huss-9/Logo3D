# Generated from .\logo3d.g by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logo3dParser import logo3dParser
else:
    from logo3dParser import logo3dParser

# This class defines a complete generic visitor for a parse tree produced by logo3dParser.

class logo3dVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logo3dParser#root.
    def visitRoot(self, ctx:logo3dParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Procs.
    def visitProcs(self, ctx:logo3dParser.ProcsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Res.
    def visitRes(self, ctx:logo3dParser.ResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Mod.
    def visitMod(self, ctx:logo3dParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#NotEqual.
    def visitNotEqual(self, ctx:logo3dParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Or.
    def visitOr(self, ctx:logo3dParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Mul.
    def visitMul(self, ctx:logo3dParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Num.
    def visitNum(self, ctx:logo3dParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#LessEqual.
    def visitLessEqual(self, ctx:logo3dParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#ExprParenthesis.
    def visitExprParenthesis(self, ctx:logo3dParser.ExprParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Div.
    def visitDiv(self, ctx:logo3dParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#GreaterEqual.
    def visitGreaterEqual(self, ctx:logo3dParser.GreaterEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Not.
    def visitNot(self, ctx:logo3dParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Pot.
    def visitPot(self, ctx:logo3dParser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Equal.
    def visitEqual(self, ctx:logo3dParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#And.
    def visitAnd(self, ctx:logo3dParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#GreaterThen.
    def visitGreaterThen(self, ctx:logo3dParser.GreaterThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Mes.
    def visitMes(self, ctx:logo3dParser.MesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Id.
    def visitId(self, ctx:logo3dParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#LessThen.
    def visitLessThen(self, ctx:logo3dParser.LessThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Input.
    def visitInput(self, ctx:logo3dParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Output.
    def visitOutput(self, ctx:logo3dParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Assig.
    def visitAssig(self, ctx:logo3dParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Mesmes.
    def visitMesmes(self, ctx:logo3dParser.MesmesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#Menysmenys.
    def visitMenysmenys(self, ctx:logo3dParser.MenysmenysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#IfElse.
    def visitIfElse(self, ctx:logo3dParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#For.
    def visitFor(self, ctx:logo3dParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#While.
    def visitWhile(self, ctx:logo3dParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logo3dParser#CallFunction.
    def visitCallFunction(self, ctx:logo3dParser.CallFunctionContext):
        return self.visitChildren(ctx)



del logo3dParser
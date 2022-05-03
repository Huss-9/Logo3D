import sys
from antlr4 import *
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser
from visitor import visitor


def main():
    inp = [str(x) for x in sys.argv]
    if len(inp) < 2:
        print("Parametres insuficients en la comanda")
    else:
        arxiu = FileStream(f'./{inp[1]}')
        lexer = logo3dLexer(arxiu)
        token_stream = CommonTokenStream(lexer)
        parser = logo3dParser(token_stream)
        tree = parser.root()
        logovisitor = visitor()
        logovisitor.visit(tree)
        if len(inp) > 2:
            params = [float(x) for x in inp[3:]]
            logovisitor.StartFromFunction(inp[2], params)
        else:
            logovisitor.StartFromFunction("main", [])


if __name__ == "__main__":
    main()

grammar logo3d;
root : (proc)* EOF ;

proc: PROC ID LPAREN (ID | COMMA)* RPAREN IS stmt* END #Procs;

expr : LPAREN expr RPAREN           #ExprParenthesis
    | <assoc = right> expr POT expr #Pot
    | expr MOD expr                 #Mod
    | expr DIV expr                 #Div
    | expr MUL expr                 #Mul
    | expr RES expr                 #Res
    | expr MES expr                 #Mes
    | expr LT expr                  #LessThen
    | expr LE expr                  #LessEqual
    | expr GT expr                  #GreaterThen
    | expr GE expr                  #GreaterEqual
    | expr EQ expr                  #Equal
    | expr NEQ expr                 #NotEqual
    | NOT expr                      #Not
    | expr AND expr                 #And
    | expr OR  expr                 #Or
    | NUM                           #Num
    | ID                            #Id
    ;

stmt : IN ID                                    #Input
    | OUT expr                                  #Output
    | ID ASSIG expr                             #Assig
    | ID MESMES                                 #Mesmes
    | ID MENYSMENYS                             #Menysmenys
    | IF expr THEN (stmt)* (ELSE stmt*)? END    #IfElse
    | FOR ID FROM expr TO expr DO stmt* END     #For
    | WHILE expr DO stmt* END                   #While
    | ID LPAREN (expr | COMMA)* RPAREN          #CallFunction
    ;

MESMES      : '++';
MENYSMENYS  : '--';

AND     : 'and';
OR      : 'or' ;
NOT     : 'not';
ASSIG   : ':=' ;
MES     : '+' ;
RES     : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;
POT     : '^' ;
EQ      : '==' ;
NEQ     : '!=';
LT      : '<' ;
LE      : '<=';
GT      : '>' ;
GE      : '>=';

IN      : '>>' ;
OUT     : '<<' ;

PROC    : 'PROC';
LPAREN  : '(';
RPAREN  : ')';
IS      : 'IS';

FOR     : 'FOR';
FROM    : 'FROM';
TO      : 'TO';

WHILE   : 'WHILE';
DO      : 'DO';

IF      : 'IF';
THEN    : 'THEN';
ELSE    : 'ELSE';
END     : 'END' ;

COMMA   : ',';
NUM     : [0-9]+'.'[0-9]*
        | [0-9]+
        | '.'[0-9]+
        | '-' NUM;

ID      : LETRA (LETRA | NUM | DASH)*;
LETRA   : 'a' .. 'z'
        | 'A' .. 'Z';
DASH    : '_';


COMMENT: '//' ~( '\r' | '\n' )* -> skip ;
WS      : [ \n\r\t]+ -> skip ;
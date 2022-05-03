import sys

from turtle3d import *
from logo3dVisitor import logo3dVisitor


class visitor(logo3dVisitor):
    """
    Diccionari que ens serveix per tenir el nombre de paràmetres de cada funció de la tortuga
    """
    turtle_func_names = {"hide": 0, "show": 0, "home": 0,
                         "up": 1, "down": 1, "left": 1, "right": 1, "forward": 1, "backward": 1,
                         "color": 3}

    def __init__(self):
        """
        Inicialitza la instancia del visitor

        var_dics: Llista que conté las varibales locals dels procediments. Només accedirem a la ultima posició ja que és
        el ultim procediment és el que ens interesa. Quan sortim d'un procediment, borrem la ultima posició de la llista,
        ja que volem borrar les variables locals del ultim procediment

        funcs: Diccionari que conté les funcions amb el seus parametres y el codi a executar de la funció

        turtle: Instancia de la tortuga amb la qual interacturem
        """
        self.var_dics = [{}]
        self.funcs = {}
        self.turtle = Turtle3D()

    def visitRoot(self, ctx):
        """
        Funció que permet visitar tots els procediments i guardar la seva informació per poder fer crides més endavant
        :param ctx: Context del node root
        :return: No retornem res
        """
        # sys.tracebacklimit = 0
        l = list(ctx.getChildren())
        for fill in l:
            self.visit(fill)

    def visitMes(self, ctx):
        """
        Funció que permet evaluar un node que conté una operació de suma entre dos expressions
        :param ctx: Context de la operació suma
        :return: Retornem la suma de les dues expressions
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        return esq + der

    def visitRes(self, ctx):
        """
        Funció que permet evaluar un node que conté una operació de resta entre dos expressions
        :param ctx: Context de la operació suma
        :return: Retornem la resta de les dues expressions
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        return esq - der

    def visitMul(self, ctx):
        """
        Funció que permet evaluar un node que conté una operació de multiplicació entre dos expressions
        :param ctx: Context de la operació multipliació
        :return: Retornem la multiplicació entre les dues expressions després evaluar-les
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        return esq * der

    def visitMod(self, ctx):
        """
        Funció que permet evaluar un node que conte una operació de modul entre dos expressions.
        :param ctx: Context de la operació modul
        :return: Retornem el modul de la primera expressió per la segona expressió
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        if der == 0:
            raise Exception("Modul per zero no permes")
        else:
            return esq % der

    def visitDiv(self, ctx):
        """
        Funció que permet evaluar un node que conté una divisió entre dues expressions. Si intentem una divisió amb 0,
        llençem una excepció.
        :param ctx: Context de la operació divisió
        :return: Retornem la divisió entre les dues expressions.
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        if der == 0:
            raise Exception("Divisió per zero no permesa")
        else:
            return esq / der

    def visitPot(self, ctx):
        """
        Operació que permet evaluar un node que conté el context de una operació poténcia.
        :param ctx: Contexte de la operació de potencia
        :return: Retornem el resultat de elevar la primera expressió a la segona expressió
        """
        l = list(ctx.getChildren())
        esq = self.visit(l[0])
        der = self.visit(l[2])
        return esq ** der

    def visitNum(self, ctx):
        """
        Operació que ens retorna el float contingut en un node
        :param ctx: Context del node que conté un número
        :return: Retornem el float que representa el node
        """
        l = list(ctx.getChildren())
        return float(l[0].getText())

    def visitId(self, ctx):
        """
        Funció que evalua un ID. EL id representa una variable, si la variable existeix en el context del procediment,
        retornem el seu valor, en cas contrari retornem 0.
        :param ctx: Context de un ID
        :return: Retornem el valor de la variable que representa ctx.
        """
        s = ctx.getText()
        if s in self.var_dics[-1]:
            return self.var_dics[-1][s]
        else:
            return 0

    def visitAssig(self, ctx):
        """
        Operació que permet evaluar un node que representa una assignació. Agafem la expressió de la dreta, la evaluem, i
        afegim el valor de la evaluació en el diccionari del últim procediment. En el diccionari, identifiquem la variable
        per el id que tenim a la esquerra del ':='
        :param ctx: Context de una assignació
        :return: No retornem res.
        """
        l = list(ctx.getChildren())
        var = l[0].getText()
        valor = self.visit(l[2])
        self.var_dics[-1][var] = valor

    def visitMesmes(self, ctx):
        """
        Funció que s'encarga d'evaluar l'expressió var++
        :param ctx: Context de l'expressió Mesmes
        :return: No retornem res
        """
        nodes = list(ctx.getChildren())
        var = nodes[0].getText()
        val = self.var_dics[-1][var]
        self.var_dics[-1][var] = val + 1

    def visitMenysmenys(self, ctx):
        """
        Funció que s'encarga d'evaluar l'expressió var--
        :param ctx: Context de l'expressió Menysmenys
        :return: No retornem res
        """
        nodes = list(ctx.getChildren())
        var = nodes[0].getText()
        val = self.var_dics[-1][var]
        self.var_dics[-1][var] = val - 1

    def visitNotEqual(self, ctx):
        """
        Funció que ens permet evaluar si dos expression no són iguals.
        :param ctx: Context de la operació de desigualtat
        :return: Si les expressions no són iguals, retornem 1, en cas contrari retornem 0.
        """
        l = list(ctx.getChildren())
        if self.visit(l[0]) != self.visit(l[2]):
            return 1
        return 0

    def visitEqual(self, ctx):
        """
        Funció que ens permet evaluar si dos expression són iguals.
        :param ctx: Context de la operació de igualtat
        :return: Si les expressions són iguals, retornem 1, en cas contrari retornem 0.
        """
        nodes = list(ctx.getChildren())
        if self.visit(nodes[0]) == self.visit(nodes[2]):
            return 1
        return 0

    def visitLessThen(self, ctx):
        """
        Funció que ens permet evaluar si una expressió és menor que un altre expressió
        :param ctx: Context de la operació de LessThan
        :return: Si la primera expressió és menor estricte, retornem 1, en cas contrari retornem 0.
        """
        nodes = list(ctx.getChildren())
        if self.visit(nodes[0]) < self.visit(nodes[2]):
            return 1
        return 0

    def visitLessEqual(self, ctx):
        """
        Funció que ens permet evaluar si una expressió és menor o igual que un altre expressió
        :param ctx: Context de la operació de LessEqual
        :return: Si la primera expressió és menor o igual que la segona, retornem 1, en cas contrari retornem 0.
        """
        nodes = list(ctx.getChildren())
        if self.visit(nodes[0]) <= self.visit(nodes[2]):
            return 1
        return 0

    def visitGreaterThen(self, ctx):
        """
        Funció que ens permet evaluar si una expressió és major que un altre expressió
        :param ctx: Context de la operació de GreaterThan
        :return: Si la primera expressió és major estricte, retornem 1, en cas contrari retornem 0.
        """
        nodes = list(ctx.getChildren())
        if self.visit(nodes[0]) > self.visit(nodes[2]):
            return 1
        return 0

    def visitGreaterEqual(self, ctx):
        """
        Funció que ens permet evaluar si una expressió és major o igual que un altre expressió
        :param ctx: Context de la operació de GreaterEqual
        :return: Si la primera expressió és major o igual que la segona, retornem 1, en cas contrari retornem 0.
        """
        nodes = list(ctx.getChildren())
        if self.visit(nodes[0]) >= self.visit(nodes[2]):
            return 1
        return 0

    def visitAnd(self, ctx):
        """
        Funció que s'encarga d'evaluar una expressió AND
        :param ctx: Context de la expressió AND
        :return: Retornem 1 si es compleix el AND, en cas contrari retornem 0
        """
        nodos = list(ctx.getChildren())
        eval1 = self.visit(nodos[0])
        eval2 = self.visit(nodos[2])
        if (-1e-6 <= eval1 <= 1e-6) or (-1e-6 <= eval2 <= 1e-6):
            return 0
        return 1

    def visitOr(self, ctx):
        """
        Funció que s'encarga d'evaluar una expressió OR
        :param ctx: Context de la expressió OR
        :return: Retornem 1 si es compleix el OR, en cas contrari retornem 0
        """
        nodos = list(ctx.getChildren())
        eval1 = self.visit(nodos[0])
        eval2 = self.visit(nodos[2])
        if (-1e-6 <= eval1 <= 1e-6) and (-1e-6 <= eval2 <= 1e-6):
            return 0
        return 1

    def visitNot(self, ctx):
        """
        Funció que s'encarga d'evaluar una expressió NOT
        :param ctx: Context de la expressió NOT
        :return: Retornem 1 si la expressió es falsa, en cas contrari retornem 1
        """
        nodos = list(ctx.getChildren())
        eval_ = self.visit(nodos[1])
        if -1e-6 <= eval_ <= 1e-6:
            return 1
        return 0

    def visitExprParenthesis(self, ctx):
        """
        Funció que s'encarrega de evaluar una expressió entre parentesis
        :param ctx: Context de la expressió entre parentesis
        :return: Valor de la evaluació de la expressió encapsulada
        """
        nodos = list(ctx.getChildren())
        return self.visit(nodos[1])

    def visitInput(self, ctx):
        """
        Operació que ens permet evaluar un node que representa llegir una variable per la entrada. Llegim el valor per la
        entrada y el guardem en les variables del procediment en el que ens trobem (ultima posició del diccionari)
        :param ctx: Context de la operació Input
        :return:No retornem res.
        """
        nodes = list(ctx.getChildren())
        var_name = nodes[1].getText()
        val = float(input("<?>"))
        self.var_dics[-1][var_name] = val

    def visitOutput(self, ctx):
        """
        Operació que ens permet treure per la sortida el valor de una expressió
        :param ctx: Context de la operació output
        :return: No retornem res.
        """
        nodes = list(ctx.getChildren())
        val = self.visit(nodes[1])
        print(val)

    def visitIfElse(self, ctx):
        """
        Operació que permet evaluar un node que representa el statement IF ELSE. També ens permet evaluar només el IF en
        cas que no tinguem un ELSE.
        :param ctx: Context del statment If Else
        :return: No retornem res.
        """
        nodes = list(ctx.getChildren())
        val = self.visit(nodes[1])
        nom = nodes[3].getText()
        i = 3
        while nom != 'ELSE' and nom != 'END':  # trobem el index del node que conte ELSE o END, el que trobem abans
            i += 1
            nom = nodes[i].getText()
        if not (-1e-6 <= val <= 1e-6):
            for st in nodes[3:i]:
                self.visit(st)
        else:
            for st in nodes[i:-1]:
                self.visit(st)

    def visitWhile(self, ctx):
        """
        Operació que ens permet evaluar un node que representa el statement WHILE. Cada cop anem evaluant el fill que
        representa la condició del while, i si no és un valor entre (-1e-6, 1e-6) evaluem els statements del cos del while.
        En cas contrari parem. La evaluació dels statements del cos del while s'encarregan d'actualitzar els valors de les
        variables.
        :param ctx: Context del statement WHILE
        :return: No retornem res.
        """
        nodes = list(ctx.getChildren())
        expression = self.visit(nodes[1])
        while not (-1e-6 < expression < 1e-6):
            for stat in nodes[3:-1]:
                self.visit(stat)
            expression = self.visit(nodes[1])

    def visitFor(self, ctx):
        """
        Funció que ens permet evaluar un statement que representa un FOR. Treiem els valors que limiten el for, i evaluem
        el cos del FOR el número de vegades que indiquen els limits. Pot ser que el número de vegades que executem el cos
        del FOR variï a causa de la evaluació del cos es canviï el valor de la variable que representa les iteracions del
        FOR.
        :param ctx: Context de la operació FOR
        :return: No retornem res.
        """
        l = list(ctx.getChildren())
        var_name = l[1].getText()
        ini = self.visit(l[3])
        self.var_dics[-1][var_name] = ini
        lim = self.visit(l[5])
        while self.var_dics[-1][var_name] <= lim:
            for stat in l[7:-1]:  # Executem tots els statements dins del for
                self.visit(stat)
            self.var_dics[-1][var_name] += 1  # Variable de control del for
        del self.var_dics[-1][var_name]  # Borrem la variable de control del for

    def visitProcs(self, ctx):
        """
        Operació que s'executa quan trobem la declaració d'un procediment en el codi. Aquesta funció s'encarrega de mirar
        que no existeixi el procediment previament i que no hi hagin parametres repetits. Si tot és correcte, afegim en
        el diccionari de funcs els parametres y els statements que representen el cos de la funció, fent servir com a key
        el nom de la funció. Això ens sera útil quan tinguem que fer crides a funcions.
        :param ctx: Context que representa la declaració de una funció
        :return: No retornem res
        """
        l = list(ctx.getChildren())
        name = l[1].getText()
        if name in self.funcs:
            raise Exception(f'Ja existeix el procediment{name}')
        else:
            stop = 3
            params = []
            l = list(filter(lambda x: x.getText() != ',', l))   # Filtrem els nodes que contenen comes
            while l[stop].getText() != ')':                     # Trobem el node on esta el següent parentesis per saber
                val = l[stop].getText()                         # els nodes dels paràmetres
                if val in params:
                    raise Exception(f"Error: parametre {val} es duplicat")
                else:
                    params.append(val)                          # Afegim el nom del paràmetre en una llista
                stop += 1
            stop += 2
            self.funcs[name] = (params, l[stop:-1])         # Guardem funcs[name_proc] = (nom_parametres, codi_del_proc)

    def visitCallFunction(self, ctx):
        """
        Operació que ens permet evaluar un node que representa la crida a un procediment. Si no existeix el procediment,
        ho indiquem amb una excepció. A més comprovem que el nombre de parametres aportats és el mateix que tenim
        guardats en el diccionari funcs. En cas que la funció sigui una funció relacionada amb la classe turtle3d, cridem
        directament a la seva funció sense necessitat de extreure el codi de la funció del diccionari de funcs. En cas que
        sigui un procediment definit en el codi, carreguem el noms dels seus parametres i els statments que representen el
        cos de la funció. Un cop fet això, afegim un nou diccionari en var_dics, i en aquest nou diccionari carreguem els
        valors dels parametres. Després, simplement evaluem els statements del cos del funció
        :param ctx: Context que representa la crida a una funció
        :return: No retornem res
        """
        l = list(ctx.getChildren())
        name = l[0].getText()
        if name not in self.funcs and name not in self.turtle_func_names:
            raise Exception(f'No existeix la funcio {name}')
        else:
            l = list(filter(lambda x: x.getText() != ',', l))   # Filtrem les comes de la crida
            if name in self.turtle_func_names:                  # Mirem si es tracta de una funció de la tortuga
                num_params = self.turtle_func_names[name]
                if len(l) - 3 != num_params:                    # Mirem que tenim el nombre exacte de parametres
                    raise Exception(
                        f'Nombre de parametres introduits es diferent que el nombre de parametres de la funcio {name}')
                else:
                    vals = [self.visit(p) for p in l[2:-1]]     # Obtenim els valors de totes les variables passades com paràmetres
                    method = getattr(self.turtle, name)         # Obtenim el mètode de la classe tortuga que representa name
                    method(*vals)                               # Cridem el mètode obtingut amb els valors dels paràmetres
            else:                                               # En cas que siguem una funció declarada en el arxiu l3d
                (params, codi) = self.funcs[name]
                if len(l) - 3 != len(params):
                    raise Exception(
                        f'Nombre de parametres introduits es diferent que el nombre de parametres de la funcio {name}')
                else:
                    dic_aux = {}
                    for i, var in enumerate(params):
                        """
                        Creem un nou diccionari amb els valors del paràmetres passats, aquest diccionari ens servirà per
                        tenir les variables locals del nou procediment a cridar
                        """
                        dic_aux[var] = self.visit(l[i + 2])
                    self.var_dics.append(dic_aux)   # Afegim el nou diccionari en la ultima posició de var_dics
                    for st in codi:                 # Executem el codi del procediment
                        self.visit(st)
                    self.var_dics.pop()             # Borrem el últim diccionari ja que hem sortit del procediment

    def StartFromFunction(self, name, pars=[]):
        """
        Operació que ens permet executar un procediment si li passem el nom del procediment i els seus parametres com una
        llista de flaots. Aquesta funció principalment ens serveix per fer crides des de logo3d.py
        :param name: Nom de la funció a cridar
        :param pars: Llista de floats que conté els paràmetres del funció definida per name
        :return: No retornem res
        """
        if name not in self.funcs:
            raise Exception(f'No existeix la funcio {name}')
        else:
            if name in self.turtle_func_names:  # Mirem si es tracta de una funció de la tortuga
                num_params = self.turtle_func_names[name]
                if len(pars) != num_params:  # Mirem que tenim el nombre exacte de parametres
                    raise Exception(
                        f'Nombre de parametres introduits es diferent que el nombre de parametres de la funcio {name}')
                else:
                    method = getattr(self.turtle, name)  # Obtenim el mètode de la classe tortuga que representa name
                    method(*pars)
            else:
                (params, codi) = self.funcs[name]
                if len(pars) != len(params):
                    raise Exception(
                        f'Nombre de parametres introduits es diferent que el nombre de parametres de la funcio {name}')
                else:
                    dics_aux = {}               #Fem el mateix que la funció visitCallFunction però per crides externes
                    for i, var in enumerate(params):
                        dics_aux[var] = pars[i]
                    self.var_dics.append(dics_aux)
                    for st in codi:
                        self.visit(st)
                    self.var_dics.pop()



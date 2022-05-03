
# Logo3D 
Hasnain Shafqat\
Grup 13\
Llenguatges de programació
  
<h2 id="taula">  
Taula de Continguts  
</h2>   

- [Introducció a Logo3D i com començar](#introduccio-a-logo3d)  
- [Sintaxi de Logo3D](#sintaxi-de-logo3d)  
   - [Variables](#variables)  
   - [Entrada i sortida](#entrada-i-sortida)  
		- [Entrada](#entrada)  
        - [Sortida](#sortida)  
   - [Assiganció](#assignacio)  
   - [Operadors i expressions](#operadors-i-expressions)  
   - [Condicionals](#condicionals)  
   - [Bucles](#bucles)  
       - [WHILE](#while)  
       - [FOR](#for)  
   - [Procediments](#procediments)  
       - [La tortuga i els procediments predefenits](#predefinits)  
       - [Declaració de procediments no predefinits](#no-definits)  
- [Programes de Logo3D](#programes-de-logo3d)  
   - [Excepcions en els programes](#excepcions)  
- [Instalació de Logo3D](#instalacio)  
- [Execució de programes en Logo3D](#execucio)
  
<h2 id="introduccio-a-logo3d">  
Introducció a Logo3D i com començar  
</h2>  

Logo3D és un llenguatge de programació que es basa en el llenguatge Logo que va ser introduït l'any 1967 per ensenyar als infants programació i pot usar-se per ensenyar la majoria dels principals conceptes de la programació, ja que proporciona suport per a maneig de llistes, arxius i entrada/sortida.  
  
Una característica molt explotada de Logo és poder produir «gràfiques tortugues», és a dir, poder a donar instruccions a una tortuga virtual que és usada per crear dibuixos, en algunes versions de Logo és un triangle, en altres té la figura d'una tortuga vista des de dalt. Aquesta tortuga es maneja mitjançant paraules que representen instruccions, per exemple:

```logo  
forward 100 (la tortuga camina cap a endavant 100 pasos)  
turnright 90 (la tortuga es gira 90º a la dreta)  
turnleft 30 (la tortuga es gira 30º a la esquerra )  
```  

Nosaltres ens basarem en Logo per crear Logo3D, amb la gran diferència del fet que ara la tortuga pintarà en 3D. És a dir, afegirem més instruccions com up, down per poder recorre tot l'espai de 3 dimensions. Cal recalcar que no implementarem totes les funcionalitats de Logo, i limitarem bastant les funcionalitats del nostre Logo3D. Una limitació molt gran que afegirem és que només interactuarem amb variables de tipus float. No tindrem ni llistes ni cap mena d'estrucutra de dades. A continuació explicarem les instruccions i la sintaxi de Logo3D.
  
<h2 id="sintaxi-de-logo3d">  
Sintaxi de Logo3D  
</h2>  

La sintaxi de Logo3D és bastant simple i fàcil d'entendre. Com veurem a continuació no tenim moltes instruccions, aleshores és bastant ràpid d'aprendre a interactuar amb ell. Explicarem la sintaxi bàsica i la relacionada amb la tortuga. És a dir, podem crear programes que no tinguin res a veure amb crear gràfiques tortugues. Podem tenir programes que calculin el factorial recursivament, el mínim comú divisor fent ús de l'algoritme d'Euclides, etc. Primer explicarem les instruccions bàsiques amb les quals podem fer programació general. I després, en l'apartat de la sintaxi dels procediments explicarem els procediments relacionats amb la tortuga 3D.
  
<h3 id="variables">  
Variables  
</h3>  

Les variables en Logo3D són totes floats, cosa que ens permet no tenir errors de tipus. A més cal indicar que podem fer servir una variable en qualsevol part d'un procediment. És a dir, si per exemple tenim el següent codi:  
  
```logo  
PROC main() IS  
    >> valor 
    IF valor < 5.0 THEN 
        x := 0 
    ELSE 
        x := 10 
    END 
    << x
END  
```  

Podem veure que estem declarant la variable x en el bloc del condicional IF  ELSE, però, després estem traient-la per la sortida en un bloc més extern. Totes les variables han de començar per una lletra, és irrellevant si la lletra és minúscula o majúscula. Podem tenir números i barra baixa  ( _ ) en el nom de les variables. Uns exemples de noms vàlids de variable serien ```var, var_1, var__, var2_, Var```. Els noms de les variables en Logo3D són case  sensitive. Per exemple, podem tenir dues variables, ''foo, Foo'', que els seus noms són idèntics si no fos per la primera lletra, i serien variables diferents. Un incís que cal fer sobre variables és que si intentem accedir a una variable no declarada, Logo3D simplement retorna un 0, quan el que seria normal és treure un error. Finalment, recalcar que no tenim variables globals, ni podem accedir a variables d'altres procediments.

<h3 id="entrada-i-sortida">  
Entrada i sortida  
</h3>  
  
Les operacions d'entrada i sortida són semblants a altres llenguatges, però amb la limitació que només podem llegir o escriure floats.
  
<h4 id="entrada">  
Entrada  
</h4>  
  
L'entrada té el següent format: ````>> x````, on x seria la variable on volem guardar el valor a llegir. Una cosa bona de Logo3D és que no cal haver declarat la variable x per guardar el valor a llegir. L' operació de llegir ja s'encarrega de crear la variable i guardar el valor llegit.   
  
Un incís important és que cada cop que introduïm un valor per l'entrada hem de clicar la tecla ENTER per poder dir-li al nostre programa que ara introduirem el següent valor. Ho hem de fer sempre, és independent a la forma d'introduir l'entrada (mitjançant arxiu de text o mitjançant terminal). Perquè sigui més fàcil d'entendre podem mirar el següent programa, on necessitem llegir dos valors.

```  
//ProgramaExemple2.l3d  
  
PROC main() IS  
    >> valor1 >> valor2 
    euclides(valor1, valor2)
END  
```  

La forma correcta d'introduir els valors seria la següent:  
  
```python3 logo3d.py ProgramaExemple2.l3d``` #Execució del programa anterior

```  
20  
5  
```  

Aleshores, queda aclarit que per cada valor nou que volem introduir, ho hem de fer en una nova línia. 
  
<h4 id="sortida">  
Sortida  
</h4>  
  
Ara, anem a explicar com s'escriuen valors pel canal de sortida. Logo3D ens permet imprimir tota mena d'expressions. Les expressions van des d'operacions matemàtiques fins variables que contenen valors. Per treure un valor per la sortida hem de fer servir l'operador ```<<```. A continuació tenim exemples vàlids de com treure valors per la sortida:  

```  
<< var  
<< 2*5 - var + 10  
<< 2 == 3  
<< 2 < 5  
<< x and y  
```  

Com podem apreciar podem treure la sortida tot el que sigui una expressió o variable. Però no tenim la possibilitat d'imprimir cadenes de caràcters per la sortida. Si ho considereu oportú us deixem la possibilitat d'implementar-ho com una extensió, però la nostra versió Logo3D no ho implementarà.  
  
<h3 id="assignacio">  
Assignació  
</h3>  
  
En logo3D per assignar un valor a una variable hem de fer servir ```:=```. A l'esquerra de l'operador d'assignació tindrem el nom de la variable a la qual volem assignar el valor de l'expressió a la dreta del ```:=```. L'expressió a la dreta pot o no contenir altres variables, o l'expressió pot ser el nom d'un altre variable, que en aquest cas voldria dir que estem fent una còpia d'aquella variable. Com podem veure, l'operador d'assignació no té molt més, és molt semblant a altres llenguatges d'alt nivell. Alguns exemples de l'operador d'assignació en Logo3D són els següents:  

```  
x := 5  
y := x + 3.14  
temp := 4 + 5 - y * 8 + 2 ^ x  
delta := (x == y) * z  
```  
  
<h3 id="operadors-i-expressions">  
Operadors i expressions  
</h3>  
  
En les següents parts del document explicarem condicionals, bucles i procediments. Però, abans hem de fer una introducció els operadors que podem usar en els condicionals i bucles. Els operadors en general s'encarreguen de comparar dues expressions. Però, què definim com una expressió? Una expressió en Logo3D pot ser moltes coses, a continuació podem veure les possibles definicions d'una expressió, les quals estàn ordrenades segons l'ordre de prioritat: 
* (Expressió)  
* Expressió ```p`^``` Expressió  
* Expressió ```%``` Expressió  
* Expressió ```/``` Expressió  
* Expressió ```*``` Expressió  
* Expressió ```-``` Expressió  
* Expressió ```+``` Expressió  
* Expressió ```==``` Expressió  
* Expressió ```!=``` Expressió  
* Expressió ```<``` Expressió  
* Expressió ```<=``` Expressió  
* Expressió ```>``` Expressió  
* Expressió ```>=``` Expressió 
* ```not``` Expressió
* Expressió ```and``` Expressió
* Expressió ```or``` Expressió
* Un Nombre  
* Una variable 
  
Podem apreciar que la definició d'expressió és recursiva, és a dir, una expressió pot estar formada per altres expressions més petites, on el cas més petit d'expressió seria un nombre o una variable. De certa forma podríem considerar que un nombre o una variable serien àtoms, ja que no tenim expressió més petita. Però, podem observar que una expressió pot ser un operador que compara dues expressions. Per tant, amb aquesta propietat recursiva en la definició d'una expressió, ens permet fer servir expressions realment complexes en els condicionals i bucles. 
  
Una propietat a destacar de Logo3D és la de posar expressions matemàtiques en els condicionals. Per exemple podríem tenir el següent programa:  

```  
>> var  
IF 4 - 5 ^ var THEN  
    << 1
ELSE  
    << 2
END  
```  

En Logo3D, si una expressió dona un valor que no estigui en l'interval (-1e-6, 1e-6) es considera com vertader, en cas contrari, es considera Fals. Aleshores, en el programa d'exemple, depenent del valor que tenim a l'entrada, traurem per la sortida un 1 o un 2. Els operadors de Logo3D, sempre retornen 0 o 1, per tant si retornem 0 (dins de l'interval mencionat) és fals, i 1 és vertader. Això ens permet fer coses com tenir expressions com ```(valor1 < valor2) * valor1 + valor2``` en les assignacions i els condicionals. Per exemple, l'expressió anterior ens permet sumar la variable valor1 a valor2 només si valor1 és més petita que valor2. En Logo3D, les expressions que usem en els condicionals no estan limitades als operadors de comparació, sinó que podem fer servir qualsevol expressió que ens convingui.  
  
<h3 id="condicionals">  
Condicionals  
</h3>  
  
Els condicionals en Logo3D són molt semblants a altres llenguatges de programació, però tenim petites   diferències de sintaxi. La sintaxi del condicional en Logo3D és la següent:  

```  
//US DEL CONDICIONAL AMB ELSE  
IF expressió THEN  
    BLOC_CODI_IF 
ELSE  
    BLOC_CODI_ELSE
END  
```  

L'expressió del IF pot ser qualsevol expressió que hem mencionat en l'apartat d'Operadors i expressions. L'expressió del IF no es limita a només expressions que contenen operands de comparació, sinó que podem fer servir qualsevol definició d'expressió mencionada. Si l'expressió del IF és certa, no és a l'interval (-1e-6, 1e-6), executem el codi que va des de THEN fins a ELSE o fins a END. La raó d'això és que podem tenir un IF sense necessitat de tenir ELSE. Per tant, en cas que no tinguem bloc ELSE, la sintaxi del condicional IF seria la següent:  

```  
//US DEL CONDICIONAL SENSE ELSE  
IF expressió THEN  
    BLOC_CODI_IF
END  
```  

Cal recalcar que sempre que volem acabar el condicional hem d'escriure un END per indicar que acaba el condicional. Si tenim un bloc ELSE en el condicional hem de ficar END després d'haver escrit els statements del bloc de codi del ELSE. És important que si tenim un bloc ELSE, no ficar el END abans de ELSE. Si fem això, l'intèrpret detecta que el IF acaba on posa el END, i quan intenta llegir el ELSE no troba cap statement en la gramàtica per poder fer match. A continuació tenim un exemple de l'ús erroni dels condicionals:

```  
//US ERRONI DEL CONDICIONAL  
IF expressió THEN  
    BLOC_CODI_IF
END  
ELSE  
    BLOC_CODI_ELSE
END  
```  

Un cop dit això, anem a explicar els bucles.  
  
<h3 id="bucles">  
Bucles  
</h3>  
  
En Logo3D, tenim dos tipus de bucles, els Whiles i els Fors. Explicarem per sobre la seva sintaxi, ja que tot el que té relació amb les condicions dels bucles, ja ha sigut mencionat en l'apartat dels condicionals.  
  
<h4 id="while">  
WHILE  
</h4>  
  
La sintaxi del WHILE en Logo3D és la següent:  

```  
WHILE expressió DO  
    BLOC_CODI_WHILE
END  
```  

Podem veure que per diferenciar l'expressió del bloc de codi que hem d'executar en el bucle, fiquem un DO al mig. En el bloc de codi del While, podem tenir tota mena de statements, els quals inclourien altres bucles. Finalment si volem marcar el final del bloc de codi del While, hem d'escriure un END que marcarà el final. Cal dir que no fa falta que el END estigui en una línia nova, millor dit, no tenim per què afegir salts de línia en el nostre codi. Un exemple de codi perfectament vàlid seria el següent: ```PROC main() IS i := 0 WHILE i < 5 DO i := i + 1 END END```. Però, recomanem afegir salts de línia per tenir programes més bonics d'entendre i que sigui fàcil treballar amb ells. Un incís important és que la variable de control del WHILE ha de ser prèviament declarada per poder-se usar en el WHILE. A més, podem apreciar que el bucle While té les mateixes capacitats que el While d'altres llenguatges de programació. Però, com és el FOR? Anem a veure.  
  
<h4 id="for">  
FOR  
</h4>  
  
Pel que fa al FOR, la sintaxi és la següent:  

```  
FOR i FROM expressió_ini TO expressió_fi DO   
    BLOC_CODI_FOR  
END  
  
//EXEMPLE FOR  
FOR i FROM 1 TO 5 DO   
    i := i + 1   
    << i 
END  
```  

Podem apreciar que la sintaxi és bastant semblant al for d'altres llenguatges, però hi ha petites diferències. La gran diferència, a part de la sintaxi, és que no podem indicar quan ha d'incrementar la variable de control en cada iteració del FOR. És a dir, tenim una part que indica que el valor inicial del variable de control, i tenim una altra part que indica el valor màxim que pot tenir. Més concretament estem parlant d'expressió_ini i expressió_fi. Com el seu nom indica, aquests valors, són expressions, i no tenen per què ser valors numèrics o noms de variables. Un cop assignat els límits de la variable de control, afegim un DO per indicar que comença el bloc de codi del for. Finalment, quan volem marcar el fí del bloc de codi del for, escrivim un END. Com hem dit anteriorment, no cal fer salts de línia, però recomanem el seu ús per facilitar la vida a altres usuaris.
  
<h3 id="procediments">  
Procediments  
</h3>  
  
En Logo3D només procediments i tenim de dos tipus, els predefinits del llenguatge i els definits per l'usuari.  
  
<h4 id="predefinits">  
La tortuga i els procediments predefenits  
</h4>  
  
En Logo3D podem fer la majoria de coses que permetria un llenguatge imperatiu, però, a més tenim l'habilitat de crear gràfics 3D. Per fer aquests gràfics tenim la tortuga. Aquesta tortuga, abans de fer qualsevol operació sobre ella, és a l'origen de coordenades mirant cap a les x positives i té el color vermell. Però, podem aplicar diverses operacions sobre ella per desplaçar-la, girar-la, fer que deixi de pintar, etc. Per saber la direcció de visió de la tortuga tenim dos angles, l'angle vertical, i l'angle horitzontal. A continuació tenim els procediments predefinits sobre la tortuga:
* ```show()```: Procediment podem fer que la tortuga torni a pintar en l'escena si prèviament hem fet que deixi de pintar.  
* ```hide()```: Procediment que permet que la tortuga deixi de pintar.  
* ```home()```: Procediment que permet moure-la tortuga a l'origen de coordenades, sense canviar la direcció en la qual estava mirant.  
* ```up(angle)```: Procediment que li donem un angle en graus, ens incrementa l'angle vertical afegint-li aquest nou angle.  
* ```down(angle)```:Procediment que li donem un angle en graus, ens decrementa l'angle vertical restant-li aquest nou angle.  
* ```left(angle)```:Procediment que li donem un angle en graus, ens incrementa l'angle horitzontal afegint-li aquest nou angle.  
* ```right(angle)```:Procediment que li donem un angle en graus, ens  decrementa l'angle horitzontal restant-li aquest nou angle.  
* ```forward(desp)```:Procediment que li donem una distància, ens desplaça la tortuga aquesta distància en la seva direcció de visió. Si la tortuga té l'habilitat de pintar activada, quan desplacem la tortuga pintem el  
rastre del desplaçament. 
* ```backward(desp)```:Procediment que li donem una distància, ens desplaça la tortuga aquesta distància en la direcció contrària a la seva direcció de visió. Si la tortuga té l'habilitat de pintar activada, quan desplacem la tortuga pintem el rastre del desplaçament. 
* ```color(r, g, b)```: El color original de la tortuga és vermella, amb aquest procediment podem canviar el color amb què pinta la tortuga. Per canviar el color, li hem de passar les tres components RGB del nou color en rang (0, 1). 
    
A continuació tenim un exemple de codi que usa aquestes funcions en Logo3D: 

```  
PROC quadrat_blau(mida) IS  
    color(0.2, 0.2, 1) 
    FOR i FROM 1 TO 4 DO 
         forward(mida) 
         left(90) 
    END
 END  
```  

Aquest codi ens dibuixa un quadrat de color blau. Podem veure que no ens cal cap sintaxi especial per cridar les funcions de la tortuga. Un cop explicats els procediments predefinits, a continuació tenim com declarar procediments propis. 
  
<h4 id="no-definits">  
Declaració de procediments no predefinits  
</h4>  
  
La sintaxi per definir procediments és la següent:  

```  
PROC NOM_PROCEDIMENT(parametres) IS  
    BLOC_CODI_FUNCIO
END  
```  

Per declarar un procediment en Logo3D, hem de començar amb un PROC seguit el nom del procediment. Després, escrivim el nom dels paràmetres entre parèntesis i separats per comes. En cas que no tinguem paràmetres, només escrivim els parèntesis sense paràmetres. Després dels paràmetres tocaria escriure un IS que marcaria l'inici del cos del procediment. Un cop hem escrit el codi del procediment, hem de ficar un END per marcar el fi de la declaració del procediment. A continuació tenim un exemple d'un procediment que calcula el mínim comú divisor de dos nombres. És important veure que no retornem res, ja que són procediments, no funcions.  

```  
//EXEMPLE PROCEDIMENT  
PROC euclides(a, b) IS  
    WHILE a != b DO 
        IF a > b THEN 
            a := a - b 
        ELSE 
            b := b - a 
        END 
    END 
    << a
END  
```  

Us preguntareu, i es pot fer ús de la recursivitat? La resposta és sí, ja que la recursivitat bàsicament és un procediment que es crida a si mateixa, la qual cosa no tenim problema, ja que cada crida té les seves variables locals ben diferenciades i no tenim cap problema en fer crides recursives. L'únic limitant que tenim és que no podem retornar variables. A continuació tenim un exemple de recursivitat fent servir la tortuga que pinta una espiral:  

```  
PROC cercle(mida, costats) IS  
    FOR i FROM 1 TO costats DO 
        forward(mida) 
        left(360 / costats) 
    END
END  
  
PROC espiral(cercles) IS  
    IF cercles > 0 THEN 
        cercle(1, 12) 
        up(5) 
        espiral(cercles - 1) 
    END
END  
  
PROC main() IS  
    espiral(5)
END  
```  

<h2 id="programes-de-logo3d">  
Programes de Logo3D  
</h2>  
  
Els programes de Logo3D es consten bàsicament d'un conjunt de procediments. Tot programa de logo3D ha de tenir un main pel fet que en cas que no indiquem per quin mètode hem de començar a executar el nostre programa, l'intèrpret s'encarrega de començar pel procediment main, el qual no rep paràmetres. 
  
Tot procediment de Logo3D consta de'un conjunt de statements. En Logo3D tenim els següents statements:  
* Lectura de valors del canal d'entrada  
* Escriptura de valors pel canal de sortida  
* L'assignació d'expressions a variables
* Augment en una unitat el valor d'una variable (```var++```)
* Decrement en una unitat a el valor d'una variable (```var--```)
* El condicional IF ELSE  
* El bucle WHILE  
* EL bucle FOR  
* Cridar un procediment  
  
<h3 id="excepcions">  
Excepcions en els programes  
</h3>  
  
A l'hora de programar, els programadors solen cometre molts errors i els quals s'han de tractar per tal d'avisar el programador. En Logo3D hem tractat els erros més bàsics i són els següents:  
* Divisó per zero  
* Crida a un procediment no definit  
* Redeclaració d'un procediment  
* Nom de paràmetres introduïts diferent del nombre de paràmetres del procediment  
* Paràmetres repetits en la declaració del procediment  
  
<h2 id="instalacio">  
Instal·lació de Logo3D  
</h2> 
 
Per instal·lar Logo3D primer que res hem d'instal·lar antlr4 en el nostre ordinador. Per fer aquesta instal·lació recomanem mirar la [pàgina oficial](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) per descarregar i instal·lar antlr4. Un cop tenim instal·lat antlr4 baixem Logo3D.zip i el descomprimim. Veurem que tenim els següents arxius:
  
* Logo3d.py  
* logo3d.g  
* visitor.py  
* turtle3d.py  
* requirements.txt  
* README.md  
* diversos arxius de prova amb extensió ```l3d```  
  
Obrim la terminal on tenim instal·lat el antlr4, pot ser la terminal de Windows, la del subsistema, etc. Però és important obrir la terminal d'aquell sistema on tenim instal·lat antlr4. A continuació, executem la següent comanda en la terminal per poder instal·lar els paquets necessaris:

```  
python -m pip install -r requirements.txt  
```  

Un cop tenim tots els requeriments instal·lats, generarem els arxius necessaris de la gramàtica fent ús de la següent comanda: 

```  
antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g  
```  

Ara, ja tenim Logo3D preparat per executar programes amb extensió ```l3d```. Anem a veure com ho fem per executar-los.  
  
<h2 id="execucio">  
Execució de programes en Logo3D  
</h2> 

Els arxius dels programes en Logo3D tenen extensió ``l3d```. Per tant, si volem executar un programa en Logo3D, requerim tenir instal·lat Python. La sintaxi per executar un programa amb extensió ''l3d'' és la següent: 

```
python3 logo3d.py nom_programa.l3d
```
  
Aquesta comanda l'hem d'executar en la terminal. A més, si volem que l'intèrpret comenci per un procediment en concret podem afegir el nom del mètode i els paràmetres. A continuació tenim un exemple:
  
```
python3 logo3d.py programa.l3d quadrats 10 20
```

#isinstance() mi dice che tipo di variabile e il mio dato
x = isinstance(5, int)

# qua mi dice che se hello e una di queste variabili mi stampa vero 
x = isinstance("Hello", (float, int, str, list, dict, tuple))
# qua creiamo una nuova variabile dico che class e di tipo my0bj e contiene l'elemento john , con isinstance chiedo se y e di tipo my0bj 
class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
#condizioni 
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

# comando if , se mettiamo un if non corretta ci darà errore 
a = 33
b = 200
if b > a:
  print("b is greater than a")

  # Elif, se le condizioni precedenti non erano vere, prova questa condizione 
c = 33
d = 33
if c > d:
  print("c is greater than d")
elif c == d:
  print("c and d are equal")

  #La parola chiave else cattura tutto ciò che non è catturato dalle condizioni precedenti.
  e = 200
f = 33
if e > f:
  print("f is greater than e")
elif e == f:
  print("e and f are equal")
else:
  print("e is greater than f")

#Mano corta , Se hai solo un'istruzione da eseguire, puoi metterla sulla stessa riga dell'istruzione if.
#if g > h: print("g is greater than h")

#Posso avere più istruzioni sulla stessa riga 
#La parola chiave and è un operatore logico e viene utilizzata per combinare istruzioni condizionali
l = 200
m = 33
n = 500
if l > m and n > l:
  print("Both conditions are True")

#Verifica se aè maggiore di b, OPPURE se a è maggiore di c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  #Puoi avere ifistruzioni all'interno ifdi istruzioni, questo è chiamato istruzioni nidificate if .

  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

  #if le istruzioni non possono essere vuote, ma se per qualche motivo hai una ifdichiarazione senza contenuto, inseriscila passper evitare di ottenere un errore.
    # mi permette di fare una condizione senza scrivere il print 
 k = 33
b  = 200

if b > k:
  pass
# AAL_20Z

Zadanie
Przedmiotem analizy jest tablica mieszająca: tablica przechowuje rekordy zawierające napisy. Długość
tablicy jest ograniczona arbitralnie przez pewną stałą K. Dla danego napisu s obliczamy k=M(s) gdzie
M() jest funkcją mieszającą i umieszczamy strukturę reprezentującą napis w tablicy mieszającej: H[k].
W przypadku kolizji funkcji mieszającej (H[k] zajęte) reprezentujące napis s struktury danych
zapisywane są w sposób alternatywny zobacz warianty). Przedmiotem implementacji powinno być:
dodanie i usunięcie elementów w H[]. Wybór funkcji mieszającej M(s) do decyzji projektanta.

Testy przeprowadzić dla: sztucznie wygenerowanych słów, generator ma posługiwać się tablicą
prawdopodobieństw wystąpienia danej litery na początku slowa (początek słowa) oraz litery po
poprzedzającej literze, (spacja, kropka, przecinek, itp. traktowane są jako litera specjalna "koniec
słowa"). Prawdopodobieństwa należy uzyskać z próbki tekstu polskiego.

  - W12:
W przypadku kolizji funkcji mieszającej reprezentujące napis s struktury danych zapisywane są w
drzewie binarnym, którego korzeń to H[k].

  - W22:
Zastosować dwie znacząco różne funkcje mieszające.

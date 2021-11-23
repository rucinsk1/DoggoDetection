# DoggoDetector
Aplikacja służąco do rozpoznawania ras psów. Po wgraniu zdjęcia aplikacja rozpozna rasę oraz poda o niej podstawowe informacje. Aplikacja wykorzystuje pythona, salesforce'a oraz serwisy zapewnione przez Azure (CustomVision oraz Storage).

## Developerzy
- [Kalata Krzysztof](https://github.com/KrzysztofKalata)
- Ruciński Konrad

## Link do prezentacji


## Architektura + stos technologiczny

- **Python** - język programowania odpowiedzialny za stworzenie aplikacji oraz obsługę pobranego modelu. Najważniejsze biblioteki to flask, tensorflow.
- **Salesorce** - platforma oferująca dostęp do aplikacji końcowej, to w niej wgrywamy zdjęcie które jest zapisywane i przekazywane do modułu Pythona
## Opis funkcjonalności
- rozpoznawanie rasy psa,
- pozyskiwanie informacji na temat rozpoznanej rasy.

## Proces tworzenia
- pobranie oraz otagowanie zdjęć,
- wytrenowanie modelu,
- pobranie modelu oraz stworzenie aplikacji wykorzystującej go,
- przygotowanie aplikacji mobilnej na platformie salesforce korespondującej z modułem pythonowym

## Zastosowanie
Wiele osób doświadczyło sytuacji w której zastanawia się jakiej rasy jest napotkany pies. Dobrym przykładem będzie wizyta w schronisku podczas której chcemy rozpoznać rasę naszego nowego domownika. Aplikacja znajdzie także zastosowanie gdy znajdziemy bezpańskiego psa na ulicy, wystarczy zrobić mu zdjęcie i nasza aplikacja ropozna rasę aby skonstruować bardziej szczegółowe ogłoszenie znalezienia pieska. Aplikacja dodatkowo zapewnia podstawowe informacje o rozpoznanej rasie.

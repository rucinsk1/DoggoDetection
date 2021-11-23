# DoggoDetector
Aplikacja służąco do rozpoznawania ras psów. Po wgraniu zdjęcia aplikacja rozpozna rasę oraz poda o niej podstawowe informacje. Aplikacja wykorzystuje pythona, salesforce'a oraz serwisy zapewnione przez Azure (CustomVision oraz Storage).

## Developerzy
- [Kalata Krzysztof](https://github.com/KrzysztofKalata)
- [Ruciński Konrad](https://github.com/rucinsk1)

## [Link do prezentacji](https://www.youtube.com/watch?v=wW4fWsHx_8w)


## Architektura + stos technologiczny
![image](https://user-images.githubusercontent.com/46794180/142996305-9c3312bb-d6be-4160-ab1e-d838f2326c35.png)

- **Python** - język programowania odpowiedzialny za stworzenie aplikacji oraz obsługę pobranego modelu. Najważniejsze biblioteki to flask, tensorflow.
- **Salesforce** - platforma oferująca dostęp do aplikacji końcowej, to w niej wgrywamy zdjęcie które jest zapisywane i przekazywane do modułu Pythona.

## Opis funkcjonalności
- rozpoznawanie rasy psa,
- pozyskiwanie informacji na temat rozpoznanej rasy.

## Proces tworzenia
- pobranie oraz otagowanie zdjęć,
- wytrenowanie modelu,
- pobranie modelu oraz stworzenie aplikacji wykorzystującej go,
- przygotowanie aplikacji mobilnej na platformie salesforce korespondującej z modułem pythonowym

## Schemat działania
- użytkownik uruchamia aplikacje Doggo Detector w Salesforce
- użytkownik zamieszcza zdjęcie psa, którego rasę chce poznać
- zdjęcie przesyłane jest do aplikacji python'owej w której analizuje je model
- na podstawie przesłanej informacji o wykrytej rasie psa, aplikacja wyświetla informacje o danej rasie

## Zastosowanie
Wiele osób doświadczyło sytuacji w której zastanawia się jakiej rasy jest napotkany pies. Dobrym przykładem będzie wizyta w schronisku podczas której chcemy rozpoznać rasę naszego nowego domownika. Aplikacja znajdzie także zastosowanie gdy znajdziemy bezpańskiego psa na ulicy, wystarczy zrobić mu zdjęcie i nasza aplikacja ropozna rasę aby skonstruować bardziej szczegółowe ogłoszenie znalezienia pieska. Aplikacja dodatkowo zapewnia podstawowe informacje o rozpoznanej rasie.

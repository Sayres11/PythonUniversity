# Instructions
# Zadanie 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli w danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele. Dane wejściowe to długość i szerokość podłogi. (do powierzchni pomieszczenia należy dodać 10%) długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)
#
# Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi w szybszy sposób niż w przykładzie. Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi. (10%)
#
# Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
#   Funkcja przyjmuje: wiadomość
# – tekst do zaszyfrowania, klucz
# – liczbę o ile należy przesunąć litery w alfabecie oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
#
#  Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)
#  Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres listy  z alfabetem oraz problem podania klucza o dowolnej wielkości(20%).
#  Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).

def ilosc_opakowan_paneli(dlugosc_podlogi, szerokosc_podlogi,
                          dlugosc_panela, szerokosc_panela,
                          ilosc_paneli_opakowaniu):
    powierzchnia_pokoju = (dlugosc_podlogi * szerokosc_podlogi) * 1.1

    powierzchnia_pakietu = dlugosc_panela * szerokosc_panela

    ilosc_paneli_potrzebna = powierzchnia_pokoju / powierzchnia_pakietu

    ilosc_opakowan_potrzebna = ilosc_paneli_potrzebna / ilosc_paneli_opakowaniu
    ilosc_opakowan_potrzebna = int(ilosc_opakowan_potrzebna) + 1

    return ilosc_opakowan_potrzebna


def czy_liczba_pierwsza(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def ceasar_cipher(slowo, klucz):
    wynik = ""
    for char in slowo.lower():
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 + klucz) % 26 + 97)
            wynik += shifted_char
        else:
            wynik += char
    return wynik


encrypted_message = \
    ceasar_cipher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5)
print(encrypted_message)

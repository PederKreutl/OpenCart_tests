# BDD testy pre platformu OpenCart (Python/Gherkin/Selenium)

Cieľom projektu bolo vytvoriť **scénare BDD** spolu s implementáciou pre testovanie platformi **OpenCart**.
Ako konkrétnu podčasť aplikácie som si vybral **nákupny proces neregistrovaného užívateľa**.

## Súbory

- ***`"steps/steps.py"`*** — Implementácia scénarov
- ***`"environment.py"`*** — Nastavanie a upratanie prostredia pre testy
- ***`"README.md"`*** — Stručná dokumentácia projektu
- ***`"page_visit.feature"`*** — Scénare na testovanie návštevy stránky
- ***`"product_seach.feature"`*** — Scénare na testovanie postupného prístupu k produktu
- ***`"cart_manipulation.feature"`*** — Scénare na testovanie práce s nákupným košíkom
- ***`"checkout_process.feature"`*** — Scénare na testovanie vyplnenia formulára objednávky

## Návšteva stránky ***(`page_visit.feature`)***

Súbor obsahuje test na proces návštevy ľubovoľnej stránky na platforme OpenCart.

**Testované scénare:**\
**1.** Návšteva stránky *(Visit page)*

## Prístup k produktu ***(`product_search.feature`)***

Súbor obsahuje testy na proces postupného prístupu k produktu na platforme OpenCart.

**Testované scénare:**\
**1.** Zobrazenie navigačnej lišty kategórie produktu *(Show products category drop-down list)*\
**2.** Zobrazenie kategórie produktu *(Show products category)*\
**3.** Zobrazenie produktu *(Show product)*

## Práca s nákupným košíkom ***(`cart_manipulation.feature`)***

Súbor obsahuje testy na proces práce nad nákupným košíkom na platforme OpenCart.

**Testované scénare:**\
**1.** Pridanie produktu do košíka *(Add product to cart)*\
**2.** Zobrazenie navigačnej lišty košíka *(Show cart drop-down list)*\
**3.** Prístup do košíka *(Go to cart)*\
**4.** Zmena meny *(Change Currency)*\
**5.** Vymazanie produktu z košíka *(Remove product from cart)*\
**6.** Zmena množstva produktu v košíku *(Change product quantity in cart)*\
**7.** Použitie zľavového kupóna *(Use Coupon code)*

## Vyplnenie formulára objednávky ***(`checkout_process.feature`)***

Súbor obsahuje testy na proces výplne formulára objednávky na platforme OpenCart.

**Testované scénare:**\
**1.** Prístup k formuláru objednávky *(Start checkout)*\
**2.** Výber spôsobu objednávky *(Insert checkout data (Step 1, Checkout options))*\
**3.** Vyplnenie údajov na doručenie *(Insert checkout data (Step 2, Billing details))*\
**4.** Výber metódy dopravy *(Insert checkout data (Step 4, Delivery method))*\
**5.** Výber metódy platenia *(Insert checkout data (Step 5, Payment method))*\
**6.** Potvrdenie objednávky *(Insert checkout data (Step 6, Confirm order))*

## Ostatné

- Autor: Peter Krutý

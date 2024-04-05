# Kako da isprogramiram svog "AI" agenta?

* Prezentacija se nalazi na linku: [Kako da isprogramiram svog "AI" agenta?](./Kako%20da%20isprogramiram%20svog%20AI%20agenta.pdf)
* Propratni kod uz prezentaciju se nalazi u ovom repozitorijumu.

## Kako da pokrenes kod?

Prvo, potrebno je da imas instaliran program za obradu koda, poput popularnog [VS Code](https://code.visualstudio.com/). Takodje je potrebno da imas instaliran programski jezik [Python](https://www.python.org/).

1. Preuzmi ovaj repozitorijum
2. Otvori repozitorijum na svom racunaru u programu za obradu koda (pretpostavka VS Code)
3. Otvori terminal u okviru svog okruzenja. Terminal mora biti tipa `bash`, a ne `cmd`
4. U terminal ukucaj: `python -m venv .venv`
5. Potom: `. .venv/Scripts/activate`
6. Kopiraj fajl `.env.examples` i promeni ime u `.env`, te unesi svoj OpenAI API kljuc. Vise o tome mozes saznati [u ovom tutorijalu](https://platform.openai.com/docs/quickstart?context=python)
7. Konacno, mozes pokrenuti program sa: `python main.py`
8. Otvori link [`http://127.0.0.1:7860`](http://127.0.0.1:7860) u svom pretrazivacu i uzivaj u sopstvenom AI programu!

Mozes izmeniti podatke u `data/` bilo kojim tekstualnim sadrzajem i uciniti da tvoj AI agent poseduje znanje koje ti zelis.
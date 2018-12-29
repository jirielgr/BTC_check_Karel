zde je základní python script na kontrolu změny v doporučení (pro Python 2.7)

Po startu zašle aktuální pozici, pak čeká do 47 minuty a zkontroluje doporučení. 
Pokud se změnilo, tak pošle nový email (pošle až 3 poslední změny včetně času kdy kontrolu provedl, pokud je zná), jinak nic. 
Pak čeká další hodinu. Na začátku je sekce "User variables" kde je nutné nastavit základní parametry (hlavně SMTP).

Zda to správně funguje uvidím, až se změní doporučení na LONG 　

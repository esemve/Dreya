# Dreya

## Mi ez?

Dreya a hobbiprojektem. Ő egy "AI", egy asszisztens, aki segít a mindennapokban, okos otthonná varázsolja a lakásomat és segít hatékonyabban kihasználni a home serverem.

## Miért magyar ez a leírás?

Mert nem célom oktatóanyagot készíteni. PHP Programozó vagyok, így bár Dreya több különböző modult is tartalmaz, alapja főként a Python, amihez nálam biztosan sokan sokkal jobban értenek. A célom ezzel a repoval csak a rendszer bemutatása, ötletek adása, és annak a bizonyítása, hogy egy kis energia befektetéssel mennyire király dolgokat lehet alkotni, ami bár nem változtatja meg a világot, de kényelmesebbé teszi a saját életed.

## Milyen részekből áll Dreya?

Jelenleg Dreya "magja" egy Python -ban írt rész, ami a Dreya mappában található, valamint része még egy PHP -ban írt üzenetküldő gateway (a kód tisztítása után publisholom azt is). Erre azért van szükség, mert facebook chatbotként kommunikál velünk, amihez szükség volt egy 24/7 elérhető https connectionnel rendelkező felületre. Emiatt a szerver és Dreya a 18080 -as porton keresztül beszélgetnek egymással, és a PHP-s rész gatewayként működik. Tartozik hozzá egy általam épített Arduino -s mozgásérzékelő.

## Mire képes jelenleg Dreya? 

 * Letölti a kedvenc sorozataimat
 * Letölti a sorozataimhoz a magyar feliratokat
 * Ha a BKV -nek gondja van valamely engem érintő járattal, arról értesít.
 * A fentiekről értesít Viber -en
 * Viber chatbotként szabad szavas üzenetekből képes learning segítségével kitalálni, hogy mit szeretnék tőle
 * Soros porton rákötött Arduino kezelése
 * Értesítések a közeledő névnapokról, szülinapokról, ünnepnapokról
 * Mozgásérzékelő, Viberen keresztül riaszt webkamera képet mellékelve
 * Hazaérkezésünkkor automatikusan bekapcsolja a PC-t
 * Éjjel 1 és reggel 8 között automatikusan kikapcsol majd be
 * Van több nem publikált biztonsági megoldása amit nem rakok fel, de többek között mobiltelefonok wifire csatlakozása alapján megállapítja, hogy itthon van-e valaki, így a riasztót képes kikapcsolni.
 * Az IP kamera zavaró, hogy folyamatosan néz. Ha a rendszer úgy érzékeli, hogy hazaértünk, akkor az ip kamerát befordítja a fal felé. Ez egy picit robotos hatást is kölcsönöz Dreyanak.
 * Chatbotként válaszol a következő jellegű kérdésekre:
 * * Milyen idő lesz ma/holnap stb kérdésekre
 * * Mondj egy viccet
 * * Hány lakosa van New York -nak?
 * * Mennyi a load?
 * * Hány fok van otthon?
 * * Emlékeztess péntek délben/délután/este, hogy ez meg az.



## Mik a tervezett funkciók?

Dreyának már volt egy PHP-ban, pythonban, node -ban írt verziója Nostromo néven. A cél most az, hogy ezeket a scripteket egyesítsem egyetlen felületen. A régi funkciók mindenképpen bele kerülnek a rendszerbe:
 * Zenelejátszás
 * Arcfelismerés IP kamera/webkamera alapján
 * Android kliens, hangvezérléshez
 * "Mosógép lejárt" kezelése, ehhez persze még arduinozni is kell
 * Megannyi jóság... :)


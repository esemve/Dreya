# Dreya

## Mi ez?

Dreya a hobbiprojektem. Ő egy "AI", egy asszisztens, aki segít a mindennapokban, okos otthonná varázsolja a lakásomat és segít hatékonyabban kihasználni a home serverem.

## Miért magyar ez a leírás?

Mert nem célom oktatóanyagot készíteni. PHP Programozó vagyok, így bár Dreya több különböző modult is tartalmaz, alapja főként a Java, amihez nálam biztosan sokan sokkal jobban értenek. A célom ezzel a repoval csak a rendszer bemutatása, ötletek adása, és annak a bizonyítása, hogy egy kis energia befektetéssel mennyire király dolgokat lehet alkotni, ami bár nem változtatja meg a világot, de kényelmesebbé teszi a saját életed.

## Milyen részekből áll Dreya?

Jelenleg Dreya "magja" egy Java -ban írt rész, ami a Dreya mappában található, valamint része még egy PHP -ban írt üzenetküldő gateway (a kód tisztítása után publisholom azt is). Erre azért van szükség, mert facebook chatbotként kommunikál velünk, amihez szükség volt egy 24/7 elérhető https connectionnel rendelkező felületre. Emiatt a szerver és Dreya a 18080 -as porton keresztül beszélgetnek egymással, és a PHP-s rész gatewayként működik. Tartozik hozzá egy általam épített Arduino -s mozgásérzékelő.

## Mire képes jelenleg Dreya? 

 * Letölti a kedvenc sorozataimat
 * Letölti a sorozataimhoz a magyar feliratokat
 * Ha a BKV -nek gondja van valamely engem érintő járattal, arról értesít.
 * A fentiekről értesít Facebookon
 * Facebook chatbotként jelenleg csak a "hello" -ra képes válaszolni.

## Mik a tervezett funkciók?

Dreyának már volt egy PHP-ban, pythonban, node -ban írt verziója Nostromo néven. A cél most az, hogy ezeket a scripteket egyesítsem egyetlen felületen. A régi funkciók mindenképpen bele kerülnek a rendszerbe:
 * Facebookról szabad szavas kérések értelmezése
 * Soros porton rákötött Arduino kezelése
 * Értesítések a közeledő névnapokról, szülinapokról, ünnepnapokról
 * Időjárási riasztások küldése
 * Zenelejátszás
 * Riasztás webkamerakép mellékelésével
 * Mozgásérzékelő ismét működjön, alertet kapjak
 * Arcfelismerés IP kamera/webkamera alapján
 * Ki van otthon? kérdésre képes legyen válaszolni
 * Mennyi az idő kérdésre válasz
 * Android kliens, hangvezérléshez
 * "Mondj egy viccet", "Milyen idő lesz ma?" jellegű kérdések kezelése
 * "Emlékeztess péntek délben, hogy mennem kell boltba" típusú üzenetek kezelése
 * Hazaérkezésre a pc bekapcsolása
 * "Mosógép lejárt" kezelése, ehhez persze még arduinozni is kell
 * Megannyi jóság... :)
 

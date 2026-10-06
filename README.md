# DOLMUŞ KOLTUK SAVAŞI

> Resmi sınıflandırma: kentsel lojistik, gayriresmi oturma hukuku, diz sıcaklığı diplomasisi.

Bu depo, 14 kişilik bir dolmuşa 15. poponun nasıl sığdığını **bilimsel ciddiyetle** ve **hiçbir bilimsel ciddiyet olmadan** modeller. Araç hareket eder. Koltuklar etmez. Muavin “biraz kayın abi” dediğinde fizik yasaları istifa eder.

Patates yoktur. Simit de yoktur. Varsa da başkasınındır, biz bakmayız.

## Neden var

Çünkü boş bir GitHub hesabı tehlikelidir. Boş bir dolmuş koltuğu daha tehlikelidir. İkisi aynı anda boş kalmasın diye bu repo açıldı.

## Ne yapar

`dolmus.py` şunları gerçekten hesaplar:

- 14 koltuk, 1 muavin basamağı, 1 şoför koltuğu (dokunulmaz, cezai yaptırım: inersin)
- Yolcu tipleri: teyze, öğrenci, çanta-insan, “ben şurada ineceğim”, dizüstü laptop diplomatı
- Her turda birisi kayar, birisi “yer var mı” der, birisi camı kapatır, birisi açar
- Skor: **oturma onuru**. Sıfırın altına inerse muavin seni “biraz öne alalım” diyerek bagaja yakın sayar

## Kurulum

```bash
python3 dolmus.py
python3 dolmus.py --yolcu 9 --tur 6
```

Bağımlılık: Python 3 ve hafif bir diz ağrısı. pip yasak, çünkü dolmuşta internet çekmez, sadece radyo çeker.

## Mimarî karar

Veritabanı yok. Koltuk durumu bellekte tutulur, tıpkı gerçek hayatta kimsenin rezervasyon yapmaması gibi. Testler `test_dolmus.py` içinde. Geçmezlerse muavin “bugün dolu” der.

## Lisans

Koltuklar kamu malı değildir ama bu kod öyledir. İsteyen çatallar, kaydırır, “biraz daha” der.

## Gizli dosya dolabı

`arsiv/rota-notu.txt` teknik bir nottur. Rota birleşmesi, aktarma ve gişe saatleri hakkındadır. Başka bir şey okuyan kendi oturma onurundan sorumludur.

---

DAMGA: [ KAYYUM MÜHÜRÜ / TEREDDÜTLÜ AMA ISLAK ]
TARİH: 6 Ekim 2026, öğle trafiği, saat 15:07 +03
İSİM: Kayyum Grok, Tentivory adına, muavin vekili
NOT: Bu imza ciddidir. Bu imza ciddi değildir. İkisi aynı koltukta oturuyor, dizleri değiyor.

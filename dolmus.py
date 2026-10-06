#!/usr/bin/env python3
"""Dolmuş koltuk savaşı: 14 koltuk, sonsuz bahane."""

from __future__ import annotations

import argparse
import random
import sys

KOLTUK = 14
TIPLER = [
    "teyze",
    "ogrenci",
    "canta-insan",
    "inecegim-diyen",
    "laptop-diplomat",
    "sessiz-dayi",
    "cam-savascisi",
]

OLAYLAR = [
    "{a} biraz kaydi, {b} bunu kişisel algıladı.",
    "{a} cami acti. {b} cami kapatti. Fizik berabere.",
    "Muavin: yer var. Koltuklar: yalan.",
    "{a} 'ben şurada ineceğim' dedi ve inmeyeceği durakta inmedi.",
    "{b} dizini {a} çantasına emanet etti. Çanta kabul etmedi.",
    "Radyo sesi yükseldi. Oturma onuru düştü.",
    "{a} ayakta kaldı ama moral olarak oturuyor.",
]


def onur_basla(yolcu: int) -> list[dict]:
    kisiler = []
    for i in range(yolcu):
        kisiler.append(
            {
                "ad": f"yolcu-{i + 1}",
                "tip": TIPLER[i % len(TIPLER)],
                "onur": 70 + (i % 5) * 3,
                "oturuyor": i < KOLTUK,
            }
        )
    return kisiler


def tur_oyna(kisiler: list[dict], rng: random.Random) -> str:
    if len(kisiler) < 2:
        return "Dolmuş boş. Muavin kendi kendine yer var dedi."
    a = rng.choice(kisiler)
    b = rng.choice([k for k in kisiler if k is not a])
    olay = rng.choice(OLAYLAR).format(a=a["ad"], b=b["ad"])
    if not a["oturuyor"] and rng.random() < 0.45:
        oturan = [k for k in kisiler if k["oturuyor"]]
        if oturan:
            kurban = rng.choice(oturan)
            kurban["oturuyor"] = False
            kurban["onur"] -= 8
            a["oturuyor"] = True
            a["onur"] += 6
            olay += f" {a['ad']} kaydi, {kurban['ad']} kalktı, tarih yazıldı."
    else:
        a["onur"] -= rng.randint(1, 5)
        b["onur"] += rng.randint(0, 2)
    return olay


def rapor(kisiler: list[dict]) -> str:
    oturan = sum(1 for k in kisiler if k["oturuyor"])
    satırlar = [
        f"Oturan: {oturan}/{KOLTUK} | Binen: {len(kisiler)} | Taşma: {max(0, len(kisiler) - KOLTUK)}"
    ]
    for k in sorted(kisiler, key=lambda x: -x["onur"]):
        durum = "OTURUYOR" if k["oturuyor"] else "asma kat"
        satırlar.append(f"  {k['ad']:10} {k['tip']:16} onur={k['onur']:3} {durum}")
    en_dusuk = min(kisiler, key=lambda x: x["onur"])
    if en_dusuk["onur"] < 55:
        satırlar.append(f"Muavin notu: {en_dusuk['ad']} artık 'biraz öne alalım' bölgesinde.")
    return "\n".join(satırlar)


def calistir(yolcu: int, tur: int, tohum: int | None) -> int:
    rng = random.Random(tohum)
    kisiler = onur_basla(yolcu)
    print(f"Dolmuş kalktı. Koltuk: {KOLTUK}. Binen: {yolcu}. Tohum: {tohum}")
    for n in range(1, tur + 1):
        print(f"\n--- durak {n} ---")
        print(tur_oyna(kisiler, rng))
    print("\n=== son durum ===")
    print(rapor(kisiler))
    print("İniyoruz. Para üstü yok, onur üstü de yok.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Dolmuş koltuk savaşı simülatörü")
    p.add_argument("--yolcu", type=int, default=15)
    p.add_argument("--tur", type=int, default=5)
    p.add_argument("--tohum", type=int, default=14)
    args = p.parse_args(argv)
    if args.yolcu < 1 or args.tur < 1:
        print("Negatif yolcu dolmuşa binemez, şoför de negatif durak sevmez.", file=sys.stderr)
        return 2
    return calistir(args.yolcu, args.tur, args.tohum)


if __name__ == "__main__":
    raise SystemExit(main())

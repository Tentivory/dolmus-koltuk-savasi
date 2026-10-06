import dolmus


def test_on_dort_koltuk_asla_on_bes_olmaz():
    kisiler = dolmus.onur_basla(15)
    assert sum(1 for k in kisiler if k["oturuyor"]) == 14


def test_tur_metin_dondurur():
    kisiler = dolmus.onur_basla(8)
    metin = dolmus.tur_oyna(kisiler, dolmus.random.Random(1))
    assert isinstance(metin, str) and len(metin) > 5


def test_bos_dolmus_bile_konusur():
    assert "yer var" in dolmus.tur_oyna(dolmus.onur_basla(1), dolmus.random.Random(0))

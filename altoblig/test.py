from sauImg import SauSprite

def test_sau():
    sau1 = SauSprite("Sau", 50, 50)
    sau1.sett_posisjon(0, 0)
    sau1.sett_fart(10, 20)
    assert sau1.hent_pvenstre() == 0
    assert sau1.hent_ptopp() == 0
    assert sau1.hent_fart_fra_venstre() == 10
    assert sau1.hent_fart_fra_topp() == 20
    sau1.beveg()
    assert sau1.hent_pvenstre() == 10
    assert sau1.hent_ptopp() == 20
    sau1.beveg()
    assert sau1.hent_pvenstre() == 20
    assert sau1.hent_ptopp() == 40
    sau1.snu()
    assert sau1.hent_fart_fra_venstre() == -10
    assert sau1.hent_fart_fra_topp() == -20
    sau1.beveg()
    print(sau1.hent_pvenstre())
    print(sau1.hent_ptopp())

test_sau()

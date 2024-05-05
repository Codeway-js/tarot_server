from tarot_class import *

conv = convertstrcarte

def test_convertstrcarte():
    assert conv("Aat")==Carte(0,"at")
test_convertstrcarte()

def test_tolist():
    assert Tas([conv("Aat"),conv("Cco")]).toList() == ["Aat","Cco"]
test_tolist()

def test_addCartestr():
    assert Tas([conv("Aat")]).addCartestr("Bat") == Tas([conv("Aat"),conv("Bat")])
test_addCartestr()

def test_removeCartestr():
    assert Tas([conv("Aat"),conv("Bat")]).removeCartestr("Bat") == Tas([conv("Aat")])
test_removeCartestr()


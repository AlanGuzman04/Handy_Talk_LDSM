from src.database import save_translation, get_last_translation

def test_save_translation():
    save_translation("a")
    last = get_last_translation()
    assert last == "a"

def test_get_all_wares(products_repo):
    db = products_repo
    all.wares = db.get_all()
    for wares in all_wares:
        print(wares)
def test_get_all_wares(products_repo):
    db = products_repo
    all_wares = db.get_all()
    for ware in all_wares:
        print(ware)
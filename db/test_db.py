def test_get_all_products(products_repo):
    db = products_repo
    all.prod = db.get_all()
    for prod in all_prod:
        print(prod)
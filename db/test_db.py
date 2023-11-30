def test_get_all_prod(products_repo):
    db = products_repo
    all_prod = db.get_all()
    for prod in all_prod:
        print(prod)

def test_add_product(products_repo):
    data = (2, 'GUCCI', 'GLASSES', 3000, 2, 'WOMAN_GLASSES')
    db = products_repo
    db.insert_one(*data)
    all_prod = db.get_all()  # Виправлено непорозуміння
    for prod in all_prod:
        print(prod)



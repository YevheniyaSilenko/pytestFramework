def test_get_all_prod(products_repo):
    db = products_repo
    all_prod = db.get_all()
    for prod in all_prod:
        print(prod)


def test_add_product(products_repo):
    data = (15, 'GUCCI', 'GLASSES', 3000, 2, 'WOMAN_GLASSES')
    db = products_repo
    db.insert_one(*data)
    all_prod = db.get_all()
    for prod in all_prod:
        print(prod)


def test_get_one_by_id(products_repo):
    db = products_repo
    product = db.get_one_by_id(1)
    print(product)


def test_update_product(products_repo):
    db = products_repo
    db.update_one(1, 'UpdatedProduct', 'UpdatedCategory', 20, 100, 'UpdatedDescription')
    updated_product = db.get_one_by_id(1)
    print(updated_product)


def test_delete_product(products_repo):
    db = products_repo
    db.delete_one(1)
    deleted_product = db.get_one_by_id(1)
    print(deleted_product)


def test_get_one_by_id_negative(products_repo):
    db = products_repo
    non_existing_product = db.get_one_by_id(-1)
    print(non_existing_product)


def test_delete_product_negative(products_repo):
    db = products_repo
    try:
        db.delete_one(-1)
    except Exception as e: #
        print(e)

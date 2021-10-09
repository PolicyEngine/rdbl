def test_rounding():
    from rdbl import gbp

    assert gbp(231e9) == "£231bn"

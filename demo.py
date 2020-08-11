import pytest


class Test1:

    @pytest.mark.example
    def test_transactions(self):
        print("it is marked test")
        assert True

    def test_a(self):
        a= 23
        c=89
        assert a==c

    def test_b(self):
        a= 50
        c=50
        assert a==c

    @pytest.mark.depends(on=['test_b'])
    @pytest.mark.depends(on=['test_a'])
    def test_c(self):
        pass





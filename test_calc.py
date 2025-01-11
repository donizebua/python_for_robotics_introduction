import unittest
import calc

class TestCalc(unittest.TestCase):
    #TestCalc is just random name
    #unittest.TestCase memungkinkan kira untuk menggunakan berbagai macam fungsi test dari turunan modul unittest

    def test_add(self):
    #penamaan test_ diawal nama diwajibkan untuk memberitahu program fungsi apa saja yang akan di test
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-3,4),1)
        self.assertEqual(calc.add(-3,-4),-7)

    def test_subtract(self):
    #penamaan test_ diawal nama diwajibkan untuk memberitahu program fungsi apa saja yang akan di test
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-3,4),-7)
        self.assertEqual(calc.subtract(-3,-4),1)
        
    def test_multiply(self):
    #penamaan test_ diawal nama diwajibkan untuk memberitahu program fungsi apa saja yang akan di test
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-3,4),-12)
        self.assertEqual(calc.multiply(-3,-4),12)

    def test_divide(self):
    #penamaan test_ diawal nama diwajibkan untuk memberitahu program fungsi apa saja yang akan di test
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-5,2),-2.5)
        self.assertEqual(calc.divide(-4,-2),2)

if __name__ == "__main__" :
    unittest.main()
    """
    Kode diatas memungkinkan kita untuk menjalankan t est operasi secara langsung, karena jika tidak ditulis maka tidak bisa di run langsung pada run code simbol segitiga di atas, harus pada terminal menggunakan script:
    "phyton -m unnittest nama_file.py"
    Kode ini juga memungkinkan kita untuk tidak menjalankan programnya jika diimpor sebagai modul, bukan dijalankan secara langsung.
    """
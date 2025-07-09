import unittest
from pypix import Pix


class TestPix(unittest.TestCase):
    def test_pix_creation(self):
        """Test basic Pix creation"""
        pix = Pix()
        pix.set_pixkey('1234567890')
        pix.set_description('Mensagem ao pagador')
        pix.set_amount(10.00)
        pix.set_merchant_name('Daniel Yohan')
        pix.set_merchant_city('MACEIO')
        pix.set_txid('Lanche')
        
        # Verificar se o código Pix foi gerado corretamente
        pix_code = str(pix)
        self.assertTrue(pix_code.startswith('00020126'))
        self.assertIn('BR.GOV.BCB.PIX', pix_code)
        self.assertIn('Lanche', pix_code)

    def test_sanitize_text(self):
        """Test text sanitization"""
        pix = Pix()
        # Teste com acentos
        self.assertEqual(pix.sanitize_text('São Paulo'), 'Sao Paulo')
        # Teste com caracteres especiais
        self.assertEqual(pix.sanitize_text('João da Silva!@#'), 'Joao da Silva')
        # Teste com números
        self.assertEqual(pix.sanitize_text('Pagamento 123'), 'Pagamento 123')

    def test_amount_formatting(self):
        """Test amount formatting"""
        pix = Pix()
        pix.set_amount(10)
        self.assertEqual(pix.amount, '10.00')
        pix.set_amount(10.5)
        self.assertEqual(pix.amount, '10.50')
        pix.set_amount(10.55)
        self.assertEqual(pix.amount, '10.55')
        pix.set_amount(10.555)  # Deve arredondar para 2 casas decimais
        self.assertEqual(pix.amount, '10.56')

    def test_field_validation(self):
        """Test field validation"""
        pix = Pix()
        # Teste sem chave Pix
        with self.assertRaises(ValueError):
            str(pix)
        
        pix.set_pixkey('10000222222')
        # Teste sem nome do comerciante
        with self.assertRaises(ValueError):
            str(pix)
        
        pix.set_merchant_name('DANIEL YOHAN')
        # Teste sem cidade
        with self.assertRaises(ValueError):
            str(pix)
        
        # Agora deve funcionar
        pix.set_merchant_city('MACEIO')
        try:
            str(pix)
        except ValueError:
            self.fail("set_merchant_city() raised ValueError unexpectedly!")

    def test_field_length_limits(self):
        """Test field length limits"""
        pix = Pix()
        
        # Teste com chave Pix muito longa (mais de 77 caracteres)
        long_key = 'a' * 100
        pix.set_pixkey(long_key)
        self.assertEqual(len(pix.pixkey), 77)
        
        # Teste com descrição muito longa (mais de 72 caracteres)
        long_desc = 'b' * 100
        pix.set_description(long_desc)
        self.assertEqual(len(pix.description), 72)
        
        # Teste com nome do comerciante muito longo (mais de 25 caracteres)
        long_name = 'c' * 100
        pix.set_merchant_name(long_name)
        self.assertEqual(len(pix.merchant_name), 25)
        
        # Teste com cidade muito longa (mais de 15 caracteres)
        long_city = 'd' * 100
        pix.set_merchant_city(long_city)
        self.assertEqual(len(pix.merchant_city), 15)
        
        # Teste com txid muito longo (mais de 25 caracteres)
        long_txid = 'e' * 100
        pix.set_txid(long_txid)
        self.assertEqual(len(pix.txid), 25)


if __name__ == '__main__':
    unittest.main()

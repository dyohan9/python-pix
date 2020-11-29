from pypix import Pix

pix = Pix()
pix.set_pixkey('12345678910')
pix.set_description('Pagamento')
pix.set_amount(500.00)
pix.set_merchant_name('Daniel Yohan')
pix.set_merchant_city('MACEIO')
pix.set_txid('Aquele Lanche')
print(pix)

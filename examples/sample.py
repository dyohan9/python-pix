from pypix import Pix

# Exemplo similar ao do Bradesco
pix = Pix()
pix.set_pixkey('08888888888')
pix.set_description('Mensagem ao pagador')
pix.set_amount(10.00)
pix.set_merchant_name('Nome')
pix.set_merchant_city('Cidade')
pix.set_txid('Identificador')
print("QR Code Pix:")
print(pix)
print("\n")

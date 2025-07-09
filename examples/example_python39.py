#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso da biblioteca pypix com Python 3.9+
Demonstra as funcionalidades principais da biblioteca com recursos modernos do Python
"""
from pypix import Pix
from dataclasses import dataclass
from typing import Optional


@dataclass
class PixPayment:
    """Classe de exemplo usando dataclass do Python 3.7+"""
    key: str
    description: Optional[str] = None
    amount: Optional[float] = None
    merchant_name: str = ""
    merchant_city: str = ""
    txid: Optional[str] = None


def create_pix_from_dataclass(payment: PixPayment) -> Pix:
    """Cria um objeto Pix a partir de um dataclass"""
    pix = Pix()
    pix.set_pixkey(payment.key)
    
    if payment.description:
        pix.set_description(payment.description)
    
    if payment.amount is not None:
        pix.set_amount(payment.amount)
    
    pix.set_merchant_name(payment.merchant_name)
    pix.set_merchant_city(payment.merchant_city)
    
    if payment.txid:
        pix.set_txid(payment.txid)
    
    return pix


def main():
    """Função principal"""
    # Exemplo usando dataclass (recurso do Python 3.7+)
    payment = PixPayment(
        key="10000000000",
        description="Pagamento via Python 3.9+",
        amount=150.75,
        merchant_name="EMPRESA MODERNA LTDA",
        merchant_city="SAO PAULO",
        txid="Cafe"
    )
    
    pix = create_pix_from_dataclass(payment)
    print("QR Code Pix (usando dataclass):")
    print(pix)
    print("\n")
    
    # Exemplo com type hints (melhorado no Python 3.9+)
    print("Exemplo com caracteres especiais (serão sanitizados):")
    pix2 = Pix()
    pix2.set_pixkey("12345678910")
    pix2.set_description("Café & Açaí")  # Caracteres especiais serão sanitizados
    pix2.set_amount(25.99)
    pix2.set_merchant_name("João da Silva")
    pix2.set_merchant_city("FLORIANÓPOLIS")
    pix2.set_txid("cafe2023")
    print(pix2)
    
    # Demonstração de arredondamento correto
    print("\nDemonstração de arredondamento:")
    pix3 = Pix()
    pix3.set_pixkey("11122233344")
    pix3.set_merchant_name("TESTE ARREDONDAMENTO")
    pix3.set_merchant_city("BRASILIA")
    
    # Valores com diferentes casas decimais
    values = [10.555, 99.995, 0.001, 0.009]
    for value in values:
        pix3.set_amount(value)
        print(f"Original: {value} -> Formatado: {pix3.amount}")


if __name__ == "__main__":
    main()

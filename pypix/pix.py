class Pix(object):
    def __init__(self):
        """
        Define objects of type Pix.
        https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf
        """
        self._ID_PAYLOAD_FORMAT_INDICATOR = "00"
        self._ID_MERCHANT_ACCOUNT_INFORMATION = "26"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_GUI = "00"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_KEY = "01"
        self._ID_MERCHANT_ACCOUNT_INFORMATION_DESCRIPTION = "02"
        self._ID_MERCHANT_CATEGORY_CODE = "52"
        self._ID_TRANSACTION_CURRENCY = "53"
        self._ID_TRANSACTION_AMOUNT = "54"
        self._ID_COUNTRY_CODE = "58"
        self._ID_MERCHANT_NAME = "59"
        self._ID_MERCHANT_CITY = "60"
        self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE = "62"
        self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE_TXID = "05"
        self._ID_CRC16 = "63"

        self.pixkey = None
        self.description = None
        self.merchant_name = None
        self.merchant_city = None
        self.country_code = "BR"
        self.txid = None
        self.amount = None

    def __str__(self):
        payload = "{}{}{}{}{}{}{}{}{}".format(
            self.get_value(self._ID_PAYLOAD_FORMAT_INDICATOR, "01"),
            self.get_merchant_account_information(),
            self.get_value(self._ID_MERCHANT_CATEGORY_CODE, "0000"),
            self.get_value(self._ID_TRANSACTION_CURRENCY, "986"),
            self.get_value(self._ID_TRANSACTION_AMOUNT, self.amount),
            self.get_value(self._ID_COUNTRY_CODE, self.country_code),
            self.get_value(self._ID_MERCHANT_NAME, self.merchant_name),
            self.get_value(self._ID_MERCHANT_CITY, self.merchant_city),
            self.get_additional_data_field_template(),
        )

        return "{}{}".format(payload, self.get_crc16(payload))

    def set_pixkey(self, pixkey: str):
        self.pixkey = pixkey

    def set_description(self, description: str):
        self.description = description

    def set_merchant_name(self, merchant_name: str):
        self.merchant_name = merchant_name

    def set_merchant_city(self, merchant_city: str):
        self.merchant_city = merchant_city

    def set_country_code(self, country: str):
        self.country_code = country

    def set_txid(self, txid: str):
        """Defines the transaction identifier."""
        self.txid = txid

    def set_amount(self, amount: float):
        """Defines the transaction amount"""
        self.amount = str(amount)

    def get_value(self, identify: str, value: str):
        """Concatenates the identifier and the value"""
        return "{}{}{}".format(identify, str(len(value)).zfill(2), value)

    def get_merchant_account_information(self):
        gui = self.get_value(
            self._ID_MERCHANT_ACCOUNT_INFORMATION_GUI, "br.gov.bcb.pix"
        )
        key = self.get_value(self._ID_MERCHANT_ACCOUNT_INFORMATION_KEY, self.pixkey)
        description = (
            self.get_value(
                self._ID_MERCHANT_ACCOUNT_INFORMATION_DESCRIPTION, self.description
            )
            if self.description
            else ""
        )

        return self.get_value(
            self._ID_MERCHANT_ACCOUNT_INFORMATION,
            "{}{}{}".format(gui, key, description),
        )

    def get_additional_data_field_template(self):
        txid = self.get_value(self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE_TXID, self.txid)
        return self.get_value(self._ID_ADDITIONAL_DATA_FIELD_TEMPLATE, txid)

    def toHex(self, dec: float):
        digits = "0123456789ABCDEF"
        x = dec % 16
        rest = dec // 16
        if rest == 0:
            return digits[x]
        return self.toHex(rest) + digits[x]

    def get_crc16(self, payload: str):
        payload = "{}{}04".format(payload, self._ID_CRC16)
        crc = 0xFFFF
        for i in range(len(payload)):
            crc ^= ord(payload[i]) << 8
            for j in range(8):
                if (crc & 0x8000) > 0:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc = crc << 1
        return "{}{}{}".format(self._ID_CRC16, "04", self.toHex(crc & 0xFFFF).upper())

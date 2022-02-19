from validate_docbr import CPF, CNPJ


class ValidaCPFouCNPJ:
    def __init__(self, cpf_cnpj):
        self.documento = str(cpf_cnpj)
        if self.valida_doc(self.documento):
            self.cpf_cnpj = self.documento
        else:
            raise ValueError(f'Documento inválido')

    def valida_doc(self, documento) -> bool:
        self.documento = documento
        if len(self.documento) == 11:
            return self.valida_cpf()
        elif len(self.documento) == 14:
            return self.valida_cnpj()
        else:
            raise ValueError(f'Quantidade de dígitos inválida!')

    def valida_cpf(self) -> bool:
        validador = CPF()
        return validador.validate(self.documento)

    def valida_cnpj(self) -> bool:
        validador = CNPJ()
        return validador.validate(self.documento)

    def __str__(self):
        documento = CPF() if len(self.documento) == 11 else CNPJ()
        return documento.mask(self.documento) + ' é válido!'

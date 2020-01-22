import json

class NumberDecoder:
    def __init__(self, numero):
        self.mensagem = ''
        self.negativo = False
        self.numero = int(numero)
        self.milhar = numero // 1000
        self.resto = numero % 1000

    def proccess(self):
        self.detecta_fora_intervalo()
        if self.fora_intervalo: 
            return
        self.detecta_negativo()
        self.tradutor_milhar()
        self.tradutor_centena()
        self.tradutor_dezena()
        self.tradutor_unidade()
        

    def detecta_fora_intervalo(self):
        if self.numero > 99999 or self.numero < -99999:
            self.fora_intervalo = True

    def detecta_negativo(self, numero):
        if numero < 0:
            self.negativo = True
            self.milhar *= -1 
            self.resto *= -1 

    def tradutor_milhar(self):
        self.tradutor_dezena()
        self.tradutor_unidade()

    def tradutor_centena(self, sem_resto=False):
        if sem_resto and self.numero < 200:
            self.mensagem += 'cento e '
        dicionario = ['cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
        

    def tradutor_dezena(self):
        if self.number < 20:
            dezenas = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove' ]
        else:
            dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem']

        

    def tradutor_unidade(self):
        unidade = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        

    def json_output(self):
        if self.fora_intervalo:
            return json.dumps({'mensagem': 'Fora do intervalo'})

        return json.dumps({'mensagem': self.mensagem})
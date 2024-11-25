from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    """docstrings"""
    """ Respresenta um restaurante """

    #MÉTODOS ESPECIAIS
    #método da clase obrigatórios
    def __init__(self, nome, categoria):
        #atributos privados
        self._nome = nome.title() #função - primeira letra maiúscula
        self._categoria = categoria.upper() #função - todas as letras maiúsculas  
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        """ 
        Inicializa uma instância de Restaurante

        Parâmetros:
        - nome (str): O nome do restaurante
        - categoria (str): A categoria do restaurante
        
        """


    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    """ Retorna uma representação em string do restaurante """
    
    #MÉTODOS PRÓPRIOS 
    @classmethod
    def listar_restaurantes(cls):
        """ Exibe uma lista formatada de todos os restaurantes """
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avalição'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    #modificar como um atributo é lido
    @property 
    def ativo(self):
        """ Retorna um simbolo indicando o estado de atividade do restaurante """
        return '✔️' if self._ativo else '❌'

    def alternar_estado(self):
        """ Altera o estado de atividade do restaurante """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """ 
        Registra uma avaliação para o restaurante

        Parâmetros:
        -cliente(str): o nome do cliente que fez a avaliacao
        -nota(float): a nota atribuida ao restaurante (entre 1 e 5) 
        """
        if 0 < nota <=5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações dp restaurante"""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media


#DIR - uma função,que mostra todos os atributos, métodos desse self - print(dir(restaurante_tuti))
#VARS - uma função, que exibi os atributos, métodos desse self em forma de lista - print(dir(restaurante_tuti)) 




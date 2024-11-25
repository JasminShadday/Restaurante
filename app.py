#importando classe Restaurante da pasta modelo do arquivo restaurantes 
from modelos.restaurante import Restaurante

#restaurante_mexicano = Restaurante('Mexicaninhos','Mexicana')
#restaurante_grego = Restaurante('Fala Grega','Grega')
#restaurante_juju = Restaurante('JuJu','Pizzaria')
restaurante_tuti = Restaurante('TuTi','Vegano')
restaurante_tuti.receber_avaliacao('Jasmin', 10)
restaurante_tuti.receber_avaliacao('Paulo', 9)
restaurante_tuti.receber_avaliacao('Julia', 5)



#aletrando o estado daquele restaurante
#restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()
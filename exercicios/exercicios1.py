#Mão na massa - Crie uma classe se chamada música
class musica:
    #atributos da classe
    nome = ''
    artista = ''
    duracao = float

musica1 = musica()
musica1.nome = 'Trilha do Amor'
musica1.artista = 'Arlindo Cruz'
musica1.duracao = 3.50

musica2 = musica()
musica2.nome = 'AluSina'
musica2.artista = 'Melly'
musica2.duracao = 3.30

musica3 = musica()
musica3.nome = 'Na Positiva'
musica3.artista = 'Natirutz'
musica3.duracao = 4.10

musicas = [musica1,musica2,musica3]

print (vars(musica1))
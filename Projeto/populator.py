#---------------------------------------------------------------
#--   Para correr:    python3 populator.py > populate.txt
#---------------------------------------------------------------

from random import randint

cidades = ["Portimão", "Vila Real", "Bragança", "Viana do Castelo", "Alcobaça", "Sintra", 
        "Funchal", "Portalegre", "Aveiro", "Almada", "Barreiro", "Cartaxo", "Elvas", 
        "Chaves", "Fátima", "Espinho", "Guarda", "Gouveia", "Fundão", "Leiria", 
        "Maia", "Loures", "Moura", "Mirandela", "Penafiel", "Pinhel", "Praia da Vitória", 
        "Queluz", "Ribeira Grande", "Santana", "Santa Cruz", "Seia", "São Pedro do Sul", "Tomar", 
        "Tavira", "Trancoso", "Trofa", "Lisboa", "Porto", "Braga", "Coimbra", 
        "Amadora", "Vila Nova de Gaia", "Setúbal", "Beja", "Évora", "Faro", "Sines", 
        "Monchique", "Viseu", "Montijo", "Alcochete", "Oliveira do Hospital", "Albufeira", "Olhão", 
        "Redondo", "Vila das Aves", "Abrantes", "Águeda", "Alcácer do Sal", "Alcobaça", "Alfena", 
        "Chaves", "Costa da Caparica", "Cartaxo", "Esmoriz", "Estarreja",
        "Fafe", "Santo André", "Felgueiras", "Fátima", "Funchal", "Gondomar", "Nazaré", 
        "Horta", "Lagoa", "Lagos", "Sagres", "Loulé", "Castro Daire", "Marco de Canavezes", 
        "Montemor-o-Novo", "Ovar", "Peniche", "Ericeira", "Pombal", "Cascais", 
        "Rio Maior", "Sabugal", "Santana", "Santo Tirso", "Seixal", "Silves", "Tondela", 
        "Valongo", "Vizela", "Ílhavo", "Lamego", "Lixa", "Lourosa", "Macedo de Cavaleiros",
        "Machico"]

nomes = ["João", "Joana", "Maria", "Rita", "Miguel", 
        "Simão", "Catarina", "Ana", "Luís", "Tomás", 
        "Pedro", "Margarida", "Madalena", "Carolina", "Ricardo", 
        "Éder", "Cristiano Ronaldo", "Bruno Fernandes", "Sancidino", "Jonas", 
        "Marega", "Camões"]

tiposEntidades = ["Bombeiros de ", "Polícia de ", "Junta de Freguesia de "]

nomesMeios = ["Ambulância", "Camião", "Carrinha", "Helicóptero"]

camaras = []
videos = []
segmentos = []
locais = []
vigia = []
eventos = []
processos = []
entidades = []
meios = []
meiosCombate = []
meiosApoio = []
meiosSocorro = []



#-----------------------------------------
#--   Camaras, Video e SegmentoVideo
#-----------------------------------------
used = []

for i in range (0, 102):
    camaras.append('insert into camara values(' + str(i) + ');')

    j = 0
    while j < 4:
        dataHoraInicio = randint(1451606400, 1546300799) # 2016 <= dataHoraInicio <= 2018
        duracao = randint(10, 30)
        dataHoraFim = dataHoraInicio + duracao*60
        numCamara = randint(1, 100)

        if (dataHoraInicio not in used):
            used.append(dataHoraInicio)
            videos.append('insert into video values(' + str(dataHoraInicio) + ', ' + str(dataHoraFim) + ', ' + str(numCamara) + ');')
            numSegmentos = randint(1, 2)

            for k in range (0, numSegmentos):
                numSegmento = k

                if (k != numSegmentos - 1):
                    duracaoSegmento = 2
                    duracao -= 2

                else:
                    duracaoSegmento = duracao

                segmentos.append('insert into segmentoVideo values(' + str(numSegmento) + ', ' + str(duracaoSegmento) + ', ' + str(dataHoraInicio) + ', ' + str(numCamara) + ');')
                dataHoraInicio += duracaoSegmento*60

            j += 1



#-----------------------------------------
#--   Local, Vigia
#-----------------------------------------

for cidade in cidades:
    locais.append('insert into local values(\'' + cidade + '\');')

for i in range(0, 102):
    vigia.append('insert into vigia values(\'' + cidades[randint(0, len(cidades) - 1)] + '\', ' + str(i) + ');')



#-----------------------------------------
#--   EventoEmergencia
#-----------------------------------------

numTelefone = 960000000
instanteChamada = 1451606400
numProcessoSocorro = 0

for i in range(0, 150):
    nome = nomes[randint(0, len(nomes) - 1)]
    morada = cidades[randint(0, len(cidades) - 1)]

    eventos.append('insert into eventoEmergencia values(' + str(numTelefone) + ', ' + str(instanteChamada) + ', \'' + nome + '\', \'' + morada + '\', ' + str(numProcessoSocorro) + ');')

    numTelefone += 1
    instanteChamada += randint(0,1000000)
    numProcessoSocorro += 1
    numProcessoSocorro = numProcessoSocorro % 102   #Numero de processos socorro



#-----------------------------------------
#--   ProcessoSocorro
#-----------------------------------------

for i in range(0, 102):
    processos.append('insert into processoSocorro values(' + str(i) + ');')



#-----------------------------------------
#--   Entidade Meio
#-----------------------------------------

todasEntidades = []
i = 0

while i < 102:
    entidade = tiposEntidades[randint(0, len(tiposEntidades) - 1)] + cidades[randint(0, len(cidades) - 1)]

    if entidade not in todasEntidades:
        todasEntidades.append(entidade)

        entidades.append('insert into entidadeMeio values(\'' + entidade + '\');')

        i += 1



#-----------------------------------------
#--   Meio (Combate, Apoio, Socorro)
#-----------------------------------------

for nomeEntidade in todasEntidades:
    for i in range (0, randint(3,5)):
        meios.append('insert into meio values(' + str(i) + ', \'' + nomesMeios[randint(0, len(nomesMeios) - 1)] + '\', \'' + nomeEntidade + '\');')



#-----------------------------------------
#--   Prints
#-----------------------------------------

def printAll():
    for x in camaras:
        print(x)

    print('\n\n')

    for x in videos:
        print(x)

    print('\n\n')

    for x in segmentos:
        print(x)

    print('\n\n')

    for x in locais:
        print(x)

    print('\n\n')

    for x in vigia:
        print(x)

    print('\n\n')

    for x in eventos:
        print(x)

    print('\n\n')

    for x in processos:
        print(x)

    print('\n\n')

    for x in entidades:
        print(x)

    print('\n\n')

    for x in meios:
        print(x)
    


printAll()
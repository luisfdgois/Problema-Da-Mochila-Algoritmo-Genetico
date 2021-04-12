# Problema Da Mochila

Trabalho da Disciplina de Inteligência Artifical - Unit 2021.01  
Equipe: José Eduardo da Costa Wynne Neto e Luis Fernando Dantas Gois.  

Está sendo utilizando o algoritmo genético como base para chegar a uma solução viável. Está sendo utilizando a linguagem Python e a lib deap para realizar as operações propostas pelo algoritmo.

Para execução do algoritmo, apresento duas opções:  
  * Utilizando a ferramenta colab do google;  
  * Instalar o python em sua máquina, caso ainda não tenha, e executar utilizando uma IDE;  

1. Instale os pacotes/libs que serão necessários(as) para a execução do projeto:  
  1.1 "!pip install deap" ou "pip install deap".  
  1.2 "!pip install matplotlib" ou "pip install matplotlib".  
  Obs.: Essa última será utilizada para gerar os gráficos da evolução das respectivas fitness dos melhores indivíduos gerados em cada geração.
  
As seguintes variáveis podem ter seus valores alterados baseado nas condições ou no ambiente que você julgar necessário ou interessante para testar:  

  * INDIVIDUAL_SIZE = Tamanho do array que representará um indivíduo.  
  * BACKPACK_WEIGHT = Peso máximo suportoda pela mochila.  
  * POPULATION_SIZE = Tamnho da população(número de indivíduos) gerada a cada interação.  
  * MAX_INTERACTION_COUNT = Máximo de interações que a estrutura de reptição terá. A contagem só será feita se satisfazer a condição da variação máxima, ou seja, se o valor da fitness do melhor indivíduo da população atual, estiver entre (maior ou menor) o valor da fitness anterior + a variação estabelecida, caso contrário, a contagem é iniciada novamente até que se chegue ao máximo estabelecido.  
  * MAX_VARIATION = Variação máxima que será estabelecida para que as soluções de cada geração, cruzem uma reta linear a partir das MAX_INTERACTION_COUNT soluções encontradas.  
  * NUMBER_ITEMS = Número de itens que estará disponível para inserir na mochila.  
  * LIST_REFERENCES = Lista dos itens.  
  * VARIATION_SIZE = Número de indivíduos que será escolhido no método da seleção.  
  * LIST_BESTINDIVIDUAL_WEIGHT = Armazenará o peso total do melhor indivíduo a cada interação.  
  * LIST_BESTINDIVIDUAL_AMOUNT = Armazenará o valor total do melhor indivíduo a cada interação.  

Ao ser executado, será exibido os itens, com seus respectivos peso e valor, que foram gerados e que estiveram disponíveis para escolha, e o gráfico, que mostrará a evolução da solução de cada geração até chegar na solução mais aproximada.

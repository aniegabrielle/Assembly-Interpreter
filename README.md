Este programa consiste em um interpretador simplificado Assembly, foi desenvolvido baseado em um trabalho universitário nestas seguintes especificações:

Vamos considerar que o processador hipotético tenha 8 Registradores chamados A, B, C, D, E, F, G e H que armazenam um inteiro (32 bits) cada um. Além desses, há o registrador PC (Program Counter) que contém o número da linha em execução e o registrador CR (Compare Result) que armazena um valor booleano referente à última instrução de comparação realizada. Além dos registradores, o interpretador considerará a existência de uma área de memória de 1024 bytes que pode ser livremente utilizada no programa. Todos os mnemônicos utilizados no programa estão escritos em letras maiúsculas e a relação dos mnemônicos está no final.

O Formato das instruções seguirá o seguinte padrão:
    [<label>:]   <MNEMÔNICO>  [<PARAM1>,<PARAM2>]     [-- comentário]

O que está em [ ] não é obrigatório. O <label> associa um rótulo à linha em questão e pode ser utilizado nos mnemônicos de JUMP. Para ser um <label>, é necessário que esteja no início da linha e com ':' colado ao final de seu nome. Cada mnemônico pode ter 0, 1 ou 2 parâmetros e se houver '--' no final da linha, é a indicação de um comentário a ser ignorado pelo interpretador. Cada linha só pode ter a presença de um mnemônico.

LISTA DOS MNEMÔNICOS

MOVE <Registrador ou Endereço de Memória ou Variável> , <Registrador ou Variável ou Literal> - Atribui ao <Registrador 1>, ou ao endereço de memória, ou à variavel, o valor presente em <Registrador 2>, ou o valor de uma literal, ou o valor de uma variável.
Ex:
    MOVE A, -29         -- Atribui em A o valor -29
    MOVE B, A            -- Atribui em B o valor presente em A
    MOVE 200, A        -- Move para a posição de memória 200 o valor presente em A
    MOVE VAR_A, B    -- Move para a posição de memória referenciada por VAR_A o valor presente em B
----------------------------------
ADD <Registrador ou Endereço de Memória ou Variável> , <Registrador ou Variável ou Literal>
Soma o valor presente em <Registrador 1>, ou ao endereço de memória, ou à variavel, com o valor presente em <Registrador 2>, ou o valor de uma literal, ou o valor de uma variável.  O resultado ficará no que está especificado no primeiro parâmetro.
Ex:
    ADD D,1  -- Incrementa o valor de D
    ADD B,D  -- Soma o valor de B com o valor de D, armazenando o resultado em B
     
Semelhante a ADD, teremos SUBT <subtração>, MULT <multiplicação> e DIV <divisão>

----------------------------------
CMP <Registrador ou Endereço de Memória ou Variável> , <Registrador ou Variável ou Literal> 
Compara o valor presente em <Registrador 1>, ou ao endereço de memória, ou à variavel, com o valor presente em <Registrador 2>, ou o valor de uma literal, ou o valor de uma variável.  Se o 1o parâmetro for igual que o 2o parâmetro, o registrador CR recebe o valor 1; senão CR recebe 0
----------------------------------
CMAIOR <Registrador ou Endereço de Memória ou Variável> , <Registrador ou Variável ou Literal> 
Compara o valor presente em <Registrador 1>, ou ao endereço de memória, ou à variavel, com o valor presente em <Registrador 2>, ou o valor de uma literal, ou o valor de uma variável.  Se o 1o parâmetro for maior que o 2o parâmetro, o registrador CR recebe o valor 1; senão CR recebe 0
----------------------------------
CMENOR <Registrador ou Endereço de Memória ou Variável> , <Registrador ou Variável ou Literal> 
Compara o valor presente em <Registrador 1>, ou ao endereço de memória, ou à variavel, com o valor presente em <Registrador 2>, ou o valor de uma literal, ou o valor de uma variável.  Se o 1o parâmetro for menor que o 2o parâmetro, o registrador CR recebe o valor 1; senão CR recebe 0
----------------------------------
JUMP <label> 
Redireciona a executação para a linha indicada por <label>

----------------------------------
JTRUE  <label> 
Redireciona a executação para a linha indicada por <label> se CR tiver um valor diferente de 0

----------------------------------
JFALSE <label> 
Redireciona a executação para a linha indicada por <label> se CR tiver um valor igual a 0

----------------------------------
INT 1 , <Endereço de Memória ou Variável> 
Interrupção tipo 1 que lê uma tecla e coloca o seu valor ASCII na posição de memória indicada

INT 2 , <Endereço de Memória ou Variável> 
Interrupção tipo 2 que escreve o valor ASCII da posição de memória indicada

----------------------------------
HALT - Para a execução do programa

----------------------------------
VAR  <nome variável>, <Endereço de Memória>  
Pseudo instrução que associa uma posição de memória a uma variável. Esse poderá ser usado pelas instruções como local para armazenamento ou leitura de valores.


Há três programas em assembly disponíveis para teste nos arquivos txt salvos. Ao iniciar o programa, basta digitar o nome do arquivo e ele rodará o script Assembly dentro dele.

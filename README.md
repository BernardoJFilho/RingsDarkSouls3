# RingsDarkSouls3
Manipulação de Arquivo CSV para Auxílio no Jogo Dark Souls 3
Este script Python permite realizar operações básicas em um arquivo CSV, como busca, marcação e desmarcação de elementos, e exibição da tabela completa ou filtrada. Ele foi desenvolvido para ajudar jogadores de Dark Souls 3 na busca pelas conquistas do jogo.

Funcionalidades
Pesquisar elementos: Busca por um termo específico na segunda coluna do arquivo CSV e exibe os resultados encontrados.

Mostrar tabela completa: Renderiza a tabela completa ou apenas as linhas que não contêm a marca 'x' na primeira coluna, conforme escolha do usuário.

Marcar elemento: Permite marcar um elemento específico na primeira coluna com 'x', indicando algum tipo de estado ou marcação.

Desmarcar elemento: Remove a marcação 'x' de um elemento previamente marcado na primeira coluna.

Acesso restrito: O acesso às funcionalidades avançadas requer que o usuário insira um nome específico ('admin') no início do programa.

Arquivo Executável
O arquivo executável main.exe foi criado a partir do script Python main.py utilizando o PyInstaller para facilitar a execução em sistemas Windows sem a necessidade de instalação de Python ou outras dependências.

Uso para Conquistas em Dark Souls 3
Este script foi projetado para ajudar os jogadores de Dark Souls 3 na busca pelas conquistas do jogo. Ele permite a organização e marcação de itens, que não necessariamente fazem parte do jogo, facilitando o acompanhamento do progresso necessário para obter todas as conquistas e platinar o jogo.

Como usar
Execução do arquivo executável:

Basta executar o arquivo main.exe para iniciar o programa:
css
Copiar código
main.exe
Menu Principal:

Digite seu nome quando solicitado. O acesso é permitido apenas se o nome inserido for 'admin'.
Selecione uma opção no menu principal digitando o número correspondente à funcionalidade desejada.
Funcionalidades:

Siga as instruções apresentadas no console para cada funcionalidade selecionada.
Utilize as opções de pesquisa, marcação, desmarcação e visualização da tabela conforme necessário.
Encerramento do programa:

Selecione a opção '5' no menu principal para sair do programa.

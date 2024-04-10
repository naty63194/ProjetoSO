# ProjetoSO
# Documentação do Código
# Visão Geral
Este código Python é uma aplicação de interface gráfica (GUI) usando Tkinter para criar um formulário de consultoria com funcionalidades de inserção, visualização, atualização e exclusão de dados. Além disso, ele possui a capacidade de gerar um arquivo de extrato contendo os dados do formulário em um formato de texto.

# Módulos e Bibliotecas
Tkinter: Utilizado para a criação da interface gráfica.
tkcalendar: Biblioteca adicional para integrar um widget de calendário à interface.
datetime: Usado para manipulação de datas e hora.
filedialog: Parte do módulo Tkinter para abrir caixas de diálogo de arquivos.
messagebox: Para exibir caixas de diálogo de mensagem.
sqlite3: Utilizado para interagir com o banco de dados SQLite que armazena os dados do formulário.
# Cores Utilizadas
Cores definidas em variáveis globais representando uma paleta de cores utilizada na interface.
# Estrutura da Interface Gráfica
Janela Principal: Criada com Tkinter, definindo o título, tamanho e cor de fundo. Não pode ser redimensionada.
Frames: A janela principal é dividida em três frames: superior, inferior e direita.
O frame superior é usado para fins de visualização.
O frame inferior contém campos de entrada para inserção de dados e botões para operações.
O frame direito exibe os dados do formulário em uma tabela e é usado para operações de atualização e exclusão.
# Funcionalidades Principais
Função mostrar(): Exibe os dados do formulário em uma tabela no frame direito da janela principal.
Função inserir(): Insere novos dados no banco de dados quando o usuário preenche os campos no frame inferior e clica no botão "Enviar".
Função atualizar(): Permite atualizar dados existentes. Quando o usuário seleciona uma entrada na tabela e clica no botão "Atualizar", os dados dessa entrada são carregados nos campos do frame inferior, permitindo que o usuário os atualize e confirme as mudanças.
Função deletar(): Remove uma entrada selecionada na tabela.
Função gerar_extrato(): Gera um arquivo de extrato contendo os dados do formulário em formato de texto.
# Banco de Dados
Utiliza um banco de dados SQLite chamado "dados.db" para armazenar os dados do formulário.
A estrutura do banco de dados inclui uma tabela chamada "formulario" com colunas para ID, Nome, Email, Telefone e Data.
Módulo view
Contém funções para interagir com o banco de dados, como inserção, consulta, atualização e exclusão de dados.

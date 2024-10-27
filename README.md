<h1 align="center">
<img src="./assets/RockInRio_1985.webp"/>
<p>Rock in Rio 2024 🎸</p>
</h1>

<h2 align="center"><p>📌 Objetivo do programa</p</h2>
<h3>

> Armazenar diversas informações de serviços disponíveis no show

</h3>

<h4>

>> *O Foco do programa é para os funcionários do evento*

>>>  ***Um Projeto de implementação de várias estruturas de dados*** 

<h2 align = center>

 📽️Vídeozinho do projeto rodando

</h2>

<div align = center>

![Gif-Exemplo do Projeto](./assets/videozinho.gif "Gif do Video")

</div>

<h6 align="center">

![Vídeo do Projeto Imagem](./assets/video_do_projeto.png)

</h6>

</h4>

<h2 align="center">⚙️Quais as funções desse programa?</h2>

> #### ***1. Registra, armazena, remove, edita, busca e exibe:***
````
Consultas, Instrumentos da Clínica, pacientes;

Convidados do Evento, Cronograma, Playlist;

Cardapio, Faturamento, Funcionários do Restaurante (classe Restaurante).
````
> #### ***2. Adicionais:***
````
Histórico médico em Consulta; 

Gerenciar Mesas em Cardapio 
(Adicionar Mesa, Ocupar/Liberar mesa, Status Mesas);

Soma do Faturamento na classe Faturamento ao vivo;

Soma do Salário na classe Restaurante também ao vivo;
````
> #### ***3.  Conta e Mostra a quantidade de itens armanenados para localizar melhor onde ele está***

> #### ***4. Atualiza os outputs do programa ("Dá um Refresh" = Atualizar Lista)***

> #### ***5. Verifica e retorna tem algo armazenado***


<h2 align="center">🛠️Quais as ferramentas usadas nesse projeto?</h2>

> - [Python](https://docs.python.org/3/ "Documentação do Python")🐍
> - [Tk](https://docs.python.org/pt-br/3/library/tkinter.html "Documentação do Tkinter") 🪟

<h2 align="center">📂 O que tem de importante nas pastas principais?</h2>

<div align="center">

|Clinica |Eventos|Restaurante|Listas|
| :---: | :---: | :---: | :---: | 
|Consulta| Convidado | Cardapio | Encadeada Circular
|Instrumento| Cronograma | Faturamento | Encadeada Dupla
|Paciente| Playlist | Restaurante | Encadeada Simples

</div>

<h2 align="center">🧐Como executar?</h2>


````python
# Dê dois cliques em Rock in Rio.ink ou vá na pasta "dist" e dê dois cliques em main.exe
````
````python
# Ou com python instalado rode com terminal nesta pasta
  
  $ py main.py 
  
````

<h2 align="center">❓Tomada de Decisão</h2>

<h6 align="center">

***5 perguntas que podem ser respondidas utilizando operações nas listas***

</h6>

````
1) Qual a eficiência na gestão de inventários rotativos dos materiais da Clínica?

Com o Instrumento (lista_encadeada_dupla), 
podemos rastrear produtos no inventário rotativo 
de instrumentos para a Clínica, otimizando o estoque dos materiais 
e redução de custos operacionais.

Operações: “adicionar_item()” para adicionar produtos novos, 
“remover_item()” para retirar produtos antigos, 
“contar_itens()” para saber e manter controle do total de itens.
````
````
2) Como podemos rastrear o histórico de mudanças de preços de produtos do Cardápio?

O Cardapio (lista_encadeada_simples) permite navegação no histórico, 
ajudando na Análise/Tomadas de decisão 
comparando com as tendências de preços do mercado.

Operações: “adicionar_item()” para registrar nova alteração de preço, 
“buscar_um_item()” para consultar histórico de um item no cardápio, 
“atualizar_item()” para corrigir se necessitar.
````
````
3) Como melhorar o rastreamento de vendas mensais?

Faturamento (lista_encadeada_simples) 
para faturamento financeiro do Restaurante 
e assim temos melhor controle financeiro e tomadas de decisão.

Operações: “adicionar_item()” para novas vendas, 
“buscar_um_item()” para verificar, 
“atualizar_item()” em correções, 
"somar_e_faturamento" para ter o faturamento atualizado na tela.
````
````
4) Como melhorar o fluxo de acompanhamento de histórico dos meus pacientes?

Utilize Paciente (lista_encadeada_dupla) para facilitar 
a visualização dos pacientes presentes e assim melhor qualidade e 
agilidade no atendimento e consequentemente uma precisão diagnóstica.

Operações: “adicionar_item()” para novos pacientes, 
“buscar_um_item()” para  consultar o nome do paciente, 
“atualizar_item()” para mudar o prontuário.
````
````
5) Como melhorar a gestão dos horários entre as atividades do evento?

Use o Cronograma (lista_encadeada_circular) para relacionar atividades 
e então melhorar o planejamento do evento, assim reduzindo o atraso.

Operações: “adicionar_item()” para novas atividades, 
“buscar_um_item()” para verificar anteriores, 
“atualizar_item()” para ajustes de cronograma.
````


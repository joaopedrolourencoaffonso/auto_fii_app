## Documentação do código
Nota: eu criei esse script anos atrás como uma forma de estudar, boas práticas de programação não eram uma preocupação.

### Propósito
O objetivo desse código é extrair dados de um site e aplicar filtragem com base em determinados critérios.

### Dependências
As seguintes dependências são necessárias para executar o código:
- `sys`: Fornece acesso a parâmetros e funções específicos do sistema.
- `webbrowser`: Fornece uma interface de alto nível para exibir documentos baseados na web.
- `requests`: Permite enviar requisições HTTP e tratar respostas.
- `bs4` (BeautifulSoup): Uma biblioteca para extrair dados de arquivos HTML e XML.

### Função `filters(fpreco, fyield, pvp)`
Esta função é usada para dividir as strings de entrada (`fpreco`, `fyield`, `pvp`) por ponto e vírgula e realizar comparações com base nos valores extraídos. A função retorna uma tupla contendo o resultado das comparações e os valores extraídos.

### Código principal
O código principal começa recuperando os argumentos da linha de comando (`fpreco`, `fyield`, `pvp`) usando `sys.argv`. Então, a função `filters()` é chamada para realizar comparações nos valores de entrada.

Se a função retornar `2`, uma mensagem de erro será impressa indicando que está faltando um ponto e vírgula em um dos filtros. Se a função retornar `1`, uma mensagem de erro é impressa indicando que um dos limites do filtro possui uma faixa inválida. Caso contrário, o código prossegue para extrair dados de um site.

O código faz uma solicitação HTTP para "https://fiis.com.br/lista-de-fundos-imobiliários/" usando a biblioteca `requests`. Em seguida, ele extrai informações específicas do HTML usando BeautifulSoup (`bs4`). Os dados extraídos são armazenados em variáveis como `nome`, `preco`, `yield_value`, `ultimo_rend`, `patrimonio` e `valor_patr`. Cálculos adicionais são realizados nessas variáveis.

Com base nas condições do filtro e nas comparações com os dados extraídos, o código constrói uma string HTML (`string`) contendo as informações relevantes. Finalmente, a `string` é impressa.

### Uso
Para executar o código, você precisa fornecer três argumentos de linha de comando: `fpreco`, `fyield` e `pvp`, cada um separado por espaços.

Exemplo de uso:
```
python script.py argumento1 argumento2 argumento3
```

### Limitações
- O código assume que a estrutura do site permanece inalterada. Quaisquer alterações na estrutura HTML do site podem quebrar o código.
- O código não fornece tratamento de erros para possíveis exceções que podem ocorrer durante solicitações HTTP ou análise de HTML.

### Outras melhorias
- Adicionar tratamento de erros e tratamento de exceções para melhorar a robustez do código.
- Implemente o log para registrar quaisquer possíveis problemas ou erros durante a execução.
- Refatore o código em funções separadas para melhorar a modularidade e a legibilidade.
- Inclua testes de unidade para verificar a funcionalidade de componentes individuais.

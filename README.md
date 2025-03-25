# Arcee CLI Demo

Demonstração da CLI para integração com Trello usando o Arcee AI.

## Descrição

Este repositório contém uma demonstração da implementação de uma CLI para integração com o Trello, usando Python, Typer e Rich para criar uma interface de linha de comando moderna e amigável.

## Comandos implementados

- `listar-listas`: Lista todas as listas do quadro Trello
- `listar-cards`: Lista todos os cards do quadro ou de uma lista específica
- `criar-lista`: Cria uma nova lista no quadro Trello
- `criar-card`: Cria um novo card em uma lista do Trello
- `arquivar-card`: Arquiva um card do Trello
- `atividade`: Lista as atividades recentes no quadro Trello
- `meus-cards`: Lista todos os cards atribuídos a você
- `atualizar-card`: Atualiza os detalhes de um card existente no Trello
- `arquivar-lista`: Arquiva uma lista do Trello

## Tecnologias utilizadas

- Python 3.8+
- [Typer](https://typer.tiangolo.com/) - Framework para CLI
- [Rich](https://rich.readthedocs.io/) - Formatação de saída no terminal
- MCPRunClient - Cliente para APIs externas

## Integração com MCP

A integração com o MCP (Model-Controlled Programming) permite acessar ferramentas externas através de chamadas de API estruturadas, facilitando a criação de aplicações que interagem com serviços como o Trello.

## Exemplo de uso

```bash
# Listar todas as listas do quadro
python trello_commands.py listar-listas

# Listar cards de uma lista específica
python trello_commands.py listar-cards list1
```

## Licença

MIT
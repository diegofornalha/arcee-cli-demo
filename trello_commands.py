#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comandos Trello para a CLI Arcee
"""

import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from datetime import datetime
import logging

# Configuração de logging
logger = logging.getLogger("arcee_cli.trello")
console = Console()

# Inicializa app do Typer
trello_app = typer.Typer(
    help="""
    📋 Gerenciamento de Trello

    Comandos para gerenciar quadros e cards do Trello.
    """
)


# Simulação da classe MCPRunClient
class MCPRunClient:
    def __init__(self, session_id=None):
        self.session_id = session_id
        
    def run_tool(self, name, params):
        # Simulação de resposta da API - na implementação real isso seria substituído
        # por chamadas reais à API do Trello via MCP
        if name == "get_lists":
            return {
                "lists": [
                    {"id": "list1", "name": "Tarefas", "cardCount": 3},
                    {"id": "list2", "name": "Em Progresso", "cardCount": 2},
                    {"id": "list3", "name": "Concluído", "cardCount": 5}
                ]
            }
        elif name == "get_cards_by_list_id":
            list_id = params.get("listId")
            if list_id == "list1":
                return {
                    "cards": [
                        {"id": "card1", "name": "Implementar CLI", "desc": "Criar CLI para Trello"},
                        {"id": "card2", "name": "Testar comandos", "desc": "Verificar funcionamento"},
                        {"id": "card3", "name": "Documentar API", "desc": "Criar documentação"}
                    ]
                }
            return {"cards": []}
        return {"error": "Comando não implementado na simulação"}


# Inicialização do cliente MCP
def get_agent():
    return MCPRunClient(session_id="demo-session")


@trello_app.command("listar-listas")
def listar_listas_trello():
    """Lista todas as listas do quadro Trello"""
    logger.info("Listando listas do Trello")
    
    # Usa o agente para obter as listas
    agent = get_agent()
    try:
        response = agent.run_tool("get_lists", {"random_string": "dummy"})
        
        if "error" in response:
            print(f"❌ Erro: {response['error']}")
            return
            
        # Exibe as listas em uma tabela
        table = Table(title="📋 Listas do Trello")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="green")
        table.add_column("Cards", style="magenta")
        
        for lista in response.get("lists", []):
            table.add_row(
                lista.get("id", "N/A"),
                lista.get("name", "N/A"),
                str(lista.get("cardCount", 0))
            )
            
        console.print(table)
    except Exception as e:
        print(f"❌ Erro ao listar listas: {e}")
        logger.exception(f"Erro ao listar listas do Trello: {e}")


@trello_app.command("listar-cards")
def listar_cards_trello(
    lista_id: Optional[str] = typer.Argument(None, help="ID da lista para filtrar os cards")
):
    """Lista todos os cards do quadro ou de uma lista específica"""
    logger.info(f"Listando cards do Trello (lista_id={lista_id})")
    
    # Usa o agente para obter as cards
    agent = get_agent()
    try:
        # Exibe os cards de uma lista específica
        response = agent.run_tool("get_cards_by_list_id", {"listId": lista_id or "list1"})
        
        if "error" in response:
            print(f"❌ Erro: {response['error']}")
            return
            
        # Exibe os cards em uma tabela
        table = Table(title=f"🗂️ Cards da Lista {lista_id or 'list1'}")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="green")
        table.add_column("Descrição", style="magenta")
        
        for card in response.get("cards", []):
            table.add_row(
                card.get("id", "N/A"),
                card.get("name", "N/A"),
                card.get("desc", "")[:50] + ("..." if len(card.get("desc", "")) > 50 else "")
            )
            
        console.print(table)
    except Exception as e:
        print(f"❌ Erro ao listar cards: {e}")
        logger.exception(f"Erro ao listar cards do Trello: {e}")


if __name__ == "__main__":
    trello_app()
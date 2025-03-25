#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cliente simplificado para MCP.run
"""

import os
import json
import requests
import logging

logger = logging.getLogger("arcee_cli.mcprun")

class MCPRunClient:
    """
    Cliente simplificado para interagir com MCP.run
    """
    
    def __init__(self, session_id=None, api_base_url="https://api.mcp.run/v1"):
        """
        Inicializa o cliente MCP
        
        Args:
            session_id (str, optional): ID de sessão do MCP.run
            api_base_url (str, optional): URL base da API
        """
        self.session_id = session_id
        self.api_base_url = api_base_url
        
        # Carrega o session_id do arquivo de configuração, se não for fornecido
        if not self.session_id:
            config_file = os.path.expanduser("~/.arcee/config.json")
            if os.path.exists(config_file):
                try:
                    with open(config_file, "r", encoding="utf-8") as f:
                        config = json.load(f)
                        self.session_id = config.get("mcp_session_id")
                except Exception as e:
                    logger.error(f"Erro ao carregar ID de sessão MCP.run: {e}")
        
        # Verifica se temos um session_id
        if not self.session_id:
            logger.warning("ID de sessão MCP.run não configurado")
    
    def get_tools(self):
        """
        Lista todas as ferramentas disponíveis
        
        Returns:
            list: Lista de ferramentas disponíveis
        """
        if not self.session_id:
            return []
            
        try:
            response = requests.get(
                f"{self.api_base_url}/session/{self.session_id}/tools",
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                tools_data = response.json()
                return tools_data.get("tools", [])
            else:
                logger.error(f"Erro ao obter ferramentas: {response.status_code} - {response.text}")
                return []
        except Exception as e:
            logger.exception(f"Erro ao listar ferramentas: {e}")
            return []
    
    def run_tool(self, tool_name, params=None):
        """
        Executa uma ferramenta específica
        
        Args:
            tool_name (str): Nome da ferramenta a ser executada
            params (dict, optional): Parâmetros da ferramenta
            
        Returns:
            dict: Resultado da execução da ferramenta
        """
        if not self.session_id:
            return {"error": "ID de sessão MCP.run não configurado"}
        
        if params is None:
            params = {}
            
        try:
            response = requests.post(
                f"{self.api_base_url}/session/{self.session_id}/tool/{tool_name}/run",
                headers={"Content-Type": "application/json"},
                json={"params": params}
            )
            
            # Processa a resposta
            if response.status_code == 200:
                result = response.json()
                return result.get("result", {})
            else:
                error_message = f"Erro ao executar ferramenta: {response.status_code} - {response.text}"
                logger.error(error_message)
                return {"error": error_message, "raw_output": response.text}
        except Exception as e:
            error_message = f"Exceção ao executar ferramenta: {str(e)}"
            logger.exception(error_message)
            return {"error": error_message}


def configure_mcprun(session_id=None):
    """
    Configura o cliente MCP.run
    
    Args:
        session_id (str, optional): ID de sessão existente
        
    Returns:
        str: ID de sessão configurado
    """
    # Na implementação real, aqui verificaríamos o session_id ou criaríamos um novo
    # Simplificado para este exemplo
    return session_id or "demo-session-id"


if __name__ == "__main__":
    # Exemplo de uso
    client = MCPRunClient(session_id="demo-session")
    
    print("Ferramentas disponíveis:")
    tools = client.get_tools()
    for tool in tools:
        print(f"- {tool['name']}: {tool['description']}")
        
    print("\nExecutando ferramenta:")
    result = client.run_tool("get_lists", {"random_string": "dummy"})
    print(json.dumps(result, indent=2))
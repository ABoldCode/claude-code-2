#!/usr/bin/env python3
"""
Claude API Direct - Sin OAuth
Script para usar Claude directamente desde línea de comandos
EVITA las restricciones de Claude Code oficial
"""

import os
import requests
import json
import sys

def chat_with_claude(message, api_key):
    """Envía mensaje a Claude usando API directa"""
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key,
        'anthropic-version': '2023-06-01'
    }
    
    data = {
        'model': 'claude-3-sonnet-20240229',
        'max_tokens': 4000,
        'messages': [{'role': 'user', 'content': message}]
    }
    
    try:
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['content'][0]['text']
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error de conexión: {str(e)}"

def main():
    """Función principal"""
    
    # Obtener API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ No se encontró ANTHROPIC_API_KEY")
        print("📝 Configura tu API key:")
        print("   $env:ANTHROPIC_API_KEY = 'sk-ant-api03-tu-clave-aqui'")
        print("")
        print("🔑 Obtén tu API key en: https://console.anthropic.com/")
        return
    
    print("🚀 Claude API Direct - ¡Listo!")
    print("💬 Escribe 'exit' para salir")
    print("🔧 Comandos especiales:")
    print("   'code <pregunta>' - Para ayuda con código")
    print("   'help' - Para ayuda general")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n🤖 Tú: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'salir']:
                print("👋 ¡Hasta luego!")
                break
                
            if not user_input:
                continue
                
            # Comando especial para código
            if user_input.lower().startswith('code '):
                question = user_input[5:]
                prompt = f"Eres un experto programador. Ayúdame con esta pregunta de programación: {question}"
            else:
                prompt = user_input
                
            print("🔄 Claude está pensando...")
            response = chat_with_claude(prompt, api_key)
            print(f"\n✨ Claude: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 
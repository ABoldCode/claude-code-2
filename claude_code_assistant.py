#!/usr/bin/env python3
"""
Claude Code Assistant - Especializado en programación
Alternativa a Claude Code oficial que funciona en entornos corporativos
"""

import os
import requests
import json
import sys
import glob
from pathlib import Path

def chat_with_claude(message, api_key):
    """Envía mensaje a Claude con contexto de programación"""
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key,
        'anthropic-version': '2023-06-01'
    }
    
    # Prompt optimizado para programación
    system_prompt = """Eres un experto programador y arquitecto de software. 
    Ayudas con:
    - Análisis de código
    - Depuración de errores
    - Mejores prácticas
    - Arquitectura de software
    - Optimización de código
    
    Responde de manera clara y práctica."""
    
    data = {
        'model': 'claude-3-sonnet-20240229',
        'max_tokens': 4000,
        'system': system_prompt,
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

def analyze_project():
    """Analiza archivos del proyecto actual"""
    code_files = []
    extensions = ['*.py', '*.js', '*.ts', '*.java', '*.cpp', '*.c', '*.cs', '*.php', '*.rb', '*.go']
    
    for ext in extensions:
        code_files.extend(glob.glob(ext))
        code_files.extend(glob.glob(f"**/{ext}", recursive=True))
    
    if not code_files:
        return "No se encontraron archivos de código en el directorio actual."
    
    analysis = f"📁 Proyecto analizado:\n"
    analysis += f"📊 {len(code_files)} archivos de código encontrados:\n\n"
    
    for file in code_files[:10]:  # Limitar a 10 archivos
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
                analysis += f"  🔹 {file} ({lines} líneas)\n"
        except:
            analysis += f"  🔹 {file} (no legible)\n"
    
    if len(code_files) > 10:
        analysis += f"  ... y {len(code_files) - 10} archivos más\n"
    
    return analysis

def read_file_content(filepath):
    """Lee el contenido de un archivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return f"📄 Contenido de {filepath}:\n```\n{content}\n```"
    except Exception as e:
        return f"❌ Error leyendo {filepath}: {e}"

def main():
    """Función principal"""
    
    # Obtener API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ No se encontró ANTHROPIC_API_KEY")
        print("📝 Configura tu API key:")
        print("   $env:ANTHROPIC_API_KEY = 'sk-ant-api03-tu-clave-aqui'")
        print("🔑 Obtén tu API key en: https://console.anthropic.com/")
        return
    
    print("👨‍💻 Claude Code Assistant - ¡Especialista en Programación!")
    print("💬 Escribe 'exit' para salir")
    print("\n🔧 Comandos especiales:")
    print("   'analyze' - Analizar proyecto actual")
    print("   'read <archivo>' - Leer contenido de archivo")
    print("   'help' - Ayuda con programación")
    print("   'debug <descripción>' - Ayuda con depuración")
    print("   'review <archivo>' - Revisión de código")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n👨‍💻 Tú: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'salir']:
                print("👋 ¡Hasta luego!")
                break
                
            if not user_input:
                continue
            
            # Comandos especiales
            if user_input.lower() == 'analyze':
                result = analyze_project()
                print(f"\n📊 {result}")
                continue
                
            elif user_input.lower().startswith('read '):
                filepath = user_input[5:].strip()
                content = read_file_content(filepath)
                print(f"\n{content}")
                continue
                
            elif user_input.lower().startswith('debug '):
                problem = user_input[6:]
                prompt = f"Ayúdame a depurar este problema de programación: {problem}. Proporciona pasos específicos y posibles soluciones."
                
            elif user_input.lower().startswith('review '):
                filepath = user_input[7:].strip()
                file_content = read_file_content(filepath)
                prompt = f"Por favor revisa este código y sugiere mejoras:\n\n{file_content}"
                
            else:
                prompt = user_input
            
            print("🔄 Claude está analizando...")
            response = chat_with_claude(prompt, api_key)
            print(f"\n✨ Claude Code Assistant: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 
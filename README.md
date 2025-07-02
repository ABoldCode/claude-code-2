# Claude Code Alternative - Proyecto de Desarrollo

Este proyecto contiene **scripts alternativos** a Claude Code que funcionan en **entornos corporativos** sin restricciones OAuth.

## 🎯 Problema Resuelto

Claude Code oficial requiere OAuth que está **bloqueado en redes corporativas**. Nuestros scripts usan la **API directa de Anthropic** sin restricciones.

## 📁 Contenido

- `claude_api_direct.py` - Chat general con Claude
- `claude_code_assistant.py` - **Especialista en programación** 
- `instrucciones.ini` - Configuraciones del proyecto

## 🚀 Instalación y Uso

### 1. Instalar dependencias:
```bash
pip install requests anthropic
```

### 2. Configurar API Key:
```powershell
# Obtén tu API key en: https://console.anthropic.com/
$env:ANTHROPIC_API_KEY = "sk-ant-api03-tu-clave-aqui"
```

### 3. Usar los scripts:

#### Chat General:
```bash
python claude_api_direct.py
```

#### Asistente de Programación:
```bash
python claude_code_assistant.py
```

## 🔧 Comandos del Code Assistant

- `analyze` - Analizar proyecto actual
- `read <archivo>` - Leer contenido de archivo  
- `debug <problema>` - Ayuda con depuración
- `review <archivo>` - Revisión de código
- `exit` - Salir

## ✅ Ventajas vs Claude Code Oficial

| Claude Code Oficial | Nuestros Scripts |
|---|---|
| ❌ Requiere OAuth | ✅ API key directa |
| ❌ Bloqueado corporativo | ✅ Solo HTTPS estándar |
| ❌ No acepta sk-proj- keys | ✅ Cualquier API key válida |
| ❌ Validaciones especiales | ✅ API estándar |

## 🏢 Ideal para Entornos Corporativos

- **Sin bloqueos de red**
- **Sin OAuth**
- **Funciona con proxy corporativo**
- **API key estándar de Anthropic**

## 👨‍💻 Autor
ABoldCode (al.bold83@gmail.com) 
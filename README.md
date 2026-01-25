# 🤖 Gemini Autonomous Code Agent

¡Bienvenido! Este repositorio contiene un Agente de IA autónomo construido con **Google Gemini**, diseñado para navegar por sistemas de archivos, leer código, ejecutar scripts de Python y corregir errores de forma independiente.

Este proyecto nació como parte del desafío técnico en **Boot.dev**, donde llevamos la IA más allá de un simple chat, convirtiéndola en un colaborador activo con capacidad de ejecución.

---

## 🚀 Tecnologías Usadas

* **Core AI:** [Google Gemini 2.0 Flash](https://ai.google.dev/) (vía Google GenAI SDK).
* **Lenguaje:** Python 3.11+.
* **Gestión de Dependencias:** [uv](https://github.com/astral-sh/uv) (extremadamente rápido).
* **Arquitectura:** Agentic Loop (Observe-Think-Act).
* **Tooling:** Function Calling, System Instructions, Context Management.

---

## 🧠 Capacidades del Agente

El agente opera en un bucle de razonamiento continuo y tiene acceso a las siguientes herramientas:

1. **Exploración:** Lista archivos y directorios para entender la estructura del proyecto.
2. **Lectura:** Analiza el contenido de archivos específicos.
3. **Escritura:** Realiza modificaciones precisas en el código (como arreglar bugs de precedencia).
4. **Ejecución:** Corre scripts de Python para validar sus propios arreglos.
5. **Memoria:** Mantiene un historial de mensajes y resultados de herramientas para tomar decisiones informadas.

---

## 🛠️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/gemini-autonomous-agent.git
   cd gemini-autonomous-agent
   ```

2. **Configurar el entorno:**
   Crea un archivo `.env` con tu API Key:
   ```
   GEMINI_API_KEY=tu_api_key_aqui
   ```

3. **Ejecutar el agente:**
   Pídele que resuelva una tarea compleja, como arreglar un bug en una carpeta específica:
   ```bash
   uv run main.py "Fix the bug in the calculator app: 3 + 7 * 2 shouldn't be 20." --verbose
   ```

---

## 🏆 Créditos y Agradecimientos

Un aplauso gigante y de pie para **Boot.dev** 👏. Gracias a su enfoque práctico y riguroso ("Learn by doing"), este proyecto pasó de ser una idea a un agente funcional capaz de manipular archivos en un entorno de sandbox seguro. ¡La mejor academia para desarrolladores que quieren ensuciarse las manos con código real!

---

## 🛡️ Sandbox & Seguridad

El agente está configurado para operar dentro de un directorio de trabajo seguro (`working_directory`), evitando que realice cambios accidentales fuera del área designada. Es un ejemplo perfecto de cómo implementar IA con barandillas de seguridad.

Desarrollado con ❤️ por Ignacio Robles (Nacho).
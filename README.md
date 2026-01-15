# VenadosRater

Aplicación web para evaluar profesores del Instituto Tecnológico de Hermosillo (ITH).

## Características
- Búsqueda de profesores
- Evaluaciones anónimas (Calidad y Dificultad)
- Directorio por departamentos

## Tecnologías
- Python 3.11+
- Flask
- Supabase (PostgreSQL)
- Bootstrap 5

## Instalación Local

1. Clonar repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno virtual: `.\venv\Scripts\activate`
4. Instalar dependencias: `pip install -r venadosrater/requirements.txt`
5. Crear archivo `.env` en `venadosrater/` basado en la plantilla
6. Ejecutar: 
   ```bash
   cd venadosrater
   flask run
   ```

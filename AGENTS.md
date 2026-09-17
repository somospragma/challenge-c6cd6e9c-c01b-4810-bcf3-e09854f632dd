# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Backend, Especialidad Desarrollador, Tecnología Python, Advanced

### Brecha de conocimiento
Ha trabajado con algún asistente AI en desarrollo (Amazon Q Dev, Kiro, Github Copilot) y lo utiliza en su día a día como desenvolvedor

### Misión / candidato
Candidato con experiencia en desarrollo backend con Python en equipo profesional

### Reto
- Tema: Desarrollo
- Seniority: advanced-l1
- Tipo: practical
- Título: Desarrollo de un Sistema de Gestión de Tareas
- Tiempo estimado: 4-6 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición del Modelo de Datos — objetivo: Definir la estructura de datos para las tareas y sus atributos. — entregable (NO resolver): Diagrama de modelo de datos para las tareas.
- Fase 2: Implementación de la Creación de Tareas — objetivo: Implementar la funcionalidad para crear nuevas tareas. — entregable (NO resolver): Módulo funcional para crear nuevas tareas.
- Fase 3: Implementación de la Actualización de Tareas — objetivo: Implementar la funcionalidad para actualizar tareas existentes. — entregable (NO resolver): Módulo funcional para actualizar tareas existentes.
- Fase 4: Implementación de la Eliminación de Tareas — objetivo: Implementar la funcionalidad para eliminar tareas. — entregable (NO resolver): Módulo funcional para eliminar tareas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "task-management-system"
version = "0.1.0"
description = "A task management system for a development team."
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "0.115.0"
pydanticv2 = "2.5.3"
sqlalchemy = "2.0.23"

[tool.poetry.dev-dependencies]
pytest = "7.4.3"

[tool.poetry.scripts]
start = "uvicorn main:app --host 0.0.0.0 --port 8000"

// === ARCHIVO: src/main/domain/task.py ===
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    title: str
    description: str
    status: TaskStatus
    due_date: datetime

// === ARCHIVO: src/main/application/task_service.py ===
from..domain.task import Task, TaskStatus
from..infrastructure.database import TaskRepository

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def create_task(self, task: Task):
        return self.task_repo.create_task(task)

    def update_task(self, task_id: int, task: Task):
        return self.task_repo.update_task(task_id, task)

    def delete_task(self, task_id: int):
        return self.task_repo.delete_task(task_id)

// === ARCHIVO: src/main/infrastructure/database.py ===
from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from..domain.task import Task, TaskStatus

Base = declarative_base()

class TaskModel(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(TaskStatus))
    due_date = Column(DateTime)

engine = create_engine('sqlite:///./test.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

class TaskRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_task(self, task: Task):
        db_task = TaskModel(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update_task(self, task_id: int, task: Task):
        db_task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            for key, value in task.dict().items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        return None

    def delete_task(self, task_id: int):
        db_task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
            return db_task
        return None

// === ARCHIVO: src/main/api/task_endpoints.py ===
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from..application.task_service import TaskService
from..domain.task import Task, TaskStatus
from..infrastructure.database import TaskRepository

router = APIRouter()

def get_task_service():
    task_repo = TaskRepository()
    return TaskService(task_repo)

@router.post('/tasks/', response_model=Task)
async def create_task(task: Task, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)

@router.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task, task_service: TaskService = Depends(get_task_service)):
    updated_task = task_service.update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return updated_task

@router.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    deleted_task = task_service.delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return deleted_task

// === ARCHIVO: src/main/config/settings.py ===
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()

// === ARCHIVO: tests/test_task_service.py ===
from unittest.mock import Mock
from src.main.application.task_service import TaskService
from src.main.domain.task import Task, TaskStatus

def test_create_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    task = Task(title="Test Task", description="Test Description", status=TaskStatus.PENDING, due_date=datetime.now())
    created_task = task_service.create_task(task)
    assert created_task.title == "Test Task"

def test_update_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    task = Task(title="Test Task", description="Test Description", status=TaskStatus.PENDING, due_date=datetime.now())
    updated_task = task_service.update_task(1, task)
    assert updated_task is not None

def test_delete_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    deleted_task = task_service.delete_task(1)
    assert deleted_task is not None

// === ARCHIVO: main.py ===
from fastapi import FastAPI
from src.main.api.task_endpoints import router as task_router

app = FastAPI()

app.include_router(task_router)

```

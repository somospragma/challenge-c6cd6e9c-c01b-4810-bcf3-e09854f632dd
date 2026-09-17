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
- Seniority: advanced-l2
- Tipo: practical
- Título: Desarrollo de un Microservicio de Gestión de Productos
- Tiempo estimado: 4-6 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición de Requisitos y Diseño Inicial — objetivo: Definir los requisitos funcionales y no funcionales del microservicio y diseñar su estructura inicial. — entregable (NO resolver): Documento de diseño inicial con los requisitos y la estructura propuesta del microservicio.
- Fase 2: Implementación de Endpoints y Validaciones — objetivo: Implementar los endpoints del microservicio y las validaciones necesarias para asegurar la integridad de los datos. — entregable (NO resolver): Microservicio con endpoints implementados y validaciones funcionales.
- Fase 3: Integración y Pruebas — objetivo: Integrar el microservicio con otros componentes del sistema y realizar pruebas exhaustivas. — entregable (NO resolver): Microservicio integrado y pruebas unitarias y de integración realizadas.

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

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# === ARCHIVO: src/main/app/__init__.py ===
from.core import get_db
from.api import router

app = FastAPI()

app.include_router(router)

# === ARCHIVO: src/main/app/core/__init__.py ===
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === ARCHIVO: src/main/app/api/__init__.py ===
from fastapi import APIRouter
from..models import Product
from..schemas import ProductCreate, ProductUpdate, ProductResponse
from..services import ProductService

router = APIRouter()

product_service = ProductService()

@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, product)

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, product_id)

# === ARCHIVO: src/main/app/models/__init__.py ===
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    stock = Column(Integer)
    category = Column(String)

# === ARCHIVO: src/main/app/schemas/__init__.py ===
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: str = Field(..., min_length=1, max_length=100)

class ProductUpdate(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    price: float = Field(None, gt=0)
    stock: int = Field(None, ge=0)
    category: str = Field(None, min_length=1, max_length=100)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: str

# === ARCHIVO: src/main/app/services/__init__.py ===
from sqlalchemy.orm import Session
from..models import Product
from..schemas import ProductCreate, ProductUpdate, ProductResponse

class ProductService:
    def create_product(self, db: Session, product: ProductCreate):
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return ProductResponse.from_orm(db_product)

    def get_product(self, db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductResponse.from_orm(product)

    def update_product(self, db: Session, product_id: int, product: ProductUpdate):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return ProductResponse.from_orm(db_product)

    def delete_product(self, db: Session, product_id: int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}

# === ARCHIVO: src/main/app/tests/unit/test_product_service.py ===
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from..services import ProductService
from..schemas import ProductCreate, ProductUpdate
from..models import Product

def test_create_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product_create = ProductCreate(name="Product 1", price=10.0, stock=100, category="Category 1")
    product = Product(**product_create.dict())
    db.query.return_value.filter.return_value.first.return_value = None
    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.return_value = None
    result = product_service.create_product(db, product_create)
    assert result.name == product_create.name

def test_get_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.get_product(db, 1)
    assert result.id == product.id

def test_update_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    product_update = ProductUpdate(name="Product 2", price=20.0, stock=200, category="Category 2")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.update_product(db, 1, product_update)
    assert result.name == product_update.name

def test_delete_product():
    db = MagicMock(spec=Session)
    product_service = ProductService()
    product = Product(id=1, name="Product 1", price=10.0, stock=100, category="Category 1")
    db.query.return_value.filter.return_value.first.return_value = product
    result = product_service.delete_product(db, 1)
    assert result["message"] == "Product deleted"

# === ARCHIVO: src/main/app/tests/integration/test_product_endpoints.py ===
from fastapi.testclient import TestClient
from..main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"}

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"}

def test_update_product():
    response = client.put("/products/1", json={"name": "Product 2", "price": 20.0, "stock": 200, "category": "Category 2"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 2", "price": 20.0, "stock": 200, "category": "Category 2"}

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted"}

# === ARCHIVO: docs/openapi/openapi.yaml ===
openapi: 3.0.3
info:
  title: Product Management API
  version: 1.0.0
paths:
  /products/:
    post:
      summary: Create a new product
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProductCreate'
      responses:
        '200':
          description: Product created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProductResponse'
  /products/{product_id}:
    get:
      summary: Get a product by ID
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Product retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProductResponse'
        '404':
          description: Product not found
    put:
      summary: Update a product by ID
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProductUpdate'
      responses:
        '200':
          description: Product updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProductResponse'
        '404':
          description: Product not found
    delete:
      summary: Delete a product by ID
      parameters:
        - name: product_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Product deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string

components:
  schemas:
    ProductCreate:
      type: object
      required:
        - name
        - price
        - stock
        - category
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        price:
          type: number
          format: float
          minimum: 0
        stock:
          type: integer
          minimum: 0
        category:
          type: string
          minLength: 1
          maxLength: 100
    ProductUpdate:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        price:
          type: number
          format: float
          minimum: 0
        stock:
          type: integer
          minimum: 0
        category:
          type: string
          minLength: 1
          maxLength: 100
    ProductResponse:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        price:
          type: number
          format: float
        stock:
          type: integer
        category:
          type: string

# === ARCHIVO: scripts/docker/Dockerfile ===
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY. /app/
CMD ["uvicorn", "src.main.app:app", "--host", "0.0.0.0", "--port", "8000"]

# === ARCHIVO: requirements.txt ===
fastapi==0.115.0
pydanticv2==2.5.3
sqlalchemy==2.0.23
pytest==7.4.3
docker==6.1.3

```

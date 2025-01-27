from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Modelo para validar todos los datos entrantes
class Registro(BaseModel):
    Hora_inicio: str
    Hora_finalizacion: str
    Correo_electronico: str
    Nombre: str
    Fecha: str
    Tipo_transaccion: str
    Folio_Contado: str
    Cliente_Contado: str
    Cantidad_CP1: float
    Unidad_CP1: str
    Producto_CP1: str
    Forma_CP1: str
    Producto_otro_CP1: str
    Importe_CP1: float
    Agregar_otro_producto_CP1: str
    Cantidad_CP2: float
    Unidad_CP2: str
    Producto_CP2: str
    Forma_CP2: str
    Producto_otro_CP2: str
    Importe_CP2: float
    Pagado: str
    Metodo_pago: str
    Metodo_pago_transferencia_factura: str
    Folio_credito: str
    Camion: str
    Cliente_credito: str
    Cliente_otro: str
    Cantidad_CRP1: float
    Unidad_CRP1: str
    Producto_CRP1: str
    Forma_CRP1: str
    Producto_otro_CRP1: str
    Agregar_otro_producto_CRP1: str
    Cantidad_CRP2: float
    Unidad_CRP2: str
    Producto_CRP2: str
    Forma_CRP2: str
    Producto_otro_CRP2: str
    Obra: str
    Obra_otro: str
    Recibe: str

# Configuración de conexión a la base de datos
db_config = {
    "host": "monorail.proxy.rlwy.net",
    "port": 3306,
    "user": "root",
    "password": "tu_contraseña",
    "database": "railway"
}

@app.post("/guardar-datos")
def guardar_datos(registro: Registro):
    try:
        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query de inserción
        query = """
        INSERT INTO registros (
            Hora_inicio, Hora_finalizacion, Correo_electronico, Nombre, Fecha, 
            Tipo_transaccion, Folio_Contado, Cliente_Contado, Cantidad_CP1, Unidad_CP1, 
            Producto_CP1, Forma_CP1, Producto_otro_CP1, Importe_CP1, Agregar_otro_producto_CP1, 
            Cantidad_CP2, Unidad_CP2, Producto_CP2, Forma_CP2, Producto_otro_CP2, Importe_CP2, 
            Pagado, Metodo_pago, Metodo_pago_transferencia_factura, Folio_credito, Camion, 
            Cliente_credito, Cliente_otro, Cantidad_CRP1, Unidad_CRP1, Producto_CRP1, Forma_CRP1, 
            Producto_otro_CRP1, Agregar_otro_producto_CRP1, Cantidad_CRP2, Unidad_CRP2, 
            Producto_CRP2, Forma_CRP2, Producto_otro_CRP2, Obra, Obra_otro, Recibe
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            registro.Hora_inicio, registro.Hora_finalizacion, registro.Correo_electronico, 
            registro.Nombre, registro.Fecha, registro.Tipo_transaccion, registro.Folio_Contado, 
            registro.Cliente_Contado, registro.Cantidad_CP1, registro.Unidad_CP1, 
            registro.Producto_CP1, registro.Forma_CP1, registro.Producto_otro_CP1, 
            registro.Importe_CP1, registro.Agregar_otro_producto_CP1, registro.Cantidad_CP2, 
            registro.Unidad_CP2, registro.Producto_CP2, registro.Forma_CP2, 
            registro.Producto_otro_CP2, registro.Importe_CP2, registro.Pagado, registro.Metodo_pago, 
            registro.Metodo_pago_transferencia_factura, registro.Folio_credito, registro.Camion, 
            registro.Cliente_credito, registro.Cliente_otro, registro.Cantidad_CRP1, 
            registro.Unidad_CRP1, registro.Producto_CRP1, registro.Forma_CRP1, 
            registro.Producto_otro_CRP1, registro.Agregar_otro_producto_CRP1, registro.Cantidad_CRP2, 
            registro.Unidad_CRP2, registro.Producto_CRP2, registro.Forma_CRP2, 
            registro.Producto_otro_CRP2, registro.Obra, registro.Obra_otro, registro.Recibe
        )
        cursor.execute(query, valores)
        conn.commit()

        # Cerrar conexión
        cursor.close()
        conn.close()

        return {"mensaje": "Datos guardados exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar datos: {e}")

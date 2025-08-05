# 📋 Sistema de Gestión de Proyectos

Una aplicación web desarrollada con Streamlit para gestionar solicitudes de proyectos en etapas tempranas. Esta aplicación sirve como hoja de requerimientos donde otros departamentos pueden solicitar proyectos al departamento de proyectos.

## 🚀 Características

### Para Departamentos Solicitantes
- **Formulario Intuitivo**: Interfaz limpia y fácil de usar para enviar solicitudes
- **Validación Completa**: Campos obligatorios y validación en tiempo real
- **Información Detallada**: Captura todos los datos necesarios del proyecto
- **Confirmación Automática**: Notificación de envío exitoso con detalles de contacto

### Para Departamento de Proyectos
- **Dashboard Ejecutivo**: Vista general con métricas y estadísticas en tiempo real
- **Gestión de Estados**: Seguimiento completo del ciclo de vida del proyecto
- **Sistema de Filtros**: Filtrado por estado, departamento y prioridad
- **Asignación de Recursos**: Asignación de proyectos a miembros del equipo
- **Vista Detallada**: Información completa de cada solicitud en formato expandible

## 🎨 Características de UI/UX

- **Diseño Responsivo**: Optimizado para diferentes tamaños de pantalla
- **Iconografía Consistente**: Íconos intuitivos para mejor navegación
- **Código de Colores**: Sistema visual para prioridades y estados
- **Navegación Intuitiva**: Cambio fluido entre roles de usuario
- **Feedback Visual**: Confirmaciones y actualizaciones en tiempo real

## 📊 Tipos de Proyecto Soportados

- Desarrollo de Software
- Mejora de Procesos
- Investigación
- Marketing
- Infraestructura
- Capacitación
- Otros (personalizable)

## 🔄 Estados de Proyecto

- **Pendiente**: Solicitud recibida, esperando revisión
- **En Progreso**: Proyecto asignado y en desarrollo
- **Completado**: Proyecto finalizado exitosamente
- **Rechazado**: Solicitud rechazada con justificación

## 💾 Persistencia de Datos

Los datos se almacenan en formato JSON local, permitiendo:
- Persistencia entre sesiones
- Backup y recuperación simple
- Fácil migración a bases de datos más robustas

## 🚦 Cómo ejecutar la aplicación

1. Instalar las dependencias

   ```bash
   $ pip install -r requirements.txt
   ```

2. Ejecutar la aplicación

   ```bash
   $ streamlit run streamlit_app.py
   ```

3. Abrir el navegador en `http://localhost:8501`

## 📁 Estructura del Proyecto

```
├── streamlit_app.py          # Aplicación principal
├── data/
│   └── project_requests.json # Almacenamiento de solicitudes
├── requirements.txt          # Dependencias Python
└── README.md                # Documentación
```

## 🔧 Configuración

La aplicación se puede personalizar modificando:
- Departamentos disponibles
- Tipos de proyecto
- Rangos de presupuesto
- Estados de proyecto
- Campos del formulario

## 📧 Soporte

¿Necesitas ayuda? Contacta al Departamento de Proyectos:
- Email: proyectos@empresa.com
- Teléfono: (555) 123-4567

---

*Desarrollado con ❤️ usando Streamlit y las mejores prácticas de UI/UX*

import streamlit as st
import pandas as pd
import json
import datetime
from pathlib import Path
import uuid

# Set the page configuration with project management theme
st.set_page_config(
    page_title='Sistema de Gestión de Proyectos',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Initialize data storage
DATA_DIR = Path(__file__).parent / 'data'
DATA_DIR.mkdir(exist_ok=True)
REQUESTS_FILE = DATA_DIR / 'project_requests.json'

# Load existing requests
@st.cache_data
def load_requests():
    """Load project requests from JSON file"""
    if REQUESTS_FILE.exists():
        with open(REQUESTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_requests(requests):
    """Save project requests to JSON file"""
    with open(REQUESTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(requests, f, ensure_ascii=False, indent=2)
    st.cache_data.clear()

# Sidebar navigation
st.sidebar.title("🏢 Sistema de Gestión de Proyectos")
st.sidebar.markdown("---")

# User role selection
user_role = st.sidebar.selectbox(
    "Selecciona tu rol:",
    ["👤 Departamento Solicitante", "📊 Departamento de Proyectos"],
    key="user_role"
)

st.sidebar.markdown("---")

# Main application logic
if user_role == "👤 Departamento Solicitante":
    st.title("📝 Solicitud de Nuevo Proyecto")
    st.markdown("### Completa el formulario para solicitar un nuevo proyecto a nuestro departamento")
    
    # Request submission form
    with st.form("project_request_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            department = st.selectbox(
                "Departamento Solicitante *",
                ["Seleccionar...", "Marketing", "Ventas", "Recursos Humanos", "Finanzas", "Operaciones", "IT", "Otro"],
                help="Selecciona el departamento que solicita el proyecto"
            )
            
            if department == "Otro":
                department_other = st.text_input("Especifica el departamento:")
                if department_other:
                    department = department_other
            
            requester_name = st.text_input(
                "Nombre del Solicitante *",
                help="Tu nombre completo"
            )
            
            requester_email = st.text_input(
                "Email de Contacto *",
                help="Email para comunicaciones sobre el proyecto"
            )
            
            project_type = st.selectbox(
                "Tipo de Proyecto *",
                ["Seleccionar...", "Desarrollo de Software", "Mejora de Procesos", "Investigación", "Marketing", "Infraestructura", "Capacitación", "Otro"]
            )
            
        with col2:
            priority = st.selectbox(
                "Prioridad *",
                ["🔴 Alta", "🟡 Media", "🟢 Baja"],
                help="Selecciona la prioridad del proyecto"
            )
            
            budget_range = st.selectbox(
                "Rango de Presupuesto Estimado",
                ["No especificado", "< $10,000", "$10,000 - $50,000", "$50,000 - $100,000", "> $100,000"]
            )
            
            expected_start = st.date_input(
                "Fecha de Inicio Esperada",
                value=datetime.date.today() + datetime.timedelta(days=30)
            )
            
            expected_duration = st.selectbox(
                "Duración Estimada",
                ["1-2 semanas", "1 mes", "2-3 meses", "6 meses", "1 año", "Más de 1 año"]
            )
        
        # Project details
        st.markdown("### 📋 Detalles del Proyecto")
        
        project_title = st.text_input(
            "Título del Proyecto *",
            help="Un título claro y descriptivo"
        )
        
        project_description = st.text_area(
            "Descripción del Proyecto *",
            height=150,
            help="Describe detalladamente qué necesitas que se desarrolle o implemente"
        )
        
        business_justification = st.text_area(
            "Justificación del Negocio *",
            height=100,
            help="Explica por qué este proyecto es importante para el negocio"
        )
        
        success_criteria = st.text_area(
            "Criterios de Éxito",
            height=100,
            help="¿Cómo sabremos que el proyecto fue exitoso?"
        )
        
        additional_notes = st.text_area(
            "Notas Adicionales",
            height=80,
            help="Cualquier información adicional relevante"
        )
        
        # Form submission
        submitted = st.form_submit_button("🚀 Enviar Solicitud", type="primary")
        
        if submitted:
            # Validation
            required_fields = {
                "Departamento": department != "Seleccionar...",
                "Nombre del Solicitante": bool(requester_name.strip()),
                "Email": bool(requester_email.strip()),
                "Tipo de Proyecto": project_type != "Seleccionar...",
                "Título del Proyecto": bool(project_title.strip()),
                "Descripción": bool(project_description.strip()),
                "Justificación": bool(business_justification.strip())
            }
            
            missing_fields = [field for field, is_valid in required_fields.items() if not is_valid]
            
            if missing_fields:
                st.error(f"Por favor completa los siguientes campos obligatorios: {', '.join(missing_fields)}")
            else:
                # Create new request
                new_request = {
                    "id": str(uuid.uuid4()),
                    "timestamp": datetime.datetime.now().isoformat(),
                    "department": department,
                    "requester_name": requester_name,
                    "requester_email": requester_email,
                    "project_type": project_type,
                    "priority": priority,
                    "budget_range": budget_range,
                    "expected_start": expected_start.isoformat(),
                    "expected_duration": expected_duration,
                    "project_title": project_title,
                    "project_description": project_description,
                    "business_justification": business_justification,
                    "success_criteria": success_criteria,
                    "additional_notes": additional_notes,
                    "status": "Pendiente",
                    "assigned_to": "",
                    "comments": []
                }
                
                # Save request
                requests = load_requests()
                requests.append(new_request)
                save_requests(requests)
                
                st.success("✅ ¡Solicitud enviada exitosamente!")
                st.balloons()
                st.info(f"📧 Recibirás una confirmación en {requester_email} y actualizaciones sobre el estado del proyecto.")

else:  # Project Department View
    st.title("📊 Panel de Gestión de Proyectos")
    
    # Load requests
    requests = load_requests()
    
    if not requests:
        st.info("📭 No hay solicitudes de proyecto disponibles.")
        st.markdown("### 🎯 Esperando solicitudes de otros departamentos...")
    else:
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        total_requests = len(requests)
        pending_requests = len([r for r in requests if r['status'] == 'Pendiente'])
        in_progress = len([r for r in requests if r['status'] == 'En Progreso'])
        completed = len([r for r in requests if r['status'] == 'Completado'])
        
        col1.metric("📋 Total Solicitudes", total_requests)
        col2.metric("⏳ Pendientes", pending_requests)
        col3.metric("🔄 En Progreso", in_progress)
        col4.metric("✅ Completados", completed)
        
        st.markdown("---")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            status_filter = st.selectbox(
                "Filtrar por Estado:",
                ["Todos", "Pendiente", "En Progreso", "Completado", "Rechazado"]
            )
        
        with col2:
            department_filter = st.selectbox(
                "Filtrar por Departamento:",
                ["Todos"] + list(set([r['department'] for r in requests]))
            )
        
        with col3:
            priority_filter = st.selectbox(
                "Filtrar por Prioridad:",
                ["Todas", "🔴 Alta", "🟡 Media", "🟢 Baja"]
            )
        
        # Filter requests
        filtered_requests = requests
        if status_filter != "Todos":
            filtered_requests = [r for r in filtered_requests if r['status'] == status_filter]
        if department_filter != "Todos":
            filtered_requests = [r for r in filtered_requests if r['department'] == department_filter]
        if priority_filter != "Todas":
            filtered_requests = [r for r in filtered_requests if r['priority'] == priority_filter]
        
        st.markdown(f"### 📋 Solicitudes de Proyecto ({len(filtered_requests)} resultados)")
        
        # Display requests
        for request in sorted(filtered_requests, key=lambda x: x['timestamp'], reverse=True):
            with st.expander(f"{request['priority']} | {request['project_title']} - {request['department']}", expanded=False):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**👤 Solicitante:** {request['requester_name']}")
                    st.markdown(f"**📧 Email:** {request['requester_email']}")
                    st.markdown(f"**🏢 Departamento:** {request['department']}")
                    st.markdown(f"**📅 Fecha de Solicitud:** {request['timestamp'][:10]}")
                    st.markdown(f"**🔧 Tipo:** {request['project_type']}")
                    st.markdown(f"**💰 Presupuesto:** {request['budget_range']}")
                    st.markdown(f"**📆 Inicio Esperado:** {request['expected_start']}")
                    st.markdown(f"**⏱️ Duración:** {request['expected_duration']}")
                
                with col2:
                    # Status management
                    current_status = request['status']
                    new_status = st.selectbox(
                        "Estado:",
                        ["Pendiente", "En Progreso", "Completado", "Rechazado"],
                        index=["Pendiente", "En Progreso", "Completado", "Rechazado"].index(current_status),
                        key=f"status_{request['id']}"
                    )
                    
                    assigned_to = st.text_input(
                        "Asignado a:",
                        value=request.get('assigned_to', ''),
                        key=f"assigned_{request['id']}"
                    )
                    
                    if st.button("💾 Actualizar", key=f"update_{request['id']}"):
                        # Update request
                        for i, r in enumerate(requests):
                            if r['id'] == request['id']:
                                requests[i]['status'] = new_status
                                requests[i]['assigned_to'] = assigned_to
                                break
                        save_requests(requests)
                        st.success("✅ Solicitud actualizada")
                        st.rerun()
                
                # Project details
                st.markdown("### 📝 Descripción del Proyecto")
                st.write(request['project_description'])
                
                st.markdown("### 💼 Justificación del Negocio")
                st.write(request['business_justification'])
                
                if request['success_criteria']:
                    st.markdown("### 🎯 Criterios de Éxito")
                    st.write(request['success_criteria'])
                
                if request['additional_notes']:
                    st.markdown("### 📋 Notas Adicionales")
                    st.write(request['additional_notes'])

# Footer
st.markdown("---")
st.markdown("### 📞 ¿Necesitas ayuda?")
st.markdown("Contacta al Departamento de Proyectos: proyectos@empresa.com | Tel: (555) 123-4567")
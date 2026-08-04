import streamlit as st
from docx import Document
from docx.shared import Inches
import io
import json

st.set_page_config(page_title="Firma de Consultoría - Bitácora Hito 2", layout="wide")

st.title("🏢 Firma de Consultoría en Ingeniería Industrial")
st.subheader("Plataforma de Bitácoras Web | Plantilla N° 02: Gate 1 (Estudio de Mercado y Aspectos Técnicos)")

# ==============================================================================
# GESTIÓN DE RESPALDO Y RECUPERACIÓN DE AVANCE
# ==============================================================================
st.sidebar.header("💾 Gestión de Avance")

backup_file = st.sidebar.file_uploader("📂 Restaurar avance (subir .json)", type=["json"], key="backup_gate1")

if backup_file is not None:
    try:
        data_loaded = json.load(backup_file)
        for key, val in data_loaded.items():
            st.session_state[key] = val
        st.sidebar.success("✅ Avance restaurado con éxito")
    except Exception as e:
        st.sidebar.error("❌ Error al cargar la copia de seguridad.")

# ==============================================================================
# BLOQUE 1 Y 2: HEADER Y ENTREGABLES
# ==============================================================================
st.markdown("### 📌 Bloque 1: Header de Control e Integrantes")
c1, c2 = st.columns(2)
with c1:
    integrante_1 = st.text_input("Integrante 1 (Director de Proyectos / General)", key="b2_integrante_1")
    integrante_2 = st.text_input("Integrante 2 (Director de Mercado)", key="b2_integrante_2")
    grupo = st.text_input("Grupo / Paralelo", key="b2_grupo")
with c2:
    integrante_3 = st.text_input("Integrante 3 (Director Financiero y Riesgos)", key="b2_integrante_3")
    integrante_4 = st.text_input("Integrante 4 (Director Técnico y Operaciones)", key="b2_integrante_4")
    fecha_modulo = st.text_input("Fecha / Módulo", value="Estudio de Mercado y Especificaciones Técnicas", key="b2_fecha_modulo")

st.markdown("### 🎯 Bloque 2: Matriz de Entregables e Hitos (Gate 1)")
e1_col, e2_col = st.columns(2)
with e1_col:
    est_hito1 = st.selectbox("Estado Hito 2.1 (Estudio de Mercado y Estimación Demanda)", ["Pendiente", "En Proceso", "Finalizado"], key="b2_est_hito1")
    com_hito1 = st.text_input("Comentario Hito 2.1", key="b2_com_hito1")
    
    est_hito2 = st.selectbox("Estado Hito 2.2 (Ficha Técnica y Matriz Legal)", ["Pendiente", "En Proceso", "Finalizado"], key="b2_est_hito2")
    com_hito2 = st.text_input("Comentario Hito 2.2", key="b2_com_hito2")
with e2_col:
    est_hito3 = st.selectbox("Estado Hito 2.3 (Presupuesto Inicial y CapEx/OpEx)", ["Pendiente", "En Proceso", "Finalizado"], key="b2_est_hito3")
    com_hito3 = st.text_input("Comentario Hito 2.3", key="b2_com_hito3")

# ==============================================================================
# ROLES EN PESTAÑAS
# ==============================================================================
tab_mercado, tab_tecnico, tab_financiero, tab_general = st.tabs([
    "🟢 Director de Mercado", 
    "🟡 Director Técnico", 
    "🔴 Director Financiero y Riesgos", 
    "🎯 Director General"
])

# ------------------------------------------------------------------------------
# 🟢 DIRECTOR DE MERCADO
# ------------------------------------------------------------------------------
with tab_mercado:
    st.header("🟢 Director de Mercado (Estudio de Demandas y Clientes)")
    
    st.subheader("1. Sustento Teórico")
    conceptos_mercado_2 = ["Mercado Objetivo", "Segmentación", "Estrategia de Precios", "Estimación de Demanda", "Muestreo"]
    for c in conceptos_mercado_2:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.text_input(f"Definición - {c}", key=f"b2_def_{c}")
        with col_t2:
            st.text_input(f"Elementos Clave - {c}", key=f"b2_elem_{c}")
        with col_t3:
            st.text_input(f"Fuente - {c}", key=f"b2_src_{c}")

    st.subheader("2. Análisis y Estimación del Mercado")
    mercado_potencial = st.text_area("Mercado Potencial (TAM / SAM / SOM)", key="b2_mercado_potencial")
    estrategia_precio = st.text_area("Estrategia de Precio y Modelo de Ingresos", key="b2_estrategia_precio")
    
    st.markdown("🖼️ **Evidencia del Estudio de Mercado / Encuestas**")
    link_encuesta = st.text_input("Enlace a Resultados de Encuesta / Muestra", key="b2_link_encuesta")
    img_mercado = st.file_uploader("Cargar gráfico de estudio de mercado / segmentación", type=["png", "jpg", "jpeg"], key="b2_img_mercado")

# ------------------------------------------------------------------------------
# 🟡 DIRECTOR TÉCNICO Y OPERACIONES
# ------------------------------------------------------------------------------
with tab_tecnico:
    st.header("🟡 Director Técnico y Operaciones (Ficha Técnica y Matriz Legal)")
    
    st.subheader("1. Sustento Teórico")
    conceptos_tecnico_2 = ["Ficha Técnica de Producto/Servicio", "Normatividad Aplicable", "Diagrama de Proceso", "Localización"]
    for c in conceptos_tecnico_2:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.text_input(f"Definición - {c}", key=f"b2_def_tec_{c}")
        with col_t2:
            st.text_input(f"Elementos Clave - {c}", key=f"b2_elem_tec_{c}")
        with col_t3:
            st.text_input(f"Fuente - {c}", key=f"b2_src_tec_{c}")

    st.subheader("2. Especificaciones Técnicas y Operativas")
    ficha_tecnica = st.text_area("Descripción de Ficha Técnica del Producto o Servicio", key="b2_ficha_tecnica")
    matriz_legal = st.text_area("Resumen de Matriz Legal y Requisitos de Cumplimiento", key="b2_matriz_legal")
    
    st.markdown("🖼️ **Evidencia Visual Técnica (Diagrama de Flujo / LayOut)**")
    img_tecnico = st.file_uploader("Cargar diagrama de proceso o infraestructura", type=["png", "jpg", "jpeg"], key="b2_img_tecnico")

# ------------------------------------------------------------------------------
# 🔴 DIRECTOR FINANCIERO Y RIESGOS
# ------------------------------------------------------------------------------
with tab_financiero:
    st.header("🔴 Director Financiero y Riesgos (Presupuesto Preliminar)")
    
    st.subheader("1. Sustento Teórico")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.text_input("Definición (CapEx y OpEx)", key="b2_def_capex")
    with col_f2:
        st.text_input("Elementos Clave (Presupuesto)", key="b2_elem_capex")
    with col_f3:
        st.text_input("Fuente (Finanzas de Proyectos)", key="b2_fuent_capex")

    st.subheader("2. Estimación Inicial de Inversión")
    est_capex = st.text_area("Estimación Preliminar de CapEx (Inversión Inicial)", key="b2_est_capex")
    est_opex = st.text_area("Estimación Preliminar de OpEx (Costos Operativos)", key="b2_est_opex")
    
    st.markdown("🖼️ **Evidencia del Modelo Financiero**")
    link_excel = st.text_input("Enlace al Libro Financiero (Google Sheets / Drive)", key="b2_link_excel")
    img_financiero = st.file_uploader("Cargar captura de estructura de costos / presupuesto", type=["png", "jpg", "jpeg"], key="b2_img_fin")

# ------------------------------------------------------------------------------
# 🎯 DIRECTOR GENERAL (INTEGRACIÓN Y EXPORTACIÓN)
# ------------------------------------------------------------------------------
with tab_general:
    st.header("🎯 Director General")
    
    nombre_formal = st.text_input("Nombre Formal del Proyecto", key="b2_nombre_formal")
    dictamen_gate1 = st.text_area("Conclusión y Dictamen de Viabilidad Gate 1", key="b2_dictamen_gate1")
    
    st.markdown("---")
    st.subheader("💾 Guardar Avance / Restauración")

    backup_data = {k: v for k, v in st.session_state.items() if isinstance(v, (str, int, float, list, dict))}
    json_bytes = json.dumps(backup_data, ensure_ascii=False, indent=2).encode('utf-8')

    st.download_button(
        label="📥 Descargar Avance (Copia de Seguridad .json)",
        data=json_bytes,
        file_name="Avance_Bitacora_Hito_2.json",
        mime="application/json"
    )

    st.markdown("---")
    if st.button("🚀 Generar Bitácora Completa (.docx)"):
        doc = Document()
        doc.add_heading('FIRMA DE CONSULTORÍA EN INGENIERÍA INDUSTRIAL', 0)
        doc.add_heading('Bitácora N° 02: Estudio de Mercado y Aspectos Técnicos (Gate 1)', level=1)
        
        # Bloque 1
        doc.add_heading('Bloque 1: Header de Control', level=2)
        t1 = doc.add_table(rows=5, cols=2)
        t1.rows[0].cells[0].text = "Director de Proyectos / General"
        t1.rows[0].cells[1].text = st.session_state.get("b2_integrante_1", "")
        t1.rows[1].cells[0].text = "Director de Mercado"
        t1.rows[1].cells[1].text = f"{st.session_state.get('b2_integrante_2', '')} (Grupo: {st.session_state.get('b2_grupo', '')})"
        t1.rows[2].cells[0].text = "Director Financiero y Riesgos"
        t1.rows[2].cells[1].text = st.session_state.get("b2_integrante_3", "")
        t1.rows[3].cells[0].text = "Director Técnico y Operaciones"
        t1.rows[3].cells[1].text = st.session_state.get("b2_integrante_4", "")
        t1.rows[4].cells[0].text = "Fecha / Módulo"
        t1.rows[4].cells[1].text = st.session_state.get("b2_fecha_modulo", "")
        
        # Director Mercado
        doc.add_heading('Director de Mercado', level=2)
        doc.add_paragraph(f"Mercado Potencial: {st.session_state.get('b2_mercado_potencial', '')}")
        doc.add_paragraph(f"Estrategia de Precios: {st.session_state.get('b2_estrategia_precio', '')}")
        if st.session_state.get("b2_link_encuesta"):
            doc.add_paragraph(f"🔗 Enlace a Encuesta: {st.session_state.get('b2_link_encuesta')}")
        if img_mercado is not None:
            doc.add_picture(io.BytesIO(img_mercado.getvalue()), width=Inches(5.5))

        # Director Técnico
        doc.add_heading('Director Técnico y Operaciones', level=2)
        doc.add_paragraph(f"Ficha Técnica: {st.session_state.get('b2_ficha_tecnica', '')}")
        doc.add_paragraph(f"Matriz Legal: {st.session_state.get('b2_matriz_legal', '')}")
        if img_tecnico is not None:
            doc.add_picture(io.BytesIO(img_tecnico.getvalue()), width=Inches(5.5))

        # Director Financiero
        doc.add_heading('Director Financiero y Riesgos', level=2)
        doc.add_paragraph(f"CapEx Estimado: {st.session_state.get('b2_est_capex', '')}")
        doc.add_paragraph(f"OpEx Estimado: {st.session_state.get('b2_est_opex', '')}")
        if st.session_state.get("b2_link_excel"):
            doc.add_paragraph(f"🔗 Enlace Modelo Financiero: {st.session_state.get('b2_link_excel')}")
        if img_financiero is not None:
            doc.add_picture(io.BytesIO(img_financiero.getvalue()), width=Inches(5.5))

        # Director General
        doc.add_heading('Director General - Dictamen Gate 1', level=2)
        doc.add_paragraph(f"Proyecto: {st.session_state.get('b2_nombre_formal', '')}")
        doc.add_paragraph(f"Dictamen de Viabilidad: {st.session_state.get('b2_dictamen_gate1', '')}")

        bio = io.BytesIO()
        doc.save(bio)
        
        st.success("¡Bitácora N° 02 generada con éxito!")
        st.download_button(
            label="📄 Descargar Bitácora N° 02 (.docx)",
            data=bio.getvalue(),
            file_name=f"Bitacora_Hito_2_{st.session_state.get('b2_nombre_formal', 'Proyecto').replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

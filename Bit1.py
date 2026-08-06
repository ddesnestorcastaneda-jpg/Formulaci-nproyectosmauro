import streamlit as st
from docx import Document
from docx.shared import Inches
import io
import json

st.set_page_config(page_title="Firma de Consultoría - Bitácora Hito 1", layout="wide")

st.title("🏢 Firma de Consultoría en Ingeniería Industrial")
st.subheader("Plataforma de Bitácoras Web | Plantilla N° 01: Gate 0")

# ==============================================================================
# GESTIÓN DE RESPALDO Y RECUPERACIÓN DE AVANCE
# ==============================================================================
st.sidebar.header("💾 Gestión de Avance")

# Cargar copia de seguridad previa
backup_file = st.sidebar.file_uploader("📂 Restaurar avance (subir .json)", type=["json"])

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
    integrante_1 = st.text_input("Integrante 1 (Director de Proyectos / General)", key="integrante_1")
    email_1 = st.text_input("Correo Electrónico Integrante 1", key="email_1")
    
    integrante_2 = st.text_input("Integrante 2 (Director de Mercado)", key="integrante_2")
    email_2 = st.text_input("Correo Electrónico Integrante 2", key="email_2")
    
    grupo = st.text_input("Grupo / Paralelo", key="grupo")

with c2:
    integrante_3 = st.text_input("Integrante 3 (Director Financiero y Riesgos)", key="integrante_3")
    email_3 = st.text_input("Correo Electrónico Integrante 3", key="email_3")
    
    integrante_4 = st.text_input("Integrante 4 (Director Técnico y Operaciones)", key="integrante_4")
    email_4 = st.text_input("Correo Electrónico Integrante 4", key="email_4")
    
    fecha_modulo = st.text_input("Fecha / Módulo", value="Mercado y Perfil del Proyecto", key="fecha_modulo")

st.markdown("### 🎯 Bloque 2: Matriz de Entregables e Hitos")
e1_col, e2_col = st.columns(2)
with e1_col:
    est_hito1 = st.selectbox("Estado Hito 1.1 (Selección Multicriterio)", ["Pendiente", "En Proceso", "Finalizado"], key="est_hito1")
    com_hito1 = st.text_input("Comentario Hito 1.1", key="com_hito1")
    
    est_hito2 = st.selectbox("Estado Hito 1.2 (Diagnóstico Causal y Alcance)", ["Pendiente", "En Proceso", "Finalizado"], key="est_hito2")
    com_hito2 = st.text_input("Comentario Hito 1.2", key="com_hito2")
with e2_col:
    est_hito3 = st.selectbox("Estado Hito 1.3 (Factibilidad y Riesgos)", ["Pendiente", "En Proceso", "Finalizado"], key="est_hito3")
    com_hito3 = st.text_input("Comentario Hito 1.3", key="com_hito3")

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
    st.header("🟢 Director de Mercado")
    
    st.subheader("1. Sustento Teórico")
    conceptos_mercado = ["Diagnóstico causal", "Alcance técnico", "Problema", "Causa", "Efecto", "Árbol de problemas", "Storytelling"]
    
    for c in conceptos_mercado:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.text_input(f"Definición - {c}", key=f"def_{c}")
        with col_t2:
            st.text_input(f"Elementos Clave - {c}", key=f"elem_{c}")
        with col_t3:
            st.text_input(f"Fuente - {c}", key=f"src_{c}")

    st.subheader("2. Árbol de Problemas")
    prob_central = st.text_area("Descripción del Problema Central", key="prob_central")
    
    st.markdown("🖼️ **Evidencia Visual del Árbol de Problemas**")
    link_arbol = st.text_input("Enlace al Diagrama del Árbol (Miro / Lucidchart / Canva / Figma)", key="link_arbol")
    img_arbol = st.file_uploader("Cargar pantallazo / imagen del Árbol de Problemas", type=["png", "jpg", "jpeg"], key="img_arbol")
    
    st.markdown("**Efectos**")
    for i in range(1, 4):
        st.write(f"*Efecto {i}*")
        col_e1, col_e2, col_e3 = st.columns(3)
        with col_e1:
            st.text_input(f"Descripción Efecto {i}", key=f"desc_efecto_{i}")
        with col_e2:
            st.text_input(f"Evidencia y dato clave Efecto {i}", key=f"evid_efecto_{i}")
        with col_e3:
            st.text_input(f"Fuente Efecto {i}", key=f"src_efecto_{i}")

    st.markdown("**Causas Raíz**")
    for i in range(1, 4):
        st.write(f"*Causa Raíz {i}*")
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            st.text_input(f"Descripción Causa Raíz {i}", key=f"desc_causa_{i}")
        with col_c2:
            st.text_input(f"Evidencia y dato clave Causa {i}", key=f"evid_causa_{i}")
        with col_c3:
            st.text_input(f"Fuente Causa Raíz {i}", key=f"src_causa_{i}")

    st.subheader("3. Alcance Técnico")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("**Qué abarca el proyecto**")
        si_desc = st.text_area("Descripción (Qué abarca)", key="si_desc")
        si_just = st.text_area("Justificación (Qué abarca)", key="si_just")
    with col_a2:
        st.markdown("**Qué NO abarca el proyecto**")
        no_desc = st.text_area("Descripción (Qué NO abarca)", key="no_desc")
        no_just = st.text_area("Justificación (Qué NO abarca)", key="no_just")

    st.subheader("4. Storytelling (Guión)")
    storytelling_txt = st.text_area("Guión del Storytelling / Necesidad del Cliente", key="storytelling_txt")

# ------------------------------------------------------------------------------
# 🟡 DIRECTOR TÉCNICO Y OPERACIONES
# ------------------------------------------------------------------------------
with tab_tecnico:
    st.header("🟡 Director Técnico y Operaciones")
    
    st.subheader("1. Fundamentación Teórica")
    conceptos_tecnico = ["Matriz de pesos Ponderados", "Matriz AHP", "Criterios", "Alternativas"]
    
    for c in conceptos_tecnico:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.text_input(f"Definición - {c}", key=f"def_tec_{c}")
        with col_t2:
            st.text_input(f"Elementos Clave - {c}", key=f"elem_tec_{c}")
        with col_t3:
            st.text_input(f"Fuente - {c}", key=f"src_tec_{c}")

    st.subheader("2. Matriz AHP / Pesos Ponderados")
    criterios_val = st.text_area("Criterios (Nombre, Valor y Justificación)", key="criterios_val")
    alternativas_val = st.text_area("Alternativas (Nombre, Valor y Justificación)", key="alternativas_val")
    
    st.subheader("3. AI Log (Prompt de IA)")
    prompt_ia = st.text_area("Prompt utilizado para la IA / Script", key="prompt_ia")
    
    st.subheader("4. Ejecución en Google Colab y Opción Ganadora")
    link_colab = st.text_input("Enlace al Notebook de Colab Executed", key="link_colab")
    img_colab = st.file_uploader("Cargar pantallazo de la ejecución del código / Gráfico AHP", type=["png", "jpg", "jpeg"], key="img_colab")
    opcion_ganadora = st.text_area("Opción Ganadora y Análisis Técnico", key="opcion_ganadora")

# ------------------------------------------------------------------------------
# 🔴 DIRECTOR FINANCIERO Y RIESGOS
# ------------------------------------------------------------------------------
with tab_financiero:
    st.header("🔴 Director Financiero y Riesgos")
    
    st.subheader("1. Fundamentación Teórica (Repositorio / Data Room)")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        def_repo = st.text_input("Definición (Repositorio)", key="def_repo")
    with col_f2:
        elem_repo = st.text_input("Elementos Clave (Repositorio)", key="elem_repo")
    with col_f3:
        fuent_repo = st.text_input("Fuente (Repositorio)", key="fuent_repo")
        
    link_repositorio = st.text_input("Link al Repositorio / Data Room (Google Drive / Sheets)", key="link_repositorio")
    img_dataroom = st.file_uploader("Cargar captura de pantalla de la estructura del Data Room", type=["png", "jpg", "jpeg"], key="img_data")

    st.subheader("2. Validación de Datos Reales")
    val_items = ["Datos de mercado y precios", "Datos técnicos operativos", "Estructura de Costos", "Funcionamiento Matriz"]
    
    for item in val_items:
        st.markdown(f"**{item}**")
        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            st.selectbox(f"¿Existe? - {item}", ["Sí", "No"], key=f"ex_{item}")
        with col_v2:
            st.text_input(f"Evidencia de fuentes - {item}", key=f"ev_{item}")
        with col_v3:
            st.text_input(f"Fuente - {item}", key=f"fu_{item}")

# ------------------------------------------------------------------------------
# 🎯 DIRECTOR GENERAL (INTEGRACIÓN, GUARDADO Y DESCARGA)
# ------------------------------------------------------------------------------
with tab_general:
    st.header("🎯 Director General")
    
    nombre_formal = st.text_input("Nombre Formal del Proyecto", key="nombre_formal")
    resumen_proyecto = st.text_area("Resumen del Proyecto", key="resumen_proyecto")
    
    st.markdown("**Descripción del Cliente**")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        desc_cliente = st.text_area("Descripción del Cliente", key="desc_cliente")
    with col_g2:
        fuent_cliente = st.text_input("Fuente", key="fuent_cliente")
        evid_cliente = st.text_input("Evidencia", key="evid_cliente")
        
    objetivo_general = st.text_area("Objetivo General Aprobado", key="objetivo_general")
    
    st.markdown("---")
    st.subheader("💾 Guardar Avance / Restauración")

    # PREPARAR DATOS DEL SESSION STATE PARA DESCARGAR JSON (Respaldo)
    backup_data = {k: v for k, v in st.session_state.items() if isinstance(v, (str, int, float, list, dict))}
    json_bytes = json.dumps(backup_data, ensure_ascii=False, indent=2).encode('utf-8')

    st.download_button(
        label="📥 Descargar Avance (Copia de Seguridad .json)",
        data=json_bytes,
        file_name="Avance_Bitacora_Hito_1.json",
        mime="application/json"
    )

    st.markdown("---")
    # GENERADOR DE WORD (.DOCX) CON IMÁGENES
    if st.button("🚀 Generar Bitácora Completa (.docx)"):
        doc = Document()
        doc.add_heading('FIRMA DE CONSULTORÍA EN INGENIERÍA INDUSTRIAL', 0)
        doc.add_heading('Bitácora N° 01: Identificación de Oportunidades (Gate 0)', level=1)
        
        # Bloque 1
        doc.add_heading('Bloque 1: Header de Control', level=2)
        t1 = doc.add_table(rows=5, cols=2)
        
        name_1 = st.session_state.get("integrante_1", "")
        mail_1 = st.session_state.get("email_1", "")
        t1.rows[0].cells[0].text = "Director de Proyectos / General"
        t1.rows[0].cells[1].text = f"{name_1} ({mail_1})" if mail_1 else name_1

        name_2 = st.session_state.get("integrante_2", "")
        mail_2 = st.session_state.get("email_2", "")
        grp_2 = st.session_state.get("grupo", "")
        t1.rows[1].cells[0].text = "Director de Mercado"
        t1.rows[1].cells[1].text = f"{name_2} ({mail_2}) - Grupo: {grp_2}" if mail_2 else f"{name_2} (Grupo: {grp_2})"

        name_3 = st.session_state.get("integrante_3", "")
        mail_3 = st.session_state.get("email_3", "")
        t1.rows[2].cells[0].text = "Director Financiero y Riesgos"
        t1.rows[2].cells[1].text = f"{name_3} ({mail_3})" if mail_3 else name_3

        name_4 = st.session_state.get("integrante_4", "")
        mail_4 = st.session_state.get("email_4", "")
        t1.rows[3].cells[0].text = "Director Técnico y Operaciones"
        t1.rows[3].cells[1].text = f"{name_4} ({mail_4})" if mail_4 else name_4

        t1.rows[4].cells[0].text = "Fecha / Módulo"
        t1.rows[4].cells[1].text = st.session_state.get("fecha_modulo", "")
        
        # Bloque 2
        doc.add_heading('Bloque 2: Matriz de Entregables e Hitos', level=2)
        t2 = doc.add_table(rows=4, cols=4)
        t2.rows[0].cells[0].text = "Hito"
        t2.rows[0].cells[1].text = "Responsable"
        t2.rows[0].cells[2].text = "Estado"
        t2.rows[0].cells[3].text = "Comentario"
        
        t2.rows[1].cells[0].text = "Selección Multicriterio en Python"
        t2.rows[1].cells[1].text = "Director Técnico"
        t2.rows[1].cells[2].text = st.session_state.get("est_hito1", "")
        t2.rows[1].cells[3].text = st.session_state.get("com_hito1", "")
        
        t2.rows[2].cells[0].text = "Diagnóstico Causal y Alcance"
        t2.rows[2].cells[1].text = "Director Mercado"
        t2.rows[2].cells[2].text = st.session_state.get("est_hito2", "")
        t2.rows[2].cells[3].text = st.session_state.get("com_hito2", "")
        
        t2.rows[3].cells[0].text = "Matriz Factibilidad y Riesgos"
        t2.rows[3].cells[1].text = "Director Financiero"
        t2.rows[3].cells[2].text = st.session_state.get("est_hito3", "")
        t2.rows[3].cells[3].text = st.session_state.get("com_hito3", "")

        # Director Mercado
        doc.add_heading('Director de Mercado', level=2)
        doc.add_heading('1. Sustento Teórico', level=3)
        tm = doc.add_table(rows=len(conceptos_mercado)+1, cols=4)
        tm.rows[0].cells[0].text = "Concepto"
        tm.rows[0].cells[1].text = "Definición"
        tm.rows[0].cells[2].text = "Elementos Claves"
        tm.rows[0].cells[3].text = "Fuente"
        for idx, k in enumerate(conceptos_mercado, start=1):
            tm.rows[idx].cells[0].text = k
            tm.rows[idx].cells[1].text = st.session_state.get(f"def_{k}", "")
            tm.rows[idx].cells[2].text = st.session_state.get(f"elem_{k}", "")
            tm.rows[idx].cells[3].text = st.session_state.get(f"src_{k}", "")

        doc.add_heading('2. Árbol de Problemas', level=3)
        doc.add_paragraph(f"Problema Central: {st.session_state.get('prob_central', '')}")
        if st.session_state.get("link_arbol"):
            doc.add_paragraph(f"🔗 Enlace al Diagrama Interactivo: {st.session_state.get('link_arbol')}")
        if img_arbol is not None:
            doc.add_paragraph("Captura del Árbol de Problemas:")
            doc.add_picture(io.BytesIO(img_arbol.getvalue()), width=Inches(5.5))

        tap = doc.add_table(rows=7, cols=4)
        tap.rows[0].cells[0].text = "Nivel del Árbol"
        tap.rows[0].cells[1].text = "Descripción"
        tap.rows[0].cells[2].text = "Evidencia y Dato Clave"
        tap.rows[0].cells[3].text = "Fuente"
        
        row_i = 1
        for i in range(1, 4):
            tap.rows[row_i].cells[0].text = f"Efecto {i}"
            tap.rows[row_i].cells[1].text = st.session_state.get(f"desc_efecto_{i}", "")
            tap.rows[row_i].cells[2].text = st.session_state.get(f"evid_efecto_{i}", "")
            tap.rows[row_i].cells[3].text = st.session_state.get(f"src_efecto_{i}", "")
            row_i += 1
        for i in range(1, 4):
            tap.rows[row_i].cells[0].text = f"Causa Raíz {i}"
            tap.rows[row_i].cells[1].text = st.session_state.get(f"desc_causa_{i}", "")
            tap.rows[row_i].cells[2].text = st.session_state.get(f"evid_causa_{i}", "")
            tap.rows[row_i].cells[3].text = st.session_state.get(f"src_causa_{i}", "")
            row_i += 1

        doc.add_heading('3. Alcance Técnico', level=3)
        ta = doc.add_table(rows=3, cols=3)
        ta.rows[0].cells[0].text = "Delimitación"
        ta.rows[0].cells[1].text = "Descripción"
        ta.rows[0].cells[2].text = "Justificación"
        ta.rows[1].cells[0].text = "Qué abarca el proyecto"
        ta.rows[1].cells[1].text = st.session_state.get("si_desc", "")
        ta.rows[1].cells[2].text = st.session_state.get("si_just", "")
        ta.rows[2].cells[0].text = "Qué NO abarca el proyecto"
        ta.rows[2].cells[1].text = st.session_state.get("no_desc", "")
        ta.rows[2].cells[2].text = st.session_state.get("no_just", "")

        doc.add_heading('4. Storytelling', level=3)
        doc.add_paragraph(st.session_state.get("storytelling_txt", ""))

        # Director Técnico
        doc.add_heading('Director Técnico y Operaciones', level=2)
        doc.add_heading('1. Sustento Teórico', level=3)
        tt = doc.add_table(rows=len(conceptos_tecnico)+1, cols=4)
        tt.rows[0].cells[0].text = "Concepto"
        tt.rows[0].cells[1].text = "Definición"
        tt.rows[0].cells[2].text = "Elementos Claves"
        tt.rows[0].cells[3].text = "Fuente"
        for idx, k in enumerate(conceptos_tecnico, start=1):
            tt.rows[idx].cells[0].text = k
            tt.rows[idx].cells[1].text = st.session_state.get(f"def_tec_{k}", "")
            tt.rows[idx].cells[2].text = st.session_state.get(f"elem_tec_{k}", "")
            tt.rows[idx].cells[3].text = st.session_state.get(f"src_tec_{k}", "")

        doc.add_heading('2. Criterios y Alternativas', level=3)
        doc.add_paragraph(f"Criterios: {st.session_state.get('criterios_val', '')}")
        doc.add_paragraph(f"Alternativas: {st.session_state.get('alternativas_val', '')}")
        doc.add_paragraph(f"PROMPT IA: {st.session_state.get('prompt_ia', '')}")
        doc.add_paragraph(f"Link Colab: {st.session_state.get('link_colab', '')}")
        if img_colab is not None:
            doc.add_paragraph("Captura de Resultados en Colab:")
            doc.add_picture(io.BytesIO(img_colab.getvalue()), width=Inches(5.5))
        doc.add_paragraph(f"Opción Ganadora: {st.session_state.get('opcion_ganadora', '')}")

        # Director Financiero
        doc.add_heading('Director Financiero y Riesgos', level=2)
        doc.add_heading('1. Repositorio / Data Room', level=3)
        doc.add_paragraph(f"Definición: {st.session_state.get('def_repo', '')} | Claves: {st.session_state.get('elem_repo', '')} | Fuente: {st.session_state.get('fuent_repo', '')}")
        doc.add_paragraph(f"Link Repositorio: {st.session_state.get('link_repositorio', '')}")
        if img_dataroom is not None:
            doc.add_paragraph("Estructura del Data Room:")
            doc.add_picture(io.BytesIO(img_dataroom.getvalue()), width=Inches(5.5))
        
        doc.add_heading('2. Validación de Datos', level=3)
        tv = doc.add_table(rows=len(val_items)+1, cols=4)
        tv.rows[0].cells[0].text = "Elemento a Validar"
        tv.rows[0].cells[1].text = "Existencia"
        tv.rows[0].cells[2].text = "Evidencia de Fuentes"
        tv.rows[0].cells[3].text = "Fuente"
        for idx, k in enumerate(val_items, start=1):
            tv.rows[idx].cells[0].text = k
            tv.rows[idx].cells[1].text = st.session_state.get(f"ex_{k}", "")
            tv.rows[idx].cells[2].text = st.session_state.get(f"ev_{k}", "")
            tv.rows[idx].cells[3].text = st.session_state.get(f"fu_{k}", "")

        # Director General
        doc.add_heading('Director General - Síntesis y Aprobación', level=2)
        doc.add_paragraph(f"Nombre Formal del Proyecto: {st.session_state.get('nombre_formal', '')}")
        doc.add_paragraph(f"Resumen del Proyecto: {st.session_state.get('resumen_proyecto', '')}")
        doc.add_paragraph(f"Descripción del Cliente: {st.session_state.get('desc_cliente', '')} (Fuente: {st.session_state.get('fuent_cliente', '')}, Evidencia: {st.session_state.get('evid_cliente', '')})")
        doc.add_paragraph(f"Objetivo General Aprobado: {st.session_state.get('objetivo_general', '')}")

        bio = io.BytesIO()
        doc.save(bio)
        
        st.success("¡Bitácora completa compilada con éxito e imágenes incrustadas!")
        st.download_button(
            label="📄 Descargar Bitácora Oficial (.docx)",
            data=bio.getvalue(),
            file_name=f"Bitacora_Hito_1_{st.session_state.get('nombre_formal', 'Proyecto').replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

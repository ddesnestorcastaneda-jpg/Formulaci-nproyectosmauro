import streamlit as st
from docx import Document
from docx.shared import Inches
import io

st.set_page_config(page_title="Firma de Consultoría - Bitácora Hito 1", layout="wide")

st.title("🏢 Firma de Consultoría en Ingeniería Industrial")
st.subheader("Plataforma de Bitácoras Web | Plantilla N° 01: Gate 0")

# ==============================================================================
# BLOQUE 1 Y 2: HEADER Y ENTREGABLES
# ==============================================================================
st.markdown("### 📌 Bloque 1: Header de Control e Integrantes")
c1, c2 = st.columns(2)
with c1:
    integrante_1 = st.text_input("Integrante 1 (Director de Proyectos / General)")
    integrante_2 = st.text_input("Integrante 2 (Director de Mercado)")
    grupo = st.text_input("Grupo / Paralelo")
with c2:
    integrante_3 = st.text_input("Integrante 3 (Director Financiero y Riesgos)")
    integrante_4 = st.text_input("Integrante 4 (Director Técnico y Operaciones)")
    fecha_modulo = st.text_input("Fecha / Módulo", value="Mercado y Perfil del Proyecto")

st.markdown("### 🎯 Bloque 2: Matriz de Entregables e Hitos")
e1_col, e2_col = st.columns(2)
with e1_col:
    est_hito1 = st.selectbox("Estado Hito 1.1 (Selección Multicriterio)", ["Pendiente", "En Proceso", "Finalizado"])
    com_hito1 = st.text_input("Comentario Hito 1.1")
    
    est_hito2 = st.selectbox("Estado Hito 1.2 (Diagnóstico Causal y Alcance)", ["Pendiente", "En Proceso", "Finalizado"])
    com_hito2 = st.text_input("Comentario Hito 1.2")
with e2_col:
    est_hito3 = st.selectbox("Estado Hito 1.3 (Factibilidad y Riesgos)", ["Pendiente", "En Proceso", "Finalizado"])
    com_hito3 = st.text_input("Comentario Hito 1.3")

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
    teoria_mercado = {}
    conceptos_mercado = ["Diagnóstico causal", "Alcance técnico", "Problema", "Causa", "Efecto", "Árbol de problemas", "Storytelling"]
    
    for c in conceptos_mercado:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            def_val = st.text_input(f"Definición - {c}", key=f"def_{c}")
        with col_t2:
            elem_val = st.text_input(f"Elementos Clave - {c}", key=f"elem_{c}")
        with col_t3:
            fuent_val = st.text_input(f"Fuente - {c}", key=f"src_{c}")
        teoria_mercado[c] = {"def": def_val, "elem": elem_val, "fuent": fuent_val}

    st.subheader("2. Árbol de Problemas")
    prob_central = st.text_area("Descripción del Problema Central")
    
    st.markdown("🖼️ **Evidencia Visual del Árbol de Problemas**")
    link_arbol = st.text_input("Enlace al Diagrama del Árbol (Miro / Lucidchart / Canva / Figma)")
    img_arbol = st.file_uploader("Cargar pantallazo / imagen del Árbol de Problemas", type=["png", "jpg", "jpeg"], key="img_arbol")
    
    st.markdown("**Efectos**")
    efectos_data = []
    for i in range(1, 4):
        st.write(f"*Efecto {i}*")
        col_e1, col_e2, col_e3 = st.columns(3)
        with col_e1:
            desc = st.text_input(f"Descripción Efecto {i}")
        with col_e2:
            evid = st.text_input(f"Evidencia y dato clave Efecto {i}")
        with col_e3:
            fuent = st.text_input(f"Fuente Efecto {i}")
        efectos_data.append((f"Efecto {i}", desc, evid, fuent))

    st.markdown("**Causas Raíz**")
    causas_data = []
    for i in range(1, 4):
        st.write(f"*Causa Raíz {i}*")
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            desc = st.text_input(f"Descripción Causa Raíz {i}")
        with col_c2:
            evid = st.text_input(f"Evidencia y dato clave Causa {i}")
        with col_c3:
            fuent = st.text_input(f"Fuente Causa Raíz {i}")
        causas_data.append((f"Causa Raíz {i}", desc, evid, fuent))

    st.subheader("3. Alcance Técnico")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("**Qué abarca el proyecto**")
        si_desc = st.text_area("Descripción (Qué abarca)")
        si_just = st.text_area("Justificación (Qué abarca)")
    with col_a2:
        st.markdown("**Qué NO abarca el proyecto**")
        no_desc = st.text_area("Descripción (Qué NO abarca)")
        no_just = st.text_area("Justificación (Qué NO abarca)")

    st.subheader("4. Storytelling (Guión)")
    storytelling_txt = st.text_area("Guión del Storytelling / Necesidad del Cliente")

# ------------------------------------------------------------------------------
# 🟡 DIRECTOR TÉCNICO Y OPERACIONES
# ------------------------------------------------------------------------------
with tab_tecnico:
    st.header("🟡 Director Técnico y Operaciones")
    
    st.subheader("1. Fundamentación Teórica")
    teoria_tecnico = {}
    conceptos_tecnico = ["Matriz de pesos Ponderados", "Matriz AHP", "Criterios", "Alternativas"]
    
    for c in conceptos_tecnico:
        st.markdown(f"**{c}**")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            def_val = st.text_input(f"Definición - {c}", key=f"def_tec_{c}")
        with col_t2:
            elem_val = st.text_input(f"Elementos Clave - {c}", key=f"elem_tec_{c}")
        with col_t3:
            fuent_val = st.text_input(f"Fuente - {c}", key=f"src_tec_{c}")
        teoria_tecnico[c] = {"def": def_val, "elem": elem_val, "fuent": fuent_val}

    st.subheader("2. Matriz AHP / Pesos Ponderados")
    criterios_val = st.text_area("Criterios (Nombre, Valor y Justificación)")
    alternativas_val = st.text_area("Alternativas (Nombre, Valor y Justificación)")
    
    st.subheader("3. AI Log (Prompt de IA)")
    prompt_ia = st.text_area("Prompt utilizado para la IA / Script")
    
    st.subheader("4. Ejecución en Google Colab y Opción Ganadora")
    link_colab = st.text_input("Enlace al Notebook de Colab Executed")
    img_colab = st.file_uploader("Cargar pantallazo de la ejecución del código / Gráfico AHP", type=["png", "jpg", "jpeg"], key="img_colab")
    opcion_ganadora = st.text_area("Opción Ganadora y Análisis Técnico")

# ------------------------------------------------------------------------------
# 🔴 DIRECTOR FINANCIERO Y RIESGOS
# ------------------------------------------------------------------------------
with tab_financiero:
    st.header("🔴 Director Financiero y Riesgos")
    
    st.subheader("1. Fundamentación Teórica (Repositorio / Data Room)")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        def_repo = st.text_input("Definición (Repositorio)")
    with col_f2:
        elem_repo = st.text_input("Elementos Clave (Repositorio)")
    with col_f3:
        fuent_repo = st.text_input("Fuente (Repositorio)")
        
    link_repositorio = st.text_input("Link al Repositorio / Data Room (Google Drive / Sheets)")
    img_dataroom = st.file_uploader("Cargar captura de pantalla de la estructura del Data Room", type=["png", "jpg", "jpeg"], key="img_data")

    st.subheader("2. Validación de Datos Reales")
    val_items = ["Datos de mercado y precios", "Datos técnicos operativos", "Estructura de Costos", "Funcionamiento Matriz"]
    validaciones = {}
    
    for item in val_items:
        st.markdown(f"**{item}**")
        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            exis = st.selectbox(f"¿Existe? - {item}", ["Sí", "No"], key=f"ex_{item}")
        with col_v2:
            evid = st.text_input(f"Evidencia de fuentes - {item}", key=f"ev_{item}")
        with col_v3:
            fuent = st.text_input(f"Fuente - {item}", key=f"fu_{item}")
        validaciones[item] = {"exis": exis, "evid": evid, "fuent": fuent}

# ------------------------------------------------------------------------------
# 🎯 DIRECTOR GENERAL (INTEGRACIÓN Y DESCARGA)
# ------------------------------------------------------------------------------
with tab_general:
    st.header("🎯 Director General")
    
    nombre_formal = st.text_input("Nombre Formal del Proyecto")
    resumen_proyecto = st.text_area("Resumen del Proyecto")
    
    st.markdown("**Descripción del Cliente**")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        desc_cliente = st.text_area("Descripción del Cliente")
    with col_g2:
        fuent_cliente = st.text_input("Fuente")
        evid_cliente = st.text_input("Evidencia")
        
    objetivo_general = st.text_area("Objetivo General Aprobado")
    
    # GENERADOR DE WORD (.DOCX) CON IMÁGENES
    if st.button("🚀 Generar Bitácora Completa (.docx)"):
        doc = Document()
        doc.add_heading('FIRMA DE CONSULTORÍA EN INGENIERÍA INDUSTRIAL', 0)
        doc.add_heading('Bitácora N° 01: Identificación de Oportunidades (Gate 0)', level=1)
        
        # Bloque 1
        doc.add_heading('Bloque 1: Header de Control', level=2)
        t1 = doc.add_table(rows=5, cols=2)
        t1.rows[0].cells[0].text = "Director de Proyectos / General"
        t1.rows[0].cells[1].text = integrante_1
        t1.rows[1].cells[0].text = "Director de Mercado"
        t1.rows[1].cells[1].text = f"{integrante_2} (Grupo: {grupo})"
        t1.rows[2].cells[0].text = "Director Financiero y Riesgos"
        t1.rows[2].cells[1].text = integrante_3
        t1.rows[3].cells[0].text = "Director Técnico y Operaciones"
        t1.rows[3].cells[1].text = integrante_4
        t1.rows[4].cells[0].text = "Fecha / Módulo"
        t1.rows[4].cells[1].text = fecha_modulo
        
        # Bloque 2
        doc.add_heading('Bloque 2: Matriz de Entregables e Hitos', level=2)
        t2 = doc.add_table(rows=4, cols=4)
        t2.rows[0].cells[0].text = "Hito"
        t2.rows[0].cells[1].text = "Responsable"
        t2.rows[0].cells[2].text = "Estado"
        t2.rows[0].cells[3].text = "Comentario"
        
        t2.rows[1].cells[0].text = "Selección Multicriterio en Python"
        t2.rows[1].cells[1].text = "Director Técnico"
        t2.rows[1].cells[2].text = est_hito1
        t2.rows[1].cells[3].text = com_hito1
        
        t2.rows[2].cells[0].text = "Diagnóstico Causal y Alcance"
        t2.rows[2].cells[1].text = "Director Mercado"
        t2.rows[2].cells[2].text = est_hito2
        t2.rows[2].cells[3].text = com_hito2
        
        t2.rows[3].cells[0].text = "Matriz Factibilidad y Riesgos"
        t2.rows[3].cells[1].text = "Director Financiero"
        t2.rows[3].cells[2].text = est_hito3
        t2.rows[3].cells[3].text = com_hito3

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
            tm.rows[idx].cells[1].text = teoria_mercado[k]["def"]
            tm.rows[idx].cells[2].text = teoria_mercado[k]["elem"]
            tm.rows[idx].cells[3].text = teoria_mercado[k]["fuent"]

        doc.add_heading('2. Árbol de Problemas', level=3)
        doc.add_paragraph(f"Problema Central: {prob_central}")
        if link_arbol:
            doc.add_paragraph(f"🔗 Enlace al Diagrama Interactivo: {link_arbol}")
        if img_arbol is not None:
            doc.add_paragraph("Captura del Árbol de Problemas:")
            doc.add_picture(io.BytesIO(img_arbol.getvalue()), width=Inches(5.5))

        tap = doc.add_table(rows=7, cols=4)
        tap.rows[0].cells[0].text = "Nivel del Árbol"
        tap.rows[0].cells[1].text = "Descripción"
        tap.rows[0].cells[2].text = "Evidencia y Dato Clave"
        tap.rows[0].cells[3].text = "Fuente"
        
        row_i = 1
        for item in efectos_data:
            tap.rows[row_i].cells[0].text = item[0]
            tap.rows[row_i].cells[1].text = item[1]
            tap.rows[row_i].cells[2].text = item[2]
            tap.rows[row_i].cells[3].text = item[3]
            row_i += 1
        for item in causas_data:
            tap.rows[row_i].cells[0].text = item[0]
            tap.rows[row_i].cells[1].text = item[1]
            tap.rows[row_i].cells[2].text = item[2]
            tap.rows[row_i].cells[3].text = item[3]
            row_i += 1

        doc.add_heading('3. Alcance Técnico', level=3)
        ta = doc.add_table(rows=3, cols=3)
        ta.rows[0].cells[0].text = "Delimitación"
        ta.rows[0].cells[1].text = "Descripción"
        ta.rows[0].cells[2].text = "Justificación"
        ta.rows[1].cells[0].text = "Qué abarca el proyecto"
        ta.rows[1].cells[1].text = si_desc
        ta.rows[1].cells[2].text = si_just
        ta.rows[2].cells[0].text = "Qué NO abarca el proyecto"
        ta.rows[2].cells[1].text = no_desc
        ta.rows[2].cells[2].text = no_just

        doc.add_heading('4. Storytelling', level=3)
        doc.add_paragraph(storytelling_txt)

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
            tt.rows[idx].cells[1].text = teoria_tecnico[k]["def"]
            tt.rows[idx].cells[2].text = teoria_tecnico[k]["elem"]
            tt.rows[idx].cells[3].text = teoria_tecnico[k]["fuent"]

        doc.add_heading('2. Criterios y Alternativas', level=3)
        doc.add_paragraph(f"Criterios: {criterios_val}")
        doc.add_paragraph(f"Alternativas: {alternativas_val}")
        doc.add_paragraph(f"PROMPT IA: {prompt_ia}")
        doc.add_paragraph(f"Link Colab: {link_colab}")
        if img_colab is not None:
            doc.add_paragraph("Captura de Resultados en Colab:")
            doc.add_picture(io.BytesIO(img_colab.getvalue()), width=Inches(5.5))
        doc.add_paragraph(f"Opción Ganadora: {opcion_ganadora}")

        # Director Financiero
        doc.add_heading('Director Financiero y Riesgos', level=2)
        doc.add_heading('1. Repositorio / Data Room', level=3)
        doc.add_paragraph(f"Definición: {def_repo} | Claves: {elem_repo} | Fuente: {fuent_repo}")
        doc.add_paragraph(f"Link Repositorio: {link_repositorio}")
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
            tv.rows[idx].cells[1].text = validaciones[k]["exis"]
            tv.rows[idx].cells[2].text = validaciones[k]["evid"]
            tv.rows[idx].cells[3].text = validaciones[k]["fuent"]

        # Director General
        doc.add_heading('Director General - Síntesis y Aprobación', level=2)
        doc.add_paragraph(f"Nombre Formal del Proyecto: {nombre_formal}")
        doc.add_paragraph(f"Resumen del Proyecto: {resumen_proyecto}")
        doc.add_paragraph(f"Descripción del Cliente: {desc_cliente} (Fuente: {fuent_cliente}, Evidencia: {evid_cliente})")
        doc.add_paragraph(f"Objetivo General Aprobado: {objetivo_general}")

        bio = io.BytesIO()
        doc.save(bio)
        
        st.success("¡Bitácora completa compilada con éxito e imágenes incrustadas!")
        st.download_button(
            label="📄 Descargar Bitácora Oficial (.docx)",
            data=bio.getvalue(),
            file_name=f"Bitacora_Hito_1_{nombre_formal.replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

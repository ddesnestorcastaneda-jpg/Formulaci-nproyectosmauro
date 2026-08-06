# ==========================================================================
    # GENERADOR DE WORD (.DOCX) - FORMATO NARRATIVO Y CONECTADO
    # ==========================================================================
    if st.button("🚀 Generar Bitácora Completa (.docx)"):
        doc = Document()
        
        # Estilos y Encabezado
        doc.add_heading('FIRMA DE CONSULTORÍA EN INGENIERÍA INDUSTRIAL', 0)
        doc.add_heading('Bitácora N° 01: Identificación de Oportunidades (Gate 0)', level=1)
        
        # ---------------------------------------------------------
        # BLOQUE 1: HEADER
        # ---------------------------------------------------------
        doc.add_heading('1. Datos del Equipo', level=2)
        p_equipo = doc.add_paragraph()
        p_equipo.add_run(f"Proyecto / Grupo: {st.session_state.get('grupo', 'No definido')}\n").bold = True
        p_equipo.add_run(f"Director General: {st.session_state.get('integrante_1', '')}\n")
        p_equipo.add_run(f"Director de Mercado: {st.session_state.get('integrante_2', '')}\n")
        p_equipo.add_run(f"Director Financiero: {st.session_state.get('integrante_3', '')}\n")
        p_equipo.add_run(f"Director Técnico: {st.session_state.get('integrante_4', '')}\n")
        p_equipo.add_run(f"Fecha: {st.session_state.get('fecha_modulo', '')}")

        # ---------------------------------------------------------
        # DIRECTOR DE MERCADO (Árbol Narrativo)
        # ---------------------------------------------------------
        doc.add_heading('2. Diagnóstico de Mercado y Árbol de Problemas', level=2)
        
        prob_central = st.session_state.get('prob_central', 'No definido')
        doc.add_paragraph(f"El problema central identificado para el desarrollo de este proyecto es: {prob_central}.")
        
        doc.add_paragraph("En la Figura 1 se observa el diagrama del Árbol de Problemas estructurado por la firma de consultoría, donde se relacionan las causas que originan este problema y los efectos que impactan al usuario o mercado.")
        
        # Inserción de Figura 1 (Si subieron imagen)
        img_arbol = st.session_state.get('img_arbol')
        if img_arbol is not None:
            image_stream = io.BytesIO(img_arbol.getvalue())
            doc.add_picture(image_stream, width=Inches(6.0))
            fig1 = doc.add_paragraph("Figura 1. Diagrama del Árbol de Problemas.")
            fig1.alignment = 1 # Centro
            fig1.runs[0].font.italic = True
        else:
            doc.add_paragraph("[El equipo no adjuntó imagen del Árbol de Problemas]", style='Intense Quote')
            
        link_arbol = st.session_state.get('link_arbol', '')
        if link_arbol:
            doc.add_paragraph(f"Enlace de trabajo interactivo (Miro/Lucidchart): {link_arbol}")

        doc.add_paragraph("A partir del análisis detallado en la figura anterior, las causas del problema detectado son las siguientes:")
        for i in range(1, 4):
            desc_c = st.session_state.get(f"desc_causa_{i}", "")
            evid_c = st.session_state.get(f"evid_causa_{i}", "")
            src_c = st.session_state.get(f"src_causa_{i}", "")
            if desc_c:
                doc.add_paragraph(f"Causa {i}: {desc_c}. (Evidencia: {evid_c} | Fuente: {src_c})", style='List Bullet')

        doc.add_paragraph("Asimismo, los efectos principales que este problema genera en el entorno son:")
        for i in range(1, 4):
            desc_e = st.session_state.get(f"desc_efecto_{i}", "")
            evid_e = st.session_state.get(f"evid_efecto_{i}", "")
            src_e = st.session_state.get(f"src_efecto_{i}", "")
            if desc_e:
                doc.add_paragraph(f"Efecto {i}: {desc_e}. (Evidencia: {evid_e} | Fuente: {src_e})", style='List Bullet')

        doc.add_heading('3. Alcance del Proyecto', level=3)
        doc.add_paragraph("Para mitigar estas causas, se ha delimitado un alcance claro para la solución técnica.")
        doc.add_paragraph(f"Lo que SÍ abarca el proyecto: {st.session_state.get('si_desc', '')}")
        doc.add_paragraph(f"Lo que NO abarca el proyecto: {st.session_state.get('no_desc', '')}")

        # ---------------------------------------------------------
        # DIRECTOR TÉCNICO (AHP Narrativo)
        # ---------------------------------------------------------
        doc.add_heading('4. Evaluación Técnica y Matriz AHP', level=2)
        
        doc.add_paragraph("Para resolver la problemática planteada, el equipo técnico postuló tres (3) alternativas de proyecto candidatas:")
        doc.add_paragraph(f"Propuesta 1: {st.session_state.get('propuesta_1', '')}", style='List Number')
        doc.add_paragraph(f"Propuesta 2: {st.session_state.get('propuesta_2', '')}", style='List Number')
        doc.add_paragraph(f"Propuesta 3: {st.session_state.get('propuesta_3', '')}", style='List Number')

        doc.add_paragraph(f"La selección definitiva se realizó mediante una matriz multicriterio (AHP), evaluando los siguientes criterios y pesos: {st.session_state.get('criterios_val', '')}")
        
        doc.add_paragraph("En la Figura 2 se presenta la ejecución del algoritmo de ponderación y el gráfico de resultados procesado en Google Colab.")

        # Inserción de Figura 2
        img_colab = st.session_state.get('img_colab')
        if img_colab is not None:
            image_stream2 = io.BytesIO(img_colab.getvalue())
            doc.add_picture(image_stream2, width=Inches(6.0))
            fig2 = doc.add_paragraph("Figura 2. Ejecución y Resultados del Código AHP (Colab).")
            fig2.alignment = 1
            fig2.runs[0].font.italic = True
        else:
            doc.add_paragraph("[El equipo no adjuntó la gráfica de resultados de Colab]", style='Intense Quote')

        doc.add_heading('4.1 Selección Final y Auditoría de IA', level=3)
        doc.add_paragraph(f"Proyecto Ganador Seleccionado: {st.session_state.get('opcion_ganadora', '')}")
        
        doc.add_paragraph("Para la construcción del modelo en Python se utilizó inteligencia artificial. Durante el proceso de auditoría del código generado por la IA, el ingeniero detectó y ajustó lo siguiente:")
        doc.add_paragraph(f"Auditoría Técnica: {st.session_state.get('audit_ia', '')}", style='Intense Quote')

        # Descarga final
        bio = io.BytesIO()
        doc.save(bio)
        
        st.success("¡Bitácora generada con éxito en formato de informe técnico!")
        st.download_button(
            label="📄 Descargar Informe Técnico (.docx)",
            data=bio.getvalue(),
            file_name=f"Informe_Tecnico_Hito_1_{st.session_state.get('grupo', 'Proyecto')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

import streamlit as st
from datetime import date, datetime
from backend.views import pegar_planilhao_filtrado
from backend.utils import validar_dia_util

def mostrar_planilhao():
    """
    Exibe a página do Planilhão, permitindo ao usuário carregar e visualizar os dados financeiros.
    """
    st.title("📋 Planilhão")
    st.write("""
        O Planilhão fornece uma visão detalhada dos dados financeiros das principais ações no mercado.
        Aqui você pode filtrar os dados por setores específicos e selecionar a data base para análise.
    """)

    st.header("📌 Parâmetros do Planilhão")
    st.markdown("""
    Configure os parâmetros abaixo para carregar o Planilhão:
    1. Escolha uma **Data Base** válida.
    2. (Opcional) Selecione os **Setores** de interesse para filtrar os dados.
    """)

    # Lista de feriados estáticos (exemplo para 2024 no Brasil)
    feriados = [
        "2024-01-01", "2024-02-13", "2024-03-29", "2024-04-21", "2024-05-01",
        "2024-09-07", "2024-10-12", "2024-11-02", "2024-11-15", "2024-12-25"
    ]
    feriados = [datetime.strptime(data, "%Y-%m-%d").date() for data in feriados]

    # Input: Data base
    data_base = st.date_input(
        "Selecione a Data Base:", 
        value=date(2024,1,2),
        help="Escolha uma data válida (dia útil). Feriados e finais de semana não são aceitos."
    )

    # Validação de finais de semana e feriados
    if not validar_dia_util(data_base, feriados):
        st.error("A data selecionada é inválida (feriado ou final de semana). Por favor, escolha outra data.")
        return

    # Input: Setores
    lista_setores = [
        'petróleo', 'mineração', 'banco', 'financeiro', 'saúde', 'energia', 
        'indústria', 'transporte', 'saneamento', 'seguro', 'varejo', 
        'consumo', 'madeira-papel', 'telecom', 'siderurgico', 'construção', 
        'shopping', 'químico', 'proteína', 'supermercado', 'tecnologia', 
        'agrícola', 'aviação', 'educação', 'textil'
    ]

    setores = st.multiselect(
        "Escolha os Setores para Filtrar (Opcional):", 
        options=lista_setores, 
        default=st.session_state.get("setores", []),
        help="Você pode selecionar um ou mais setores para filtrar os dados do Planilhão."
    )

    st.markdown("---")
    st.header("📊 Visualizar Planilhão")
    st.markdown("""
    Após configurar os parâmetros acima, clique no botão **Ver Planilhão** para carregar os dados.
    """)

    # Botão para carregar os dados
    if st.button("Carregar Planilhão"):
        with st.spinner("Carregando dados..."):
            try:
                # Obtém os dados do backend
                df_planilhao = pegar_planilhao_filtrado(data_base.strftime('%Y-%m-%d'), setores)

                if df_planilhao.empty:
                    st.warning("Nenhum dado encontrado. Verifique os filtros aplicados ou escolha outra data.")
                else:
                    # Armazena os dados no session_state
                    st.session_state["planilhao"] = df_planilhao
                    st.session_state["data_base"] = data_base
                    st.session_state["setores"] = setores

                    # Exibe o Planilhão
                    st.success("Planilhão carregado com sucesso! Veja os resultados abaixo:")
                    st.write("### Resultados do Planilhão:")
                    st.dataframe(df_planilhao)
            except Exception as e:
                st.error(f"Erro ao carregar dados: {e}")

    # Exibe os dados armazenados no session_state, se existirem
    if "planilhao" in st.session_state:
        st.write("### Planilhão Anterior:")
        st.dataframe(st.session_state["planilhao"])

    st.markdown("---")
    st.header("📂 Informações Adicionais")
    st.markdown("""
    - O Planilhão apresenta informações financeiras detalhadas das ações disponíveis.
    - Feriados e finais de semana são excluídos para evitar inconsistências nos dados.
    - Para mais informações ou dúvidas, entre em contato com o suporte.
    """)

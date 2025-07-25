import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.badges import badge



st.markdown(
    """
    <div style="display: flex; align-items: center; margin-bottom: 2em;">
        <img src="https://whatthelogo.com/storage/logos/fondation-mohammed-6-88030.png" width="180" style="margin-right: 30px; border-radius: 10px; border: 2px solid #B22222;">
        <h1 style="color: #B22222; font-family: 'Segoe UI', 'Arial', sans-serif; margin: 0;">
            Fondation Mohammed VI
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        body {
        color: black;
    }
    @media (prefers-color-scheme: dark) {
        body {
            color: white;
        }
    }
        /* Main background */
        .stApp {
            background-color: #F5F5F5 !important;
        }
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            color: #FFFFFF !important;
            border-right: 1px solid #CCCCCC;
        }
        [data-testid="stSidebar"] .css-1v3fvcr, 
        [data-testid="stSidebar"] .css-1d391kg,
        [data-testid="stSidebar"] .stRadio label,
        [data-testid="stSidebar"] .stRadio div,
        [data-testid="stSidebar"] .stTextInput,
        [data-testid="stSidebar"] .stSelectbox,
        [data-testid="stSidebar"] .stNumberInput {
            color: #FFFFFF !important;
        }
        /* Title/Header */
        h1, h2, h3, h4, h5, h6 {
            color: black !important;
            font-family: 'Segoe UI', 'Arial', sans-serif;
            font-weight: bold;
        }
        h1 {
            font-size: 38px !important;
        }
        /* Main text */
        .stMarkdown, .stText, .st-bb, .st-cq, .st-co, .st-cp, .st-cq, .st-cr, .st-cs, .st-ct, .st-cu, .st-cv, .st-cw, .st-cx, .st-cy, .st-cz {
            color: #FFFFFF !important;
        }
        /* Dataframe/table styling */
        .stDataFrame, .stTable {
            background: #FFFFFF !important;
            border-radius: 8px;
            color: #FFFFFF !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }
        /* Dataframe alternate row colors */
        .stDataFrame tbody tr:nth-child(even) {
            background-color: #F5F5F5 !important;
        }
        .stDataFrame tbody tr:hover, .stTable tbody tr:hover {
            background-color: #DCDCDC !important;
        }
        /* Metric cards */
        .stMetric {
            background: #FFFFFF !important;
            border-radius: 10px;
            padding: 10px 0;
            margin-bottom: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            border: 1px solid #CCCCCC;
            color: #FFFFFF !important;
        }
        /* Metric label */
        .stMetricLabel {
            color: #FFFFFF !important;
        }
        /* Metric value (the big number) */
        div[data-testid="stMetricValue"] {
            color: #FFFFFF !important;
        }
        /* All text below, including markdown, captions, tables, etc. */
        .stCaption, .stMarkdown, .stText, .stDataFrame, .stTable, .st-bb, .st-cq, .st-co, .st-cp, .st-cr, .st-cs, .st-ct, .st-cu, .st-cv, .st-cw, .st-cx, .st-cy, .st-cz, p, span, label {
            color: #FFFFFF !important;
        }
        /* Buttons */
        .stButton>button {
            background-color: #B22222;
            color: #FFFFFF !important;
            border-radius: 6px;
            border: none;
            font-weight: 600;
            padding: 0.5em 1.5em;
            transition: background 0.2s;
        }
        .stButton>button:hover, .stButton>button:focus {
            background-color: #DCDCDC !important;
            color: #B22222 !important;
            border: 1px solid #B22222;
        }
        /* File uploader, multiselect, input */
        .stFileUploader, .stMultiSelect, .stTextInput, .stNumberInput {
            background: #FFFFFF !important;
            border-radius: 6px;
            color: #FFFFFF !important;
            border: 1px solid #CCCCCC;
        }
        .stdownload_button {
            color : white;
        }
        /* Selectbox input text (selected value) */
        div[data-baseweb="select"] div[role="combobox"] {
            color: #FFFFFF !important;
        }
        div[data-baseweb="select"] div[role="combobox"] span {
            color: #FFFFFF !important;
        }
        /* Selectbox background for better contrast */
        div[data-baseweb="select"] {
            background-color: #222 !important;
            border-radius: 6px !important;
        }
        /* Main dropdown text (closed select) */
        div[data-baseweb="select"] > div {
            color: #FFFFFF !important;
        }
        /* Dropdown menu background and text */
        div[data-baseweb="popover"] {
            background-color: #1e1e1e !important;
            color: #FFFFFF !important;
        }
        /* Each option */
        div[data-baseweb="popover"] li {
            color: #FFFFFF !important;
            background-color: #1e1e1e !important;
        }
        /* Hovered option */
        div[data-baseweb="popover"] li:hover {
            background-color: #3c3c3c !important;
            color: #fff !important;
        }
        /* Make text in all Streamlit text input fields white */
        input[type="text"], textarea {
            color: #FFFFFF !important;
            background-color: #1e1e1e !important;
            border-radius: 6px !important;
        }
        /* Table header and cell text white */
        th, td {
            color: #FFFFFF !important;
        }
        /* Streamlit selectbox label */
        label[for^="selectbox"] {
            color: #FFFFFF !important;
        }
    </style>
""", unsafe_allow_html=True)


def load_data():
    df2 = pd.read_excel("merged_tables.xlsx", parse_dates=['Date'])
    return df2
df2 = load_data()

st.set_page_config(page_title='Tableau de Bord des Prestations', page_icon=':bar_chart:', layout='wide')
st.sidebar.title('Portail des prestations')
page = st.sidebar.radio('Aller à ', ['Page d’accueil', 'statistiques globales', 'Gestion des adhérents','Recherche par prestation'], index=st.session_state.get('page', 0))

#Home
if page == 'Page d’accueil':
    # ---------- HEADER ----------
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 2em;">
            <div>
                <h1 style="color: #B22222; font-family: 'Segoe UI', 'Arial', sans-serif; margin-bottom: 0;">Bienvenue</h1>
                <h3 style="color: #444; font-family: 'Segoe UI', 'Arial', sans-serif; margin-top: 0;">Portail de la Fondation Mohammed VI</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .welcome-card {
                background: #fff;
                border-radius: 16px;
                box-shadow: 0 2px 16px rgba(178,34,34,0.10);
                padding: 2.5em 2em 2em 2em;
                margin-bottom: 2em;
                text-align: center;
                border: 1.5px solid #f0f0f0;
            }
            .welcome-title {
                font-size: 2em;
                color: #B22222;
                font-weight: bold;
                margin-bottom: 0.5em;
            }
            .welcome-desc {
                font-size: 1.15em;
                color: #333;
                margin-bottom: 1.5em;
            }
            .badge {
                display: inline-block;
                background: #B22222;
                color: #fff;
                border-radius: 8px;
                padding: 0.2em 0.8em;
                font-size: 0.95em;
                margin: 0.2em;
            }
            .quick-links {
                display: flex;
                justify-content: center;
                gap: 2em;
                margin-top: 2em;
            }
            .quick-link-card {
                background: #f8f8f8;
                border-radius: 10px;
                padding: 1.2em 1.5em;
                min-width: 180px;
                text-align: center;
                box-shadow: 0 1px 6px rgba(178,34,34,0.07);
                transition: box-shadow 0.2s, border 0.2s;
                border: 1px solid #eee;
            }
            .quick-link-card:hover {
                box-shadow: 0 2px 16px rgba(178,34,34,0.13);
                border: 1.5px solid #B22222;
            }
            .quick-link-icon {
                font-size: 2em;
                margin-bottom: 0.3em;
            }
            .footer {
                text-align:center;
                margin-top:2em;
                color: #888;
                font-size: 0.95em;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="welcome-card">
            <div class="welcome-title">Bienvenue sur votre espace digital</div>
            <div class="welcome-desc">
                Ce portail vous offre un accès centralisé à toutes les informations sur les prestations consommées.<br><br>
                <span class="badge">Sécurisé</span>
                <span class="badge">Simple</span>
                <span class="badge">Rapide</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    

    st.markdown("""
        <div class="footer">
            ✨ Réalisé par <b>Aya Ait Allal</b> — Juillet 2025
        </div>
    """, unsafe_allow_html=True)

    
#statistiques globales
if page == 'statistiques globales':
    
    st.title('statistiques globales')
    st.markdown("""
    <style>
        .metric-label > div {
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    
    
    col1, col2, col3 = st.columns(3)
    total_prestations = len(df2)
    col1.metric("Nombre de prestations", total_prestations)
    total_cost = df2['Montant'].sum()
    col2.metric("Cout total (MAD)", f"{total_cost:,.0f}")
    average_montant = df2['Montant'].mean()
    col3.metric("Montant moyen (MAD)", f"{average_montant:,.0f}")
        
    st.markdown("---")
        
    col1, col2 = st.columns(2)
    # Pie chart
    with col1:
        st.subheader("Répartition des statuts de traitement")
        threshold = 0.03  # 3%
        status_counts = df2['Statut'].value_counts(normalize=True)
        grouped_statuses = status_counts[status_counts >= threshold]
        others = status_counts[status_counts < threshold].sum()

        final_labels = grouped_statuses.index.tolist()
        final_sizes = grouped_statuses.values.tolist()

        if others > 0:
            final_labels.append("Autres")
            final_sizes.append(others)

        fig, ax = plt.subplots(figsize=(6, 6))
        colors = plt.get_cmap("Set3").colors if hasattr(plt.get_cmap("Set3"), 'colors') else None
        wedges, texts, autotexts = ax.pie(
            final_sizes,
            labels=final_labels,
            autopct='%1.1f%%',
            startangle=140,
            textprops={'fontsize': 12},
            colors=colors
        )
        ax.axis('equal')
        st.pyplot(fig)

    # Bar chart
    with col2:
        st.subheader('Montant total par type de prestation')
        Montant_parType = df2.groupby('Type prestation', as_index=False)['Montant'].sum().sort_values(by='Montant', ascending=False)
        fig2, ax2 = plt.subplots(figsize=(16, 16))
        sns.barplot(data=Montant_parType, x='Type prestation', y='Montant', palette='Set2', ax=ax2)
        ax2.set_xlabel('Type de prestation')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
        ax2.set_ylabel('Montant total (MAD)')
        ax2.set_title('Montant total par type de prestation')
        fig2.tight_layout()
        st.pyplot(fig2)
        
        
    
    

elif page == 'Gestion des adhérents':
    st.title('Gestion des adhérents')
    
    num_adherent = st.text_input('Entrer le numéro d\'adhérent')
    montant_alias = ["Montant", "Montant_Gere", "montant_crédit", "MONT_REMB_CNOPS"]
    adherent_alias = ['NumeroAdherent', 'Num_Adherent_Adherent', 'N°_Adherent_Adherent', 'Num_Adherent', 'NUM_ADHERENT']

    if st.button("Rechercher"):
        if num_adherent:
            results_found = False
            excel_file = pd.ExcelFile("ExtractionStagiaire 11.07.2025.xlsx")
            sheet_names = excel_file.sheet_names[1:]
            for sheet_name in excel_file.sheet_names:
                df_sheet = excel_file.parse(sheet_name)
                # Try to find the correct column for adhérent
                for alias in adherent_alias:
                    if alias in df_sheet.columns:
                        df_search = df_sheet.rename(columns={alias: 'Num Adherent'})
                        break
                else:
                    df_search = df_sheet

                if 'Num Adherent' in df_search.columns:
                    matched_rows = df_search[df_search['Num Adherent'].astype(str).str.contains(num_adherent)]
                    if not matched_rows.empty:
                        results_found = True
                        st.markdown(f"### Prestation consommée : {sheet_name}")
                        col1, col2 = st.columns(2)
                        # Total montant in col1
                        for col in montant_alias:
                            if col in matched_rows.columns:
                                total_montant = matched_rows[col].sum()
                                col1.metric("💰 Montant total", f"{total_montant:.2f} MAD")
                                break
                        # Table in col2
                        col2.dataframe(matched_rows)
            if not results_found:
                st.warning("Aucun client correspondant trouvé dans les feuilles.")
        else:
            st.warning("Veuillez entrer un numéro d’adhérent.")
            

            
    st.write('Veuillez charger un fichier CSV contenant les numéros d\'adhérents')    
    uploaded_file = st.file_uploader('Uploader un fichier CSV', type=['csv'])
    
    if uploaded_file is not None :
        uploaded_df = pd.read_csv(uploaded_file)
        adherent_list = uploaded_df.iloc[:, 0].astype(str).tolist()
        filtered_df = df2[df2['Num Adherent'].isin(adherent_list)]
        
        if not filtered_df.empty :
            st.success(f"Fichier chargé avec succès. {len(adherent_list)} clients trouvés.")
            col1, col2, col3 = st.columns(3)
            total_prestations = len(filtered_df)
            col1.metric("Nombre de prestations", total_prestations)
            total_cost = filtered_df['Montant'].sum()
            col2.metric("Cout total (MAD)", f"{total_cost:,.0f}")
            average_montant = filtered_df['Montant'].mean()
            col3.metric("Montant moyen (MAD)", f"{average_montant:,.0f}")
            
            
            st.dataframe(filtered_df)
            
            # Download button
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button('Telecharger la liste des adherents', csv, file_name='adherents.csv')

            # --- NEW: Select a Num Adherent and search in Excel sheets ---
            selected_num = st.selectbox(
                "Choisissez un Num Adherent pour voir ses prestations détaillées dans les feuilles Excel :",
                filtered_df['Num Adherent'].astype(str).unique()
            )

            if selected_num:
                excel_file = pd.ExcelFile("ExtractionStagiaire 11.07.2025.xlsx")
                adherent_alias = ['NumeroAdherent', 'Num_Adherent_Adherent', 'N°_Adherent_Adherent', 'Num_Adherent', 'NUM_ADHERENT']
                found_any = False
                for sheet_name in excel_file.sheet_names:
                    df_sheet = excel_file.parse(sheet_name)
                    # Try to find the correct column for adhérent
                    found_col = None
                    for alias in adherent_alias:
                        for col in df_sheet.columns:
                            if col.lower().replace("é", "e").replace("_", " ").replace("-", " ").strip() == alias.lower().replace("é", "e").replace("_", " ").replace("-", " ").strip():
                                found_col = col
                                break
                        if found_col:
                            break
                    if found_col:
                        df_sheet['Num Adherent'] = df_sheet[found_col].astype(str).str.strip()
                        matched_rows = df_sheet[df_sheet['Num Adherent'] == str(selected_num).strip()]
                        if not matched_rows.empty:
                            found_any = True
                            st.markdown(f"#### Prestation consommée : {sheet_name}")
                            st.dataframe(matched_rows)
                if not found_any:
                    st.info("Aucune prestation trouvée pour ce Num Adherent dans les feuilles Excel.")
        else:
            st.warning("Aucun client correspondant trouvé")
        
# filtrer par service
elif page == 'Recherche par prestation':
    st.title('Recherche par prestation')
    excel_file = pd.ExcelFile("ExtractionStagiaire 11.07.2025.xlsx")
    sheet_names = excel_file.sheet_names[1:]
    
    selected_sheet = st.selectbox('Choisisser une prestation', sheet_names)
    df_prestation = pd.read_excel(excel_file, sheet_name=selected_sheet)
   
    col1, col2, col3 = st.columns(3)
    
    

    with col1:
       montant_alias = ["Montant", "Montant_Gere", "montant_crédit"]
       for col in df_prestation :
           if col in montant_alias :
               total_montant = df_prestation[col].sum()
               col1.metric(f'Montant total  :', total_montant)
               found = True
               
    with col2 :
        col2.metric('Nombre de benificiaires', len(df_prestation))
        
    with col3 : 
        col3.metric('Colonnes disponibles', len(df_prestation.columns))
 
    columns_show = st.multiselect('Colonnes a afficher', df_prestation.columns.tolist())
    num_row = st.number_input('Nombre de lignes a afficher', min_value=5, max_value=len(df_prestation), value=5, step=1)
    if columns_show :
        st.dataframe(df_prestation[columns_show].head(num_row))
        
        
    else : 
        st.info('Veuillez selectionner au moins une colonnes')
    
    

    
      
       
    
        
        
        

    
    
    



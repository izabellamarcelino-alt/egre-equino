import streamlit as st

st.set_page_config(page_title="EGRE - Escore de Gravidade Respiratória Equino")

st.title("🐎 EGRE")
st.subheader("Escore de Gravidade Respiratória Equino")

st.markdown("### Avaliação Clínica")

# Frequência Respiratória
fr = st.number_input("Frequência Respiratória (mov/min)", min_value=0)

# Esforço Respiratório
esforco = st.selectbox(
    "Esforço Respiratório",
    [
        "Normal",
        "Leve aumento abdominal",
        "Uso de musculatura acessória",
        "Dispneia marcada"
    ]
)

# Secreção Nasal
secrecao = st.selectbox(
    "Secreção Nasal",
    [
        "Ausente",
        "Serosa discreta",
        "Mucosa ou mucopurulenta",
        "Purulenta abundante"
    ]
)

# Auscultação
ausculta = st.selectbox(
    "Auscultação Pulmonar",
    [
        "Normal",
        "Roncos leves",
        "Sibilos ou crepitações",
        "Redução de sons + ruídos intensos"
    ]
)

# Temperatura
temp = st.number_input("Temperatura Corporal (°C)", min_value=30.0, format="%.1f")

score = 0

# Pontuação FR
if 8 <= fr <= 16:
    score += 0
elif 17 <= fr <= 20:
    score += 1
elif 21 <= fr <= 30:
    score += 2
elif fr > 30:
    score += 3

# Pontuação esforço
score += [
    "Normal",
    "Leve aumento abdominal",
    "Uso de musculatura acessória",
    "Dispneia marcada"
].index(esforco)

# Pontuação secreção
score += [
    "Ausente",
    "Serosa discreta",
    "Mucosa ou mucopurulenta",
    "Purulenta abundante"
].index(secrecao)

# Pontuação ausculta
score += [
    "Normal",
    "Roncos leves",
    "Sibilos ou crepitações",
    "Redução de sons + ruídos intensos"
].index(ausculta)

# Pontuação temperatura
if 37.5 <= temp <= 38.5:
    score += 0
elif 38.6 <= temp <= 39.0:
    score += 1
elif 39.1 <= temp <= 39.5:
    score += 2
elif temp > 39.5:
    score += 3

if st.button("Calcular EGRE"):
    st.markdown(f"## Pontuação Total: {score}")

    if score <= 4:
        st.success("🟢 Classificação: LEVE")
        st.markdown("""
        **Recomendações:**
        - Monitoramento clínico
        - Redução de exercício
        - Avaliação se persistir
        """)

    elif 5 <= score <= 9:
        st.warning("🟡 Classificação: MODERADO")
        st.markdown("""
        **Recomendações:**
        - Avaliação veterinária recomendada
        - Possível terapia anti-inflamatória
        - Isolamento se suspeita infecciosa
        """)

    else:
        st.error("🔴 Classificação: GRAVE")
        st.markdown("""
        **Recomendações:**
        - Atendimento veterinário imediato
        - Risco de pneumonia ou afecção grave
        - Pode necessitar exames complementares
        """)

st.markdown("---")
st.caption("Ferramenta auxiliar. Não substitui avaliação veterinária completa.")

import streamlit as st

def convert_number(value, base_from, base_to):
    try:
        base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
        num = int(value, base_dict[base_from])
        if base_to == "Binário":
            return bin(num)[2:]
        elif base_to == "Decimal":
            return str(num)
        elif base_to == "Octal":
            return oct(num)[2:]
        elif base_to == "Hexadecimal":
            return hex(num)[2:].upper()
    except ValueError:
        return "Valor inválido para a base selecionada."

def perform_operation(num1, num2, operation, base):
    base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
    try:
        n1 = int(num1, base_dict[base])
        n2 = int(num2, base_dict[base])
        result = 0
        if operation == "Adição":
            result = n1 + n2
        elif operation == "Subtração":
            result = n1 - n2
        elif operation == "Multiplicação":
            result = n1 * n2
        elif operation == "Divisão":
            result = n1 // n2 if n2 != 0 else "Erro: divisão por zero"
        else:
            return "Operação inválida"

        if isinstance(result, str):
            return result  # Erro de divisão por zero

        if base == "Binário":
            return bin(result)[2:]
        elif base == "Decimal":
            return str(result)
        elif base == "Octal":
            return oct(result)[2:]
        elif base == "Hexadecimal":
            return hex(result)[2:].upper()
    except ValueError:
        return "Número inválido para a base selecionada."

# --- Interface ---
st.set_page_config(page_title="Conversor de Sistemas Numéricos", page_icon="🧮", layout="centered")
st.title("🧮 Conversor e Operador de Bases Numéricas")
st.markdown("Converta entre **binário**, **decimal**, **octal** e **hexadecimal** e realize operações básicas!")
st.markdown("Integrantes do Grupo: **Marcolino Lemos**, **Loide Padre**, **Zeferino** e **Mikhail Freire**")


tabs = st.tabs(["🔁 Conversor", "➕ Operações"])

# --- Conversor ---
with tabs[0]:
    st.header("🔁 Conversor de Bases")
    value = st.text_input("Digite o número:")
    base_from = st.selectbox("Converter de:", ["Binário", "Decimal", "Octal", "Hexadecimal"])
    base_to = st.selectbox("Para base:", ["Binário", "Decimal", "Octal", "Hexadecimal"])

    if st.button("Converter"):
        result = convert_number(value, base_from, base_to)
        st.success(f"Resultado: {result}")

# --- Operações ---
with tabs[1]:
    st.header("➕ Operações em Bases")
    base = st.selectbox("Base dos números:", ["Binário", "Decimal", "Octal", "Hexadecimal"])
    num1 = st.text_input("Número 1:")
    num2 = st.text_input("Número 2:")
    operation = st.radio("Operação", ["Adição", "Subtração", "Multiplicação", "Divisão"], horizontal=True)

    if st.button("Calcular"):
        result = perform_operation(num1, num2, operation, base)
        st.success(f"Resultado: {result}")

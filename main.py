import streamlit as st
from math import floor



# Configuração de estilo
def set_bg_hack(main_bg):
    main_bg_ext = "png"
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover;
            background-attachment: fixed;
        }}
        .css-1v0mbdj {{
            border-radius: 10px;
        }}
        .st-b7 {{
            background-color: rgba(255, 255, 255, 0.8);
        }}
        .st-b8 {{
            background-color: rgba(245, 245, 245, 0.9);
        }}
        .stButton>button {{
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 10px 24px;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }}
        .stSelectbox, .stTextInput {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
        }}
        .stRadio > div {{
            flex-direction: row;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 10px;
        }}
        .stSuccess {{
            background-color: rgba(209, 242, 235, 0.9);
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            border-left: 5px solid #00cc99;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
        }}
        .stTabs [data-baseweb="tab"] {{
            background: rgba(255, 255, 255, 0.7);
            border-radius: 10px 10px 0 0;
            padding: 10px 20px;
            margin-right: 5px;
        }}
        .stTabs [aria-selected="true"] {{
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            color: white;
            font-weight: bold;
        }}
        .title {{
            color: #2c3e50;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 0.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        .subheader {{
            color: #2c3e50;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 1.5em;
        }}
        .team {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def convert_fractional_part(fractional_part, base_from, base_to):
    """Converte a parte fracionária (0.xxx) entre bases"""
    try:
        base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
        from_base = base_dict[base_from]
        to_base = base_dict[base_to]
        
        # Se origem e destino forem iguais, retorna direto
        if from_base == to_base:
            return fractional_part
        
        # Converte a parte fracionária para decimal primeiro
        decimal_value = 0
        for i, digit in enumerate(fractional_part):
            if digit.isdigit():
                digit_value = int(digit)
            else:
                digit_value = 10 + ord(digit.upper()) - ord('A')
            
            decimal_value += digit_value * (from_base ** -(i + 1))
        
        # Converte de decimal para a base de destino
        result = []
        for _ in range(3):  # Limitando a 3 casas decimais
            decimal_value *= to_base
            digit = int(decimal_value)
            if digit >= 10:
                digit = chr(ord('A') + digit - 10)
            result.append(str(digit))
            decimal_value -= int(decimal_value)
            if decimal_value == 0:
                break
        
        return ''.join(result)
    except:
        return "0"

def convert_number(value, base_from, base_to):
    try:
        base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
        
        # Verifica se é número fracionário
        if '.' in value:
            integer_part, fraction_part = value.split('.')
            fraction_part = fraction_part[:3]  # Limita a 3 casas decimais
        else:
            integer_part = value
            fraction_part = None
        
        # Converte parte inteira
        if integer_part:
            num = int(integer_part, base_dict[base_from])
            if base_to == "Binário":
                converted_int = bin(num)[2:]
            elif base_to == "Decimal":
                converted_int = str(num)
            elif base_to == "Octal":
                converted_int = oct(num)[2:]
            elif base_to == "Hexadecimal":
                converted_int = hex(num)[2:].upper()
        else:
            converted_int = "0"
        
        # Converte parte fracionária se existir
        if fraction_part:
            converted_frac = convert_fractional_part(fraction_part, base_from, base_to)
            return f"{converted_int}.{converted_frac}"
        else:
            return converted_int
    except ValueError:
        return "Valor inválido para a base selecionada."

def perform_operation(num1, num2, operation, base):
    base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
    current_base = base_dict[base]
    
    def to_decimal(number, base):
        if '.' in number:
            integer_part, fraction_part = number.split('.')
            fraction_part = fraction_part[:3]  # Limita a 3 casas decimais
        else:
            integer_part = number
            fraction_part = None
        
        # Converte parte inteira
        int_value = int(integer_part, base) if integer_part else 0
        
        # Converte parte fracionária
        frac_value = 0
        if fraction_part:
            for i, digit in enumerate(fraction_part):
                if digit.isdigit():
                    digit_value = int(digit)
                else:
                    digit_value = 10 + ord(digit.upper()) - ord('A')
                frac_value += digit_value * (base ** -(i + 1))
        
        return int_value + frac_value
    
    def from_decimal(decimal, to_base):
        # Parte inteira
        integer_part = int(decimal)
        if to_base == 2:
            converted_int = bin(integer_part)[2:]
        elif to_base == 8:
            converted_int = oct(integer_part)[2:]
        elif to_base == 16:
            converted_int = hex(integer_part)[2:].upper()
        else:
            converted_int = str(integer_part)
        
        # Parte fracionária
        fractional = decimal - integer_part
        if fractional > 0:
            converted_frac = []
            for _ in range(3):  # Limitando a 3 casas decimais
                fractional *= to_base
                digit = int(fractional)
                if digit >= 10:
                    digit = chr(ord('A') + digit - 10)
                converted_frac.append(str(digit))
                fractional -= int(fractional)
                if fractional == 0:
                    break
            return f"{converted_int}.{''.join(converted_frac)}"
        else:
            return converted_int
    
    try:
        n1 = to_decimal(num1, current_base)
        n2 = to_decimal(num2, current_base)
        
        if operation == "Adição":
            result = n1 + n2
        elif operation == "Subtração":
            result = n1 - n2
        elif operation == "Multiplicação":
            result = n1 * n2
        elif operation == "Divisão":
            if n2 == 0:
                return "Erro: divisão por zero"
            result = n1 / n2
        else:
            return "Operação inválida"
        
        return from_decimal(result, current_base)
    except ValueError:
        return "Número inválido para a base selecionada."

# --- Interface ---
st.set_page_config(page_title="Conversor de Sistemas Numéricos", page_icon="🧮", layout="centered")
st.title("🧮 Conversor e Operador de Bases Numéricas")
st.markdown("Converta entre **binário**, **decimal**, **octal** e **hexadecimal** e realize operações básicas!")
st.markdown("**Agora com suporte a números fracionários (até 3 casas decimais)!**")
st.markdown("Integrantes do Grupo: **Marcolino Lemos**, **Loide Padre**, **Zeferino** e **Mikhail Freire**")

tabs = st.tabs(["🔁 Conversor", "➕ Operações"])

# --- Conversor ---
with tabs[0]:
    st.header("🔁 Conversor de Bases")
    value = st.text_input("Digite o número (use ponto para decimais):")
    base_from = st.selectbox("Converter de:", ["Binário", "Decimal", "Octal", "Hexadecimal"])
    base_to = st.selectbox("Para base:", ["Binário", "Decimal", "Octal", "Hexadecimal"])

    if st.button("Converter"):
        result = convert_number(value, base_from, base_to)
        st.success(f"Resultado: {result}")

# --- Operações ---
with tabs[1]:
    st.header("➕ Operações em Bases")
    base = st.selectbox("Base dos números:", ["Binário", "Decimal", "Octal", "Hexadecimal"])
    num1 = st.text_input("Número 1 (use ponto para decimais):")
    num2 = st.text_input("Número 2 (use ponto para decimais):")
    operation = st.radio("Operação", ["Adição", "Subtração", "Multiplicação", "Divisão"], horizontal=True)

    if st.button("Calcular"):
        result = perform_operation(num1, num2, operation, base)
        st.success(f"Resultado: {result}")






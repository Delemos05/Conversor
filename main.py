import streamlit as st
from math import floor
import time

# Configuração inicial
st.set_page_config(
    page_title="NEON CONVERTER",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Efeito de partículas (JavaScript simplificado)
particles_js = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas');
    canvas.id = 'particles-canvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '-1';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const colors = ['#00ffff', '#ff00ff', '#9d00ff'];
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1;
            this.color = colors[Math.floor(Math.random() * colors.length)];
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3 - 1.5;
        }
        
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
            if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
        }
        
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    
    function init() {
        for (let i = 0; i < 50; i++) {
            particles.push(new Particle());
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
            
            for (let j = i; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.strokeStyle = particles[i].color;
                    ctx.lineWidth = 0.2;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
        
        requestAnimationFrame(animate);
    }
    
    init();
    animate();
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
});
</script>
"""

# Estilo Cyberpunk Neon otimizado
def set_cyberpunk_style():
    st.markdown(
        f"""
        <style>
        /* Base styles */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');
        
        :root {{
            --neon-pink: #ff00ff;
            --neon-cyan: #00ffff;
            --neon-purple: #9d00ff;
            --dark-bg: #0a0a1a;
            --darker-bg: #050510;
        }}
        
        body, .stApp {{
            background-color: var(--dark-bg);
            color: white;
            font-family: 'Rajdhani', sans-serif;
            min-height: 100vh;
        }}
        
        /* Container principal */
        .main-container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 1rem;
            position: relative;
            z-index: 10;
        }}
        
        /* Cards */
        .neon-card {{
            background: rgba(10, 10, 30, 0.7);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid var(--neon-cyan);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.1);
        }}
        
        /* Tipografia */
        h1, h2, h3 {{
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            color: var(--neon-cyan);
            margin-bottom: 1rem !important;
        }}
        
        h1 {{
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 0.5rem !important;
            background: linear-gradient(90deg, var(--neon-cyan), var(--neon-pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        /* Botões */
        .stButton>button {{
            background: transparent;
            color: var(--neon-cyan) !important;
            border: 2px solid var(--neon-cyan);
            border-radius: 4px;
            padding: 0.75rem 1.5rem;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            transition: all 0.3s ease;
        }}
        
        .stButton>button:hover {{
            background: rgba(0, 255, 255, 0.1);
            transform: translateY(-2px);
            box-shadow: 0 0 15px var(--neon-cyan);
        }}
        
        /* Inputs */
        .stTextInput>div>div>input, 
        .stSelectbox>div>div>select {{
            background: rgba(0, 0, 0, 0.3) !important;
            border: 1px solid var(--neon-pink) !important;
            color: white !important;
            border-radius: 4px !important;
            padding: 0.75rem !important;
        }}
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            margin-bottom: 1.5rem;
            border-bottom: none;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background: transparent !important;
            border: 2px solid var(--neon-purple) !important;
            border-radius: 4px !important;
            padding: 0.5rem 1rem !important;
            font-family: 'Orbitron', sans-serif;
            color: var(--neon-purple) !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: rgba(157, 0, 255, 0.2) !important;
            color: white !important;
            border-color: var(--neon-pink) !important;
        }}
        
        /* Mensagens */
        .stAlert {{
            border-left: 4px solid var(--neon-cyan) !important;
            background-color: rgba(0, 0, 0, 0.5) !important;
        }}
        
        /* Responsividade */
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}
            
            .neon-card {{
                padding: 1.5rem;
            }}
        }}
        </style>
        
        {particles_js}
        """,
        unsafe_allow_html=True
    )

# Aplicar estilos
set_cyberpunk_style()

# Funções de conversão (com validação reforçada)
def is_valid_number(number, base):
    if not number:
        return "Erro: Número não pode estar vazio"
    
    base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
    current_base = base_dict[base]
    valid_chars = {
        2: {'0', '1', '.'},
        8: {'0', '1', '2', '3', '4', '5', '6', '7', '.'},
        10: {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'},
        16: {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
             'a', 'b', 'c', 'd', 'e', 'f', 
             'A', 'B', 'C', 'D', 'E', 'F', '.'}
    }
    
    # Verifica caracteres válidos
    for char in number:
        if char not in valid_chars[current_base]:
            return f"Erro: Caractere '{char}' inválido para base {base}"
    
    # Verifica múltiplos pontos
    if number.count('.') > 1:
        return "Erro: Número não pode ter múltiplos pontos decimais"
    
    return None

def convert_fractional_part(fractional_part, base_from, base_to):
    try:
        base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
        from_base = base_dict[base_from]
        to_base = base_dict[base_to]
        
        if from_base == to_base:
            return fractional_part
        
        decimal_value = 0
        for i, digit in enumerate(fractional_part):
            if digit.isdigit():
                digit_value = int(digit)
            else:
                digit_value = 10 + ord(digit.upper()) - ord('A')
            
            decimal_value += digit_value * (from_base ** -(i + 1))
        
        result = []
        for _ in range(4):  # 4 casas decimais de precisão
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
    validation_error = is_valid_number(value, base_from)
    if validation_error:
        return validation_error
    
    base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
    
    try:
        if '.' in value:
            integer_part, fraction_part = value.split('.')
            fraction_part = fraction_part[:4]  # Limita a 4 casas decimais
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
        return "Valor inválido para a base selecionada"

def perform_operation(num1, num2, operation, base):
    validation_error1 = is_valid_number(num1, base)
    validation_error2 = is_valid_number(num2, base)
    
    if validation_error1:
        return validation_error1
    if validation_error2:
        return validation_error2
    
    base_dict = {"Binário": 2, "Decimal": 10, "Octal": 8, "Hexadecimal": 16}
    current_base = base_dict[base]
    
    def to_decimal(number):
        if '.' in number:
            integer_part, fraction_part = number.split('.')
            fraction_part = fraction_part[:4]
        else:
            integer_part = number
            fraction_part = None
        
        # Converte parte inteira
        int_value = int(integer_part, current_base) if integer_part else 0
        
        # Converte parte fracionária
        frac_value = 0
        if fraction_part:
            for i, digit in enumerate(fraction_part):
                if digit.isdigit():
                    digit_value = int(digit)
                else:
                    digit_value = 10 + ord(digit.upper()) - ord('A')
                frac_value += digit_value * (current_base ** -(i + 1))
        
        return int_value + frac_value
    
    def from_decimal(decimal):
        # Parte inteira
        integer_part = int(decimal)
        if current_base == 2:
            converted_int = bin(integer_part)[2:]
        elif current_base == 8:
            converted_int = oct(integer_part)[2:]
        elif current_base == 16:
            converted_int = hex(integer_part)[2:].upper()
        else:
            converted_int = str(integer_part)
        
        # Parte fracionária
        fractional = decimal - integer_part
        if fractional > 0:
            converted_frac = []
            for _ in range(4):  # 4 casas decimais
                fractional *= current_base
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
        n1 = to_decimal(num1)
        n2 = to_decimal(num2)
        
        if operation == "Adição":
            result = n1 + n2
        elif operation == "Subtração":
            result = n1 - n2
        elif operation == "Multiplicação":
            result = n1 * n2
        elif operation == "Divisão":
            if n2 == 0:
                return "Erro: Não é possível a divisão por zero"
            result = n1 / n2
        else:
            return "Operação inválida"
        
        return from_decimal(result)
    except Exception as e:
        return f"Erro: {str(e)}"

# Interface principal
with st.container():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1>HERMES CONVERTER</h1>
        <p style="color: #00ffff; font-family: 'Rajdhani'; font-size: 1.1rem;">
            Ferramenta avançada de conversão e operação em várias bases
        </p>
    </div>
    """, unsafe_allow_html=True)

tabs = st.tabs(["🔁 CONVERSOR", "➕ OPERAÇÕES", "ℹ️ SOBRE"])

# --- Conversor ---
with tabs[0]:
    with st.container():
        st.markdown("""
        <div class="neon-card">
            <h2>CONVERSOR DE BASE</h2>
            <h4>Binária, Decimal, Octal e Hexadecimal</h4>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            value = st.text_input("Número:", placeholder="Ex: 101.01, 12.3A, 77.12", key="conv_value")
        with col2:
            base_from = st.selectbox("Base:", ["Binário", "Decimal", "Octal", "Hexadecimal"], key="conv_from")
        
        base_to = st.selectbox("Base à converter:", ["Binário", "Decimal", "Octal", "Hexadecimal"], key="conv_to")

        if st.button("CONVERTER", key="conv_btn"):
            with st.spinner('Converting...'):
                time.sleep(0.3)
                result = convert_number(value, base_from, base_to)
                if result.startswith("Erro:"):
                    st.error(result)
                else:
                    st.success(f"**Result:** `{result}`")
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- Operações ---
with tabs[1]:
    with st.container():
        st.markdown("""
        <div class="neon-card">
            <h2>OPERAÇÕES MATEMÁTICAS EM VÁRIAS BASES</h2>
        """, unsafe_allow_html=True)
        
        base = st.selectbox("BASE:", ["Binário", "Decimal", "Octal", "Hexadecimal"], key="op_base")
        
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.text_input("NÚMERO 1:", key="op_num1")
        with col2:
            num2 = st.text_input("NÚMERO 2:", key="op_num2")
        
        operation = st.radio("OPERATION:", ["Adição", "Subtração", "Multiplicação", "Divisão"], 
                           horizontal=True, key="op_type")

        if st.button("CALCULAR", key="op_btn"):
            with st.spinner('Calculando...'):
                time.sleep(0.3)
                result = perform_operation(num1, num2, operation, base)
                if result.startswith("Erro:"):
                    st.error(result)
                else:
                    st.success(f"**Resultado:** `{result}`")
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- Sobre ---
with tabs[2]:
    with st.container():
        st.markdown("""
        <div class="neon-card">
        
             <div style="margin-top: 1.5rem;">
                <h3 style="color: #00ffff; border-bottom: 1px solid #00ffff; padding-bottom: 0.5rem;">
                    SOBRE O APP
                </h3>
                <ul style="color: #aaa; list-style-type: none; padding-left: 0;">
                    O HERMES Converter é uma ferramenta avançada de conversão entre sistemas numéricos com design cyberpunk neon. Oferece:

Conversão entre binário, decimal, octal e hexadecimal

Operações matemáticas em qualquer base

Interface futurista com efeitos visuais impressionantes

Dark mode automático

🛠 Tecnologias Utilizadas
Python (Linguagem principal)

Streamlit (Framework para interface web)

HTML/CSS/JS (Efeitos visuais personalizados)

Particles.js (Efeito de partículas interativo)
                </ul>
            </div>
            <div style="margin-top: 1.5rem;">
                <h3 style="color: #00ffff; border-bottom: 1px solid #00ffff; padding-bottom: 0.5rem;">
                    EQUIPA
                </h3>
                <ul style="color: #aaa; list-style-type: none; padding-left: 0;">
                    <li>► Marcolino Lemos -> DEV BACK-END E CTO</li>
                    <li>► Loid Padre -> DEV BACK-END E CEO</li>
                    <li>► Zeferino Fulano -> DEV FRONT-END E COO</li>
                    <li>► Mikhail Freire -> DEV FRONT-END E CMO</li>
                </ul>
            </div>
            
        
        

        """, unsafe_allow_html=True)


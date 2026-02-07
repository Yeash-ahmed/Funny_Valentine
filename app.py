import streamlit as st

st.set_page_config(page_title="Valentine 💘", layout="centered")

# ---------------- STATE ----------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ---------------- CSS + JS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0f14, #1a1a24);
}

.title {
    text-align: center;
    font-size: 30px;
    font-weight: 700;
    color: #ff4d6d;
    margin-top: 20px;
}

.heart {
    text-align: center;
    font-size: 60px;
    margin-top: 10px;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-top: 50px;
}

button {
    padding: 16px 30px;
    font-size: 18px;
    border-radius: 16px;
    border: none;
}

#yes-btn {
    background: #ff4d6d;
    color: white;
}

#no-btn {
    background: #495057;
    color: white;
    position: fixed;
}
</style>

<script>
function moveButton() {
    const btn = document.getElementById("no-btn");
    const maxX = window.innerWidth - btn.offsetWidth - 20;
    const maxY = window.innerHeight - btn.offsetHeight - 20;

    const x = Math.random() * maxX;
    const y = Math.random() * maxY;

    btn.style.left = x + "px";
    btn.style.top = y + "px";
}

function playMusic() {
    const audio = document.getElementById("bg-music");
    if (audio) audio.play();
}
</script>
""", unsafe_allow_html=True)

# ---------------- MUSIC ----------------
st.markdown("""
<audio id="bg-music" loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# ---------------- MAIN SCREEN ----------------
if not st.session_state.accepted:
    st.markdown("<div class='heart'>💘</div>", unsafe_allow_html=True)
    st.markdown("<div class='title'>Will you be my Valentine? 🥺💖</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="buttons">
        <a href="?yes=true">
            <button id="yes-btn" onclick="playMusic()">YES 💕</button>
        </a>

        <button id="no-btn"
            ontouchstart="moveButton()"
            onpointerdown="moveButton()"
            onclick="moveButton()">
            NO 😝
        </button>
    </div>
    """, unsafe_allow_html=True)

    # ✅ NEW API (NO WARNING)
    if st.query_params.get("yes") == "true":
        st.session_state.accepted = True
        st.query_params.clear()

# ---------------- AFTER YES ----------------
else:
    st.balloons()
    st.markdown("<div class='heart'>💞💞💞</div>", unsafe_allow_html=True)
    st.markdown("<div class='title'>YAYYYY 💖🥰</div>", unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align:center; font-size:18px; color:#ffc2d1;">
    You are officially my Valentine 😌🌹<br><br>
    🍫 Chocolates × Infinity<br>
    🤗 Hugs × Lifetime<br>
    😂 Memes × Daily
    </p>
    """, unsafe_allow_html=True)

    st.image(
        "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
        use_container_width=True
    )
import streamlit as st
from pathlib import Path
import base64

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="ANUDIP COE INDUSTRIAL VISIT",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Gallery data
# ------------------------------------------------------------
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

photos = [
    ("photo_01.jpeg", "Departure & Team Journey"),
    ("photo_02.jpeg", "Learning Together"),
    ("photo_03.jpeg", "Arrival at the Visit Location"),
    ("photo_04.jpeg", "Group Moments"),
    ("photo_05.jpeg", "Lunch & Conversations"),
    ("photo_06.jpeg", "Journey Back Together"),
    ("photo_07.jpeg", "TATA Communications Visit"),
    ("photo_08.jpeg", "Industry Interaction"),
    ("photo_09.jpeg", "Knowledge Sharing Session"),
    ("photo_10.jpeg", "Team Discussion"),
    ("photo_11.jpeg", "Interactive Session"),
    ("photo_12.jpeg", "Collaborative Learning"),
    ("photo_13.jpeg", "People & Connections"),
    ("photo_14.jpeg", "Memorable Moments"),
]

# ------------------------------------------------------------
# Custom CSS
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(0, 184, 148, 0.13), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(52, 152, 219, 0.13), transparent 30%),
            #f7fafc;
    }

    /* Hide Streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hero */
    .hero {
        padding: 42px 28px 36px;
        border-radius: 28px;
        text-align: center;
        color: white;
        background:
            linear-gradient(135deg, #073b4c 0%, #0b6e69 45%, #118ab2 100%);
        box-shadow: 0 18px 50px rgba(7, 59, 76, 0.25);
        margin-bottom: 25px;
        overflow: hidden;
        position: relative;
    }

    .hero:before {
        content: "";
        position: absolute;
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: rgba(255,255,255,0.07);
        top: -110px;
        left: -80px;
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: rgba(255,255,255,0.06);
        bottom: -170px;
        right: -100px;
    }

    .hero h1 {
        position: relative;
        z-index: 1;
        font-size: clamp(1.8rem, 4vw, 3.3rem);
        margin: 0;
        font-weight: 800;
        letter-spacing: -1px;
    }

    .hero p {
        position: relative;
        z-index: 1;
        font-size: 1.15rem;
        margin: 12px 0 0;
        opacity: 0.94;
    }

    .badge-row {
        position: relative;
        z-index: 1;
        margin-top: 20px;
    }

    .badge {
        display: inline-block;
        padding: 8px 15px;
        margin: 4px;
        border: 1px solid rgba(255,255,255,0.28);
        border-radius: 999px;
        background: rgba(255,255,255,0.12);
        font-size: 0.9rem;
    }

    /* Section heading */
    .section-title {
        text-align: center;
        margin: 32px 0 8px;
        color: #073b4c;
        font-size: 1.8rem;
        font-weight: 800;
    }

    .section-subtitle {
        text-align: center;
        color: #607d8b;
        margin-bottom: 22px;
    }

    /* Image cards */
    div[data-testid="stImage"] {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 7px 24px rgba(0,0,0,0.10);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        background: white;
        margin-bottom: 8px;
    }

    div[data-testid="stImage"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 15px 34px rgba(0,0,0,0.18);
    }

    /* Caption text */
    .photo-caption {
        text-align: center;
        color: #29434e;
        font-weight: 650;
        font-size: 0.92rem;
        margin: 4px 0 24px;
    }

    /* Info cards */
    .info-card {
        background: rgba(255,255,255,0.90);
        border: 1px solid rgba(7,59,76,0.08);
        border-radius: 18px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }

    .info-card .icon {
        font-size: 1.7rem;
    }

    .info-card h3 {
        margin: 7px 0 5px;
        color: #073b4c;
        font-size: 1.08rem;
    }

    .info-card p {
        color: #607d8b;
        margin: 0;
        line-height: 1.55;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 22px;
        color: #607d8b;
        border-top: 1px solid rgba(7,59,76,0.10);
    }

    /* Mobile */
    @media (max-width: 700px) {
        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }
        .hero {
            padding: 30px 18px;
            border-radius: 20px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Hero section
# ------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>📸 ANUDIP COE INDUSTRIAL VISIT</h1>
        <p>to TATA Communication</p>
        <div class="badge-row">
            <span class="badge">📅 23rd September, 2026</span>
            <span class="badge">📍 Kolkata, West Bengal</span>
            <span class="badge">👥 Learning • Interaction • Teamwork</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Highlights
# ------------------------------------------------------------
st.markdown('<div class="section-title">✨ Visit Highlights</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A visual journey of learning, collaboration and memorable moments.</div>',
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("🏢", "Industry Visit", "An opportunity to experience a professional technology environment."),
    ("💡", "Knowledge Sharing", "Interactive discussions, questions and practical insights."),
    ("🤝", "Team Connection", "Students, mentors and professionals learning together."),
    ("📸", "Memories", "A collection of moments from the complete visit."),
]

for col, (icon, title, text) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# Gallery controls
# ------------------------------------------------------------
st.markdown('<div class="section-title">🖼️ Photo Gallery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">All photographs from the ANUDIP COE Industrial Visit.</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1])
with left:
    view_mode = st.radio(
        "Gallery layout",
        ["Grid", "Large View"],
        horizontal=True,
        label_visibility="collapsed",
    )

with right:
    columns_count = st.selectbox(
        "Photos per row",
        [2, 3, 4],
        index=2,
        label_visibility="collapsed",
    )

# ------------------------------------------------------------
# Render gallery
# ------------------------------------------------------------
existing_photos = [
    (filename, caption)
    for filename, caption in photos
    if (IMAGE_DIR / filename).exists()
]

if view_mode == "Grid":
    for start in range(0, len(existing_photos), columns_count):
        row = existing_photos[start:start + columns_count]
        cols = st.columns(columns_count, gap="medium")

        for col, (filename, caption) in zip(cols, row):
            with col:
                st.image(
                    str(IMAGE_DIR / filename),
                    use_container_width=True,
                )
                st.markdown(
                    f'<div class="photo-caption">{caption}</div>',
                    unsafe_allow_html=True,
                )
else:
    # Large view: one image at a time with a selector.
    names = [caption for _, caption in existing_photos]
    selected_caption = st.selectbox(
        "Choose a photograph",
        names,
        label_visibility="collapsed",
    )
    selected_file = next(
        filename for filename, caption in existing_photos
        if caption == selected_caption
    )
    st.image(
        str(IMAGE_DIR / selected_file),
        use_container_width=True,
        caption=selected_caption,
    )

# ------------------------------------------------------------
# Visit story
# ------------------------------------------------------------
st.markdown('<div class="section-title">🌟 The Visit in Moments</div>', unsafe_allow_html=True)

story_cols = st.columns(3)
story = [
    ("🚌", "Journey", "The day began with the group travelling together and building excitement for the industrial visit."),
    ("🏢", "Industry Exposure", "The group experienced a professional workplace environment and participated in interactive sessions."),
    ("🍽️", "Memories", "Conversations, lunch, photographs and teamwork made the day memorable for everyone."),
]

for col, (icon, title, text) in zip(story_cols, story):
    with col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <strong>ANUDIP COE INDUSTRIAL VISIT</strong><br>
        TATA Communication • Kolkata • 23rd September 2026<br><br>
        Made with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)

"""
AI Learning & Study Assistant - Premium Quality Edition
Featuring:
- Typography: Outfit (Display & Headings) + Plus Jakarta Sans (Interface & Body) + JetBrains Mono (Code/Citations)
- Glassmorphism & Aurora Gradients
- 🏠 Dashboard Cockpit with KPI Metrics & Instant Document Inspector
- 📚 Study Materials: PDF ingestion, chunking, FAISS vector index
- 💬 Ask AI: Strict RAG with expandable citations & autonomous tool agent
- 📝 Practice Quiz: Gamified MCQ practice with instant grading & weak-area diagnosis
- 📊 Progress & Memory: Long-term mastery tracker with direct 1-click weak-topic drills
- 📅 Study Planner: Day-by-day exam schedules with active recall allocations & export
"""

import os
import time
from datetime import date, timedelta
from pathlib import Path
import streamlit as st

# Configure page
st.set_page_config(
    page_title="StudyAI • Intelligent Student Workspace",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Design System (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    :root {
        --font-display: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
        --primary: #4F46E5;
        --primary-glow: rgba(79, 70, 229, 0.25);
        --accent: #06B6D4;
        --surface: #FFFFFF;
        --surface-subtle: #F8FAFC;
        --border: #E2E8F0;
        --border-focus: #818CF8;
    }

    html, body, [class*="css"] {
        font-family: var(--font-body);
        color: #0F172A;
        letter-spacing: -0.011em;
    }

    h1, h2, h3, .hero-title, .brand-text, .score-big {
        font-family: var(--font-display) !important;
        letter-spacing: -0.025em;
    }

    code, pre, .mono-badge {
        font-family: var(--font-mono) !important;
    }

    /* Page Container */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3.5rem;
        max-width: 1260px;
    }

    /* Modern Aurora Hero Banner */
    .hero-banner {
        background: radial-gradient(100% 120% at 80% 0%, #312E81 0%, #1E1B4B 45%, #0F172A 100%);
        border-radius: 24px;
        padding: 2.5rem 2.8rem;
        color: #FFFFFF;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px -15px rgba(15, 23, 42, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.08);
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: "";
        position: absolute;
        top: -80px;
        right: -80px;
        width: 320px;
        height: 320px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.35) 0%, rgba(99, 102, 241, 0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-banner::after {
        content: "";
        position: absolute;
        bottom: -60px;
        left: 20%;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(6, 182, 212, 0.2) 0%, rgba(6, 182, 212, 0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 0.3rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #E0E7FF;
        margin-bottom: 0.9rem;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1.15;
        margin: 0;
        background: linear-gradient(135deg, #FFFFFF 60%, #C7D2FE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #CBD5E1;
        margin-top: 0.65rem;
        margin-bottom: 1.2rem;
        font-weight: 400;
        max-width: 680px;
        line-height: 1.5;
    }
    .hero-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
    }
    .hero-tag {
        font-size: 0.76rem;
        font-weight: 600;
        color: #94A3B8;
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 0.25rem 0.65rem;
        border-radius: 6px;
    }

    /* KPI Stat Cards with Double-Border Depth */
    .kpi-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.1rem;
        margin-bottom: 2rem;
    }
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.35rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02), 0 10px 24px -4px rgba(15, 23, 42, 0.04), inset 0 1px 0 rgba(255, 255, 255, 0.9);
        display: flex;
        align-items: center;
        gap: 1.2rem;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px -4px rgba(79, 70, 229, 0.12);
        border-color: #CBD5E1;
    }
    .kpi-icon-wrap {
        width: 52px;
        height: 52px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        flex-shrink: 0;
    }
    .kpi-icon-indigo { background: #EEF2FF; color: #4F46E5; box-shadow: 0 2px 8px rgba(79, 70, 229, 0.15); }
    .kpi-icon-emerald { background: #ECFDF5; color: #059669; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15); }
    .kpi-icon-amber { background: #FFFBEB; color: #D97706; box-shadow: 0 2px 8px rgba(245, 158, 11, 0.15); }
    .kpi-icon-rose { background: #FFF1F2; color: #E11D48; box-shadow: 0 2px 8px rgba(225, 29, 72, 0.15); }

    .kpi-val {
        font-family: var(--font-display);
        font-size: 1.85rem;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.1;
        letter-spacing: -0.03em;
    }
    .kpi-lbl {
        font-size: 0.8rem;
        font-weight: 600;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-top: 0.25rem;
    }

    /* Action Tiles (Launchpad) */
    .action-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.4rem;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }
    .action-card:hover {
        border-color: #6366F1;
        box-shadow: 0 12px 28px -4px rgba(99, 102, 241, 0.16);
        transform: translateY(-3px);
    }
    .action-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-family: var(--font-display);
        font-weight: 700;
        font-size: 1.1rem;
        color: #0F172A;
        margin-bottom: 0.45rem;
    }
    .action-desc {
        font-size: 0.88rem;
        color: #64748B;
        line-height: 1.5;
        margin-bottom: 1.1rem;
    }

    /* Status Pill Badges with Pulse Animation */
    @keyframes live-pulse {
        0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); }
        70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
        100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    .pulse-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #10B981;
        animation: live-pulse 2s infinite;
    }
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .pill-ready { background: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; }
    .pill-empty { background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }
    .pill-tool { 
        background: #EEF2FF; 
        color: #3730A3; 
        border: 1px solid #C7D2FE; 
        font-family: var(--font-mono); 
        font-size: 0.75rem; 
    }

    /* Modern Card */
    .modern-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.6rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02), 0 8px 24px -4px rgba(15, 23, 42, 0.04);
        margin-bottom: 1.3rem;
    }

    /* Citation & Sources Box */
    .source-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #4F46E5;
        border-radius: 0 14px 14px 0;
        padding: 1rem 1.3rem;
        margin-top: 0.7rem;
        font-size: 0.88rem;
        line-height: 1.55;
    }
    .source-meta {
        font-weight: 600;
        color: #334155;
        display: flex;
        gap: 0.8rem;
        align-items: center;
        margin-bottom: 0.45rem;
        font-size: 0.82rem;
    }
    .source-snippet {
        color: #475569;
        font-style: italic;
        background: #FFFFFF;
        padding: 0.7rem 0.9rem;
        border-radius: 10px;
        border: 1px dashed #CBD5E1;
    }

    /* Quiz Card UI */
    .quiz-question-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #4F46E5;
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin-bottom: 1.3rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
    }
    .quiz-q-num {
        display: inline-block;
        background: #EEF2FF;
        color: #4338CA;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 0.25rem 0.7rem;
        border-radius: 8px;
        margin-bottom: 0.7rem;
        font-family: var(--font-display);
        letter-spacing: 0.02em;
    }
    .quiz-q-text {
        font-family: var(--font-display);
        font-size: 1.15rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.4;
        margin-bottom: 0.85rem;
    }

    /* Score Hero Result */
    .score-hero {
        background: radial-gradient(100% 120% at 50% 0%, #312E81 0%, #1E1B4B 60%, #0F172A 100%);
        color: #FFFFFF;
        border-radius: 20px;
        padding: 2.4rem;
        text-align: center;
        margin-bottom: 1.8rem;
        box-shadow: 0 16px 36px -10px rgba(30, 27, 75, 0.35);
    }
    .score-big {
        font-family: var(--font-display);
        font-size: 4rem;
        font-weight: 900;
        line-height: 1;
        letter-spacing: -0.05em;
        background: linear-gradient(135deg, #38BDF8 0%, #818CF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .score-badge {
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 0.75rem;
        color: #E2E8F0;
        font-family: var(--font-display);
    }

    /* Custom Streamlit Form Elements */
    .stButton > button {
        border-radius: 12px !important;
        font-family: var(--font-display) !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.1rem !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        letter-spacing: -0.01em !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px -2px rgba(79, 70, 229, 0.25);
    }

    /* Sidebar Navigation Aesthetic */
    section[data-testid="stSidebar"] {
        background-color: #FAFAFA;
        border-right: 1px solid #E5E7EB;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Application Modules
import config
import rag
import quiz
import memory
import study_plan
import tools

# Session State Initialization
if "nav_choice" not in st.session_state:
    st.session_state.nav_choice = "🏠 Dashboard"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = None
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = None
if "quiz_topic" not in st.session_state:
    st.session_state.quiz_topic = ""
if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = None

# Quick navigation helper function
def set_nav(destination: str, topic: str = None):
    st.session_state.nav_choice = destination
    if topic:
        st.session_state.quiz_topic = topic
    st.rerun()

# System Snapshot
v_status = rag.get_vector_store_status()
mem_summary = memory.get_progress_summary()

# ==========================================
# SIDEBAR NAVIGATION & TELEMETRY
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 0.85rem; margin-bottom: 0.6rem;">
        <div style="width: 44px; height: 44px; border-radius: 12px; background: linear-gradient(135deg, #4F46E5, #7C3AED); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);">
            🎓
        </div>
        <div>
            <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 1.35rem; color: #0F172A; line-height: 1.1;">StudyAI</div>
            <div style="font-size: 0.78rem; color: #64748B; font-weight: 500;">Intelligent Learning Assistant</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    nav_options = [
        "🏠 Dashboard",
        "📚 Study Materials",
        "💬 Ask AI",
        "📝 Practice Quiz",
        "📊 Progress & Memory",
        "📅 Study Planner"
    ]

    current_idx = nav_options.index(st.session_state.nav_choice) if st.session_state.nav_choice in nav_options else 0

    selected_nav = st.radio(
        "Navigation",
        nav_options,
        index=current_idx,
        label_visibility="collapsed"
    )
    if selected_nav != st.session_state.nav_choice:
        st.session_state.nav_choice = selected_nav
        st.rerun()

    st.markdown("---")
    st.markdown("<div style='font-size: 0.82rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.6rem;'>System Telemetry</div>", unsafe_allow_html=True)

    # Telemetry Status
    if config.is_gemini_configured():
        st.markdown(f'''
        <div class="status-pill pill-ready">
            <span class="pulse-dot"></span>
            <span>Gemini AI ({config.GEMINI_MODEL_NAME})</span>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill pill-empty">⚠️ Gemini Key Missing</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 6px'></div>", unsafe_allow_html=True)

    if v_status["is_ready"]:
        st.markdown(f'''
        <div class="status-pill pill-ready">
            <span class="pulse-dot"></span>
            <span>FAISS Store: {v_status["total_chunks"]} chunks</span>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill pill-empty">○ No PDF Indexed</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 14px'></div>", unsafe_allow_html=True)
    st.caption("🔒 Dense vector indexing and progress memory run securely on your local workstation.")


# ==========================================
# GLOBAL HERO BANNER
# ==========================================
st.markdown("""
<div class="hero-banner">
    <div class="hero-badge">
        <span>✨</span> Next-Gen Retrieval-Augmented Learning Companion
    </div>
    <div class="hero-title">Master Any Subject with Grounded AI</div>
    <div class="hero-subtitle">
        Upload your lecture slides, notes, or textbooks. Study with strict citation-backed answers, 
        adaptive practice tests, and structured day-by-day exam schedules.
    </div>
    <div class="hero-tags">
        <span class="hero-tag">⚡ Strict Grounded RAG</span>
        <span class="hero-tag">🎯 Adaptive MCQ Generator</span>
        <span class="hero-tag">🧠 Persistent Student Memory</span>
        <span class="hero-tag">📅 Automated Study Timetable</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 1. 🏠 DASHBOARD (High-level cockpit)
# ==========================================
if st.session_state.nav_choice == "🏠 Dashboard":
    # Top KPI Metrics Row
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-indigo">📚</div>
            <div>
                <div class="kpi-val">{len(v_status["indexed_files"])}</div>
                <div class="kpi-lbl">Indexed Materials</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-emerald">💬</div>
            <div>
                <div class="kpi-val">{mem_summary["total_questions_asked"]}</div>
                <div class="kpi-lbl">Questions Solved</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-amber">📝</div>
            <div>
                <div class="kpi-val">{mem_summary["total_quizzes_taken"]}</div>
                <div class="kpi-lbl">Quizzes Taken</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-rose">🎯</div>
            <div>
                <div class="kpi-val">{mem_summary["average_quiz_score"]}%</div>
                <div class="kpi-lbl">Mastery Score</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Launchpad Cards
    st.markdown("### 🚀 Study Launchpad")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="action-card">
            <div>
                <div class="action-header">📚 Upload Notes</div>
                <div class="action-desc">Ingest PDFs, extract clean text, and generate local FAISS vector embeddings.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Manage Notes →", key="act_upload", use_container_width=True):
            set_nav("📚 Study Materials")

    with col2:
        st.markdown("""
        <div class="action-card">
            <div>
                <div class="action-header">💬 Ask AI</div>
                <div class="action-desc">Ask specific questions with exact file and page citations from your course material.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Asking →", key="act_ask", use_container_width=True):
            set_nav("💬 Ask AI")

    with col3:
        st.markdown("""
        <div class="action-card">
            <div>
                <div class="action-header">📝 Take Quiz</div>
                <div class="action-desc">Generate an interactive practice exam with instant grading and explanations.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Quiz →", key="act_quiz", use_container_width=True):
            set_nav("📝 Practice Quiz")

    with col4:
        st.markdown("""
        <div class="action-card">
            <div>
                <div class="action-header">📅 Exam Plan</div>
                <div class="action-desc">Create a customized day-by-day exam roadmap tailored to your deadline.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Build Schedule →", key="act_plan", use_container_width=True):
            set_nav("📅 Study Planner")

    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)

    # Dashboard Split Row: Focus Topics & Quick Search Inspector
    d_col1, d_col2 = st.columns([1, 1])

    with d_col1:
        st.markdown("#### 🎯 Focus Areas & Weak Topics")
        if mem_summary["weak_topics"]:
            st.warning(f"**Action Required:** {len(mem_summary['weak_topics'])} topic(s) scored below 70% in recent quizzes.")
            for wt in mem_summary["weak_topics"]:
                c_t1, c_t2 = st.columns([3, 1])
                with c_t1:
                    st.markdown(f"🔴 **{wt}**")
                with c_t2:
                    if st.button("⚡ Drill", key=f"drill_{wt}", use_container_width=True):
                        set_nav("📝 Practice Quiz", topic=wt)
        else:
            st.success("🎉 Great job! No weak topics currently flagged. Take a quiz to test your comprehension.")

        st.markdown("#### 📚 Active Course Topics")
        if mem_summary["topics_studied"]:
            topics_html = " ".join([f"<span class='status-pill pill-tool' style='margin: 3px;'>📘 {t}</span>" for t in mem_summary["topics_studied"]])
            st.markdown(topics_html, unsafe_allow_html=True)
        else:
            st.info("No course materials indexed yet. Upload notes to begin.")

    with d_col2:
        st.markdown("#### 🔎 Instant Document Recall Inspector")
        st.write("Test semantic retrieval against your indexed materials:")
        test_query = st.text_input("Enter a concept or query to inspect top chunks:", placeholder="e.g. What is virtualization?", label_visibility="collapsed")
        if test_query:
            results = rag.search_study_material(test_query, top_k=2)
            if results:
                for r in results:
                    st.markdown(f"""
                    <div class="source-box">
                        <div class="source-meta">
                            <span>📄 <b>{r['file_name']}</b></span>
                            <span>• Page {r['page']}</span>
                            <span>• Relevance: <b>{r['score']:.3f}</b></span>
                        </div>
                        <div class="source-snippet">"{r['text'][:180]}..."</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No matching chunks found in the current vector store.")


# ==========================================
# 2. 📚 STUDY MATERIALS (Upload & Ingestion)
# ==========================================
elif st.session_state.nav_choice == "📚 Study Materials":
    st.markdown("### 📚 Study Materials Library")
    st.write("Upload course slides, textbooks, or notes in PDF format. We extract the content, generate dense semantic embeddings, and store them in a local FAISS index.")

    col1, col2 = st.columns([1.8, 1.2])

    with col1:
        st.markdown("#### 📤 Upload Documents")
        uploaded_files = st.file_uploader(
            "Select one or more PDF files",
            type=["pdf"],
            accept_multiple_files=True,
            help="Supports lecture slides, chapters, and study handouts."
        )

        if uploaded_files:
            st.info(f"📁 **{len(uploaded_files)}** file(s) selected.")
            process_btn = st.button("🚀 Process & Index Materials", type="primary", use_container_width=True)

            if process_btn:
                for uploaded_file in uploaded_files:
                    file_path = config.UPLOADS_DIR / uploaded_file.name
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    with st.spinner(f"Extracting, chunking & embedding '{uploaded_file.name}'..."):
                        try:
                            result = rag.process_and_index_pdf(file_path, uploaded_file.name)
                            st.success(f"✅ Successfully indexed **{result['file_name']}**")

                            m_c1, m_c2, m_c3 = st.columns(3)
                            with m_c1:
                                st.metric("Pages Extracted", result["total_pages"])
                            with m_c2:
                                st.metric("Chunks Generated", result["total_chunks"])
                            with m_c3:
                                st.metric("Total Store Chunks", result["total_index_size"])

                        except ValueError as ve:
                            st.error(f"⚠️ {ve}")
                        except Exception as ex:
                            st.error(f"❌ Error indexing '{uploaded_file.name}': {ex}")

    with col2:
        st.markdown("#### 📑 Vector Store Index")
        status = rag.get_vector_store_status()

        if status["is_ready"]:
            st.markdown(f"""
            <div class="modern-card">
                <div style="font-weight: 700; color: #047857; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span class="pulse-dot"></span> FAISS Vector Index Active
                </div>
                <div style="font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 800; color: #0F172A;">{status['total_chunks']}</div>
                <div style="font-size: 0.8rem; color: #64748B; text-transform: uppercase; font-weight: 600; margin-bottom: 1.1rem;">Searchable Chunks</div>
                <div style="font-weight: 600; font-size: 0.9rem; color: #334155; margin-bottom: 0.4rem;">Indexed Files:</div>
                <ul style="padding-left: 1.2rem; margin: 0; font-size: 0.88rem; color: #475569;">
                    {''.join([f"<li><code>{fn}</code></li>" for fn in status['indexed_files']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🗑️ Clear Vector Index", help="Delete stored embeddings to start fresh"):
                rag.clear_vector_store()
                st.success("Vector store cleared.")
                st.rerun()
        else:
            st.warning("⚠️ No materials indexed yet.\n\nUpload a PDF file to enable grounded RAG answering and quiz generation.")


# ==========================================
# 3. 💬 ASK AI (Direct RAG & Agent Mode)
# ==========================================
elif st.session_state.nav_choice == "💬 Ask AI":
    st.markdown("### 💬 Ask Questions on Your Materials")

    c_m1, c_m2 = st.columns([2.5, 1])
    with c_m1:
        interaction_mode = st.radio(
            "Answering Strategy",
            ["Direct Study Q&A (Strict RAG)", "Autonomous AI Agent (Intent Router)"],
            horizontal=True,
            help="Direct RAG answers strictly with document citations; Autonomous Agent executes quizzes, memory checks, or study plans."
        )
    with c_m2:
        if st.button("🧹 Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    # Suggestion Chips
    st.markdown("<div style='font-size: 0.82rem; font-weight: 600; color: #64748B; margin-bottom: 0.4rem;'>💡 Quick Suggestions:</div>", unsafe_allow_html=True)
    chip_col1, chip_col2, chip_col3 = st.columns(3)
    quick_query = None

    with chip_col1:
        if st.button("📌 Summarize core concepts", key="qp1", use_container_width=True):
            quick_query = "What are the core concepts and summaries covered in this material?"
    with chip_col2:
        if st.button("📝 Test me on this material", key="qp2", use_container_width=True):
            quick_query = "Give me a practice quiz on this topic"
    with chip_col3:
        if st.button("📅 Plan my exam review", key="qp3", use_container_width=True):
            quick_query = "Create a study plan for this course"

    st.markdown("---")

    # Render History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            if msg.get("tool"):
                st.markdown(f'<span class="status-pill pill-tool">Tool: {msg["tool"]}</span>', unsafe_allow_html=True)
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander(f"🔍 View Sources & Citations ({len(msg['sources'])} snippets)", expanded=False):
                    for src in msg["sources"]:
                        st.markdown(f"""
                        <div class="source-box">
                            <div class="source-meta">
                                <span>📄 <b>{src['file_name']}</b></span>
                                <span>• Page {src['page']}</span>
                                <span>• Relevance: <b>{src['score']}</b></span>
                            </div>
                            <div class="source-snippet">"{src['snippet']}"</div>
                        </div>
                        """, unsafe_allow_html=True)

    user_input = st.chat_input("Ask any question regarding your study materials...")
    prompt_to_run = quick_query if quick_query else user_input

    if prompt_to_run:
        if not config.is_gemini_configured():
            st.error("⚠️ AI assistant service is not configured. Please ensure GEMINI_API_KEY is set in your .env file.")
            st.stop()

        st.session_state.chat_history.append({"role": "user", "content": prompt_to_run})
        with st.chat_message("user"):
            st.markdown(prompt_to_run)

        with st.chat_message("assistant"):
            with st.spinner("Searching document context and formulating grounded answer..."):
                try:
                    if interaction_mode == "Autonomous AI Agent (Intent Router)":
                        res = tools.route_and_execute(prompt_to_run)
                        st.markdown(f'<span class="status-pill pill-tool">Tool: {res["tool_selected"]}</span>', unsafe_allow_html=True)
                        st.markdown(res["response"])
                        if res.get("sources"):
                            with st.expander(f"🔍 Citations ({len(res['sources'])} snippets)", expanded=False):
                                for src in res["sources"]:
                                    st.markdown(f"""
                                    <div class="source-box">
                                        <div class="source-meta">
                                            <span>📄 <b>{src['file_name']}</b></span>
                                            <span>• Page {src['page']}</span>
                                            <span>• Score: <b>{src['score']}</b></span>
                                        </div>
                                        <div class="source-snippet">"{src['snippet']}"</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": res["response"],
                            "tool": res["tool_selected"],
                            "sources": res.get("sources", [])
                        })
                    else:
                        rag_out = rag.answer_question(prompt_to_run)
                        st.markdown(rag_out["answer"])
                        if rag_out.get("sources"):
                            with st.expander(f"🔍 Citations ({len(rag_out['sources'])} snippets)", expanded=True):
                                for src in rag_out["sources"]:
                                    st.markdown(f"""
                                    <div class="source-box">
                                        <div class="source-meta">
                                            <span>📄 <b>{src['file_name']}</b></span>
                                            <span>• Page {src['page']}</span>
                                            <span>• Similarity: <b>{src['score']}</b></span>
                                        </div>
                                        <div class="source-snippet">"{src['snippet']}"</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": rag_out["answer"],
                            "sources": rag_out.get("sources", [])
                        })
                except Exception as err:
                    st.error(f"❌ Processing error: {err}")


# ==========================================
# 4. 📝 PRACTICE QUIZ (Interactive Test)
# ==========================================
elif st.session_state.nav_choice == "📝 Practice Quiz":
    st.markdown("### 📝 Interactive Practice Quiz")
    st.write("Generate adaptive multiple choice tests tailored to your materials. Scores and weak areas update directly to your student profile.")

    default_quiz_topic = st.session_state.quiz_topic or (mem_summary["topics_studied"][-1] if mem_summary["topics_studied"] else "Cloud Computing")

    with st.expander("⚙️ Quiz Parameters", expanded=(st.session_state.current_quiz is None)):
        q_c1, q_c2, q_c3 = st.columns([2, 1, 1])
        with q_c1:
            quiz_topic = st.text_input("Quiz Topic / Concept", value=default_quiz_topic, help="Chapter, concept, or specific unit to test.")
        with q_c2:
            num_q = st.selectbox("Number of Questions", [5, 10], index=0)
        with q_c3:
            difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"], index=1)

        gen_quiz_btn = st.button("⚡ Generate Practice Test", type="primary", use_container_width=True)

    if gen_quiz_btn:
        if not config.is_gemini_configured():
            st.error("⚠️ AI quiz service is unavailable. Please verify your GEMINI_API_KEY.")
        else:
            with st.spinner(f"Synthesizing {num_q} {difficulty} questions on '{quiz_topic}'..."):
                try:
                    context_chunks = rag.search_study_material(quiz_topic, top_k=3)
                    context_str = "\n\n".join([c["text"] for c in context_chunks]) if context_chunks else ""

                    questions = quiz.generate_quiz_questions(
                        topic=quiz_topic,
                        num_questions=num_q,
                        difficulty=difficulty,
                        context=context_str
                    )
                    st.session_state.current_quiz = questions
                    st.session_state.quiz_answers = {}
                    st.session_state.quiz_results = None
                    st.session_state.quiz_topic = quiz_topic
                    st.success(f"Generated {len(questions)} questions on '{quiz_topic}'!")
                    st.rerun()
                except Exception as ex:
                    st.error(f"Failed to generate quiz: {ex}")

    # Active Test Form
    if st.session_state.current_quiz:
        st.markdown(f"#### ✍️ Examination: **{st.session_state.quiz_topic}** ({len(st.session_state.current_quiz)} Questions)")

        with st.form("quiz_taking_form"):
            for q in st.session_state.current_quiz:
                st.markdown(f"""
                <div class="quiz-question-box">
                    <span class="quiz-q-num">Question {q['id']}</span>
                    <div class="quiz-q-text">{q['question']}</div>
                </div>
                """, unsafe_allow_html=True)

                options_list = [f"{k}. {v}" for k, v in q["options"].items()]
                prev_choice = st.session_state.quiz_answers.get(q["id"], None)
                idx = 0
                if prev_choice:
                    for opt_idx, opt_str in enumerate(options_list):
                        if opt_str.startswith(prev_choice):
                            idx = opt_idx
                            break

                selected = st.radio(
                    f"Select answer for Question {q['id']}:",
                    options_list,
                    index=idx if prev_choice else None,
                    key=f"q_radio_{q['id']}",
                    label_visibility="collapsed"
                )
                if selected:
                    st.session_state.quiz_answers[q["id"]] = selected[0]

                st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)

            submit_quiz = st.form_submit_button("📊 Submit Test & Calculate Score", type="primary", use_container_width=True)

        if submit_quiz:
            with st.spinner("Evaluating responses and recording progress..."):
                results = quiz.calculate_quiz_score(
                    questions=st.session_state.current_quiz,
                    user_answers=st.session_state.quiz_answers,
                    topic=st.session_state.quiz_topic
                )
                st.session_state.quiz_results = results
                st.rerun()

    # Results Breakdown Screen
    if st.session_state.quiz_results:
        res = st.session_state.quiz_results
        st.markdown("---")

        rating = "🌟 Excellent Mastery!" if res['percentage'] >= 80 else ("👍 Solid Comprehension!" if res['percentage'] >= 60 else "⚠️ Needs Active Review")

        st.markdown(f"""
        <div class="score-hero">
            <div class="score-big">{res['score']} / {res['total']}</div>
            <div class="score-badge">{res['percentage']}% • {rating}</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(res['percentage'] / 100.0)

        st.markdown("#### 📋 Detailed Question Review")
        for item in res["details"]:
            if item["is_correct"]:
                st.success(f"""
                ✅ **Question {item['id']}: Correct!**  
                **Question:** {item['question']}  
                **Your Answer:** `{item['selected_option']}` {item['selected_text']}  
                💡 *Explanation:* {item['explanation']}
                """)
            else:
                st.error(f"""
                ❌ **Question {item['id']}: Incorrect**  
                **Question:** {item['question']}  
                **Your Answer:** `{item['selected_option']}` {item['selected_text']}  
                **Correct Answer:** `{item['correct_option']}` {item['correct_text']}  
                💡 *Explanation:* {item['explanation']}
                """)

        if res["weak_areas"]:
            st.warning(f"⚠️ **Targeted Focus Areas:** {', '.join(res['weak_areas'])}")

        st.info("✅ Your quiz results and weak topics have been automatically updated in your **📊 Progress & Memory** dashboard.")


# ==========================================
# 5. 📊 PROGRESS & MEMORY (Analytics)
# ==========================================
elif st.session_state.nav_choice == "📊 Progress & Memory":
    st.markdown("### 📊 Student Learning Memory & Mastery Analytics")
    st.write("Persistent memory tracks every topic studied, quiz taken, and automatically diagnoses concepts needing revision.")

    summary = memory.get_progress_summary()

    # KPI Row
    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-indigo">📚</div>
            <div>
                <div class="kpi-val">{summary["total_topics_studied"]}</div>
                <div class="kpi-lbl">Topics Tracked</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-emerald">💬</div>
            <div>
                <div class="kpi-val">{summary["total_questions_asked"]}</div>
                <div class="kpi-lbl">Questions Asked</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-amber">📝</div>
            <div>
                <div class="kpi-val">{summary["total_quizzes_taken"]}</div>
                <div class="kpi-lbl">Quizzes Taken</div>
            </div>
        </div>
        <div class="kpi-card">
            <div class="kpi-icon-wrap kpi-icon-rose">🎯</div>
            <div>
                <div class="kpi-val">{summary["average_quiz_score"]}%</div>
                <div class="kpi-lbl">Mastery Score</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c_left, c_right = st.columns([1, 1])

    with c_left:
        st.markdown("#### 🎯 Weak Topic Diagnosis")
        if summary["weak_topics"]:
            st.warning(f"The following **{len(summary['weak_topics'])}** topic(s) had quiz scores below 70%:")
            for wt in summary["weak_topics"]:
                wt_col1, wt_col2 = st.columns([3, 1])
                with wt_col1:
                    st.markdown(f"🔴 **{wt}** *(needs practice)*")
                with wt_col2:
                    if st.button("⚡ Practice", key=f"mem_drill_{wt}", use_container_width=True):
                        set_nav("📝 Practice Quiz", topic=wt)
        else:
            st.success("🎉 No weak topics flagged! Your retention is in excellent shape.")

        st.markdown("#### 📚 Mastered & Studied Topics")
        if summary["topics_studied"]:
            for t in summary["topics_studied"]:
                st.markdown(f"- 📘 **{t}**")
        else:
            st.info("No topics recorded yet.")

    with c_right:
        st.markdown("#### 📝 Quiz History")
        if summary["quiz_history"]:
            for qh in reversed(summary["quiz_history"]):
                badge = "🟢 Pass" if qh["percentage"] >= 70 else "🔴 Review"
                with st.expander(f"{badge} | {qh['topic']} ({qh['score']}/{qh['total']} - {qh['percentage']}%)"):
                    st.write(f"📅 **Date:** {qh['timestamp']}")
                    st.write(f"🎯 **Score:** {qh['score']} of {qh['total']} ({qh['percentage']}%)")
                    if qh.get("weak_areas"):
                        st.write(f"⚠️ **Focus Areas:** {', '.join(qh['weak_areas'])}")
        else:
            st.info("No quizzes completed yet. Test yourself in the **📝 Practice Quiz** tab!")

        st.markdown("#### 🕒 Recent Inquiries")
        if summary["recent_questions"]:
            for rq in summary["recent_questions"][:5]:
                st.markdown(f"- 💬 *\"{rq['question']}\"* ({rq.get('topic', 'General')})")
        else:
            st.info("No questions recorded yet.")

    st.markdown("---")
    if st.button("🗑️ Reset All Student Memory", help="Wipes all recorded topics, quiz history, and weak areas"):
        memory.clear_memory()
        st.success("Student memory reset.")
        st.rerun()


# ==========================================
# 6. 📅 STUDY PLANNER (Personalized Schedule)
# ==========================================
elif st.session_state.nav_choice == "📅 Study Planner":
    st.markdown("### 📅 Personalized Day-by-Day Study Planner")
    st.write("Generate an actionable study roadmap based on your exam deadline, daily available hours, and diagnosed weak topics.")

    default_sub = mem_summary["topics_studied"][-1] if mem_summary["topics_studied"] else "Cloud Computing"

    col_p1, col_p2 = st.columns([1, 1])

    with col_p1:
        subject = st.text_input("Course / Subject Name", value=default_sub)
        exam_date = st.date_input("Target Exam Date", value=date.today() + timedelta(days=7), min_value=date.today())
        days_left = (exam_date - date.today()).days
        st.caption(f"⏳ **{days_left} day(s)** remaining until exam.")
        daily_hours = st.slider("Daily Study Hours Available", min_value=1.0, max_value=8.0, value=2.5, step=0.5)

    with col_p2:
        knowledge_level = st.selectbox("Current Knowledge Level", ["Beginner", "Intermediate", "Advanced"], index=1)
        suggested_weak = mem_summary.get("weak_topics", [])
        selected_weak = st.multiselect(
            "Priority Topics to Reinforce",
            options=suggested_weak + ["Core Theory", "Exam Review", "Problem Solving"],
            default=suggested_weak if suggested_weak else []
        )
        custom_focus = st.text_input("Additional Focus Concepts (optional)", placeholder="e.g., Virtualization, System Architecture")
        if custom_focus.strip():
            selected_weak.append(custom_focus.strip())

    gen_plan_btn = st.button("📅 Generate Structured Study Plan", type="primary", use_container_width=True)

    if gen_plan_btn:
        if not config.is_gemini_configured():
            st.error("⚠️ Study plan service is unavailable. Please verify GEMINI_API_KEY.")
        else:
            with st.spinner(f"Generating personalized {days_left}-day study schedule for '{subject}'..."):
                try:
                    plan = study_plan.generate_study_plan(
                        subject=subject,
                        exam_date=str(exam_date),
                        daily_hours=daily_hours,
                        knowledge_level=knowledge_level,
                        weak_topics=selected_weak
                    )
                    st.session_state.generated_plan = plan
                    st.success("Study plan successfully generated!")
                except Exception as ex:
                    st.error(f"Error generating study plan: {ex}")

    if st.session_state.generated_plan:
        plan = st.session_state.generated_plan
        st.markdown("---")
        st.markdown(f"### 📋 Study Roadmap: **{plan['subject']}**")

        c_d1, c_d2, c_d3 = st.columns(3)
        with c_d1:
            st.metric("Days Remaining", plan["days_remaining"])
        with c_d2:
            st.metric("Daily Commitment", f"{plan['daily_hours']} hours")
        with c_d3:
            st.metric("Knowledge Level", plan["knowledge_level"])

        st.markdown(plan["plan_markdown"])

        # Markdown Export Button
        st.download_button(
            label="📥 Export Study Plan (.md)",
            data=plan["plan_markdown"],
            file_name=f"Study_Plan_{plan['subject'].replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )

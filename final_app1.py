# ==========================================================
#              DIGITAL FOOTPRINT VISUALIZER
#     App-Specific Permissions + Weighted Risk Analysis
# ==========================================================
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Digital Footprint Visualizer",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }

    .hero-banner {
        background: radial-gradient(circle at top left, #1e1b4b 0%, #0f172a 60%, #022c22 100%);
        border-radius: 20px; padding: 2.2rem 2.5rem; margin-bottom: 1.2rem;
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 20px 35px -15px rgba(0,0,0,0.45); color: white;
    }
    .hero-tag {
        display: inline-block; background: rgba(16,185,129,0.15); color: #34d399;
        border: 1px solid rgba(52,211,153,0.3); padding: 0.25rem 0.75rem;
        border-radius: 9999px; font-size: 0.75rem; font-weight: 700;
        letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.6rem;
    }
    .hero-title {
        font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; margin: 0;
        background: linear-gradient(to right, #ffffff, #a7f3d0, #38bdf8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .hero-desc { color: #94a3b8; font-size: 1.05rem; margin-top: 0.5rem; max-width: 820px; line-height: 1.6; }

    .getstarted-banner {
        background: #0b2230; border: 1px solid rgba(56,189,248,0.25); border-radius: 12px;
        padding: 0.85rem 1.2rem; color: #bae6fd; font-size: 0.95rem; margin-bottom: 1.4rem;
    }
    .feature-card {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px;
        padding: 1.3rem 1.1rem; text-align: center; box-shadow: 0 4px 20px -4px rgba(0,0,0,0.06); height: 100%;
    }
    .feature-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
    .feature-title { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #64748b; margin-bottom: 0.5rem; }
    .feature-desc { font-size: 0.85rem; color: #475569; line-height: 1.5; }

    .dashboard-section {
        font-size: 1.28rem; font-weight: 700; margin: 1.8rem 0 0.9rem 0;
        display: flex; align-items: center; gap: 0.6rem;
        border-bottom: 2px solid rgba(120,120,160,0.2); padding-bottom: 0.35rem;
    }

    .stat-card {
        border-radius: 16px; padding: 1.25rem 1.4rem; border: 1px solid #e2e8f0;
        box-shadow: 0 4px 20px -4px rgba(0,0,0,0.06); transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-align: center; height: 100%;
    }
    .stat-card:hover { transform: translateY(-4px); box-shadow: 0 12px 28px -6px rgba(0,0,0,0.12); }
    .stat-title { font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.35rem; opacity: 0.85; }
    .stat-number { font-size: 2.1rem; font-weight: 800; line-height: 1.1; }
    .stat-sub { font-size: 0.82rem; font-weight: 500; margin-top: 0.35rem; opacity: 0.85; }

    .theme-low  { background: linear-gradient(135deg, #064e3b 0%, #059669 100%); color: #fff; border: none; }
    .theme-mod  { background: linear-gradient(135deg, #78350f 0%, #d97706 100%); color: #fff; border: none; }
    .theme-high { background: linear-gradient(135deg, #881337 0%, #e11d48 100%); color: #fff; border: none; }
    .theme-dark { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #fff; border: none; }

    .callout-pill {
        border-radius: 12px; padding: 0.85rem 1.15rem; margin-bottom: 0.6rem;
        font-size: 0.93rem; line-height: 1.5; border-left: 5px solid #3b82f6; transition: transform 0.15s ease;
    }
    .callout-pill:hover { transform: translateX(5px); }
    .pill-danger  { background: #fef2f2; border-left-color: #ef4444; color: #991b1b; }
    .pill-warning { background: #fffbeb; border-left-color: #f59e0b; color: #92400e; }
    .pill-success { background: #ecfdf5; border-left-color: #10b981; color: #065f46; }

    .badge-wrap { display: flex; flex-wrap: wrap; gap: 0.6rem; margin: 0.6rem 0; }
    .cyber-badge {
        display: inline-flex; align-items: center; gap: 0.4rem; background: #f1f5f9;
        border: 1px solid #cbd5e1; color: #1e293b; padding: 0.4rem 0.95rem;
        border-radius: 999px; font-size: 0.84rem; font-weight: 600; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    .disclaimer-card {
        background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 14px;
        padding: 1rem 1.3rem; font-size: 0.86rem; color: #64748b; margin-top: 2rem; line-height: 1.55;
    }
    .footer { text-align: center; padding: 1.2rem 0 0.4rem 0; opacity: 0.6; font-size: 0.85rem; }

    .app-tag {
        display: inline-block; background: #eef2ff; color: #4338ca; border: 1px solid #c7d2fe;
        padding: 0.2rem 0.65rem; border-radius: 999px; font-size: 0.78rem; font-weight: 600; margin: 0.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO HEADER
# ==========================================================
st.markdown("""
<div class="hero-banner">
    <span class="hero-tag">🛡 Real-time Privacy Intelligence</span>
    <p class="hero-title">Digital Footprint Visualizer</p>
    <p class="hero-desc">
        Map exactly which apps hold your camera, microphone, location and contacts —
        Instagram, WhatsApp, Zoom, ChatGPT, Claude and more — and see a weighted
        exposure profile built from real per-app data practices.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# APP CATALOG + RISK WEIGHTS
# App weight = a rough, educational multiplier for how much
# scrutiny that app's data practices typically warrant.
# 1.0 = baseline. Higher = broader/known data collection.
# ==========================================================
APP_CATALOG = {
    "📱 Social & Media": ["Instagram", "Facebook", "YouTube", "TikTok", "Snapchat", "Twitter / X", "LinkedIn"],
    "💬 Messaging & Calls": ["WhatsApp", "Telegram", "Zoom", "Google Meet", "Microsoft Teams"],
    "🤖 AI Assistants": ["ChatGPT", "Claude", "Google Gemini"],
    "🛒 Shopping & Finance": ["Amazon / Flipkart", "Other Shopping Apps", "Banking / Payment Apps"],
    "🎮 Entertainment": ["Netflix / Streaming", "Gaming Apps"],
    "☁️ Productivity & Cloud": ["Google Drive / Cloud Storage", "Email Apps"],
}
ALL_APPS = [app for group in APP_CATALOG.values() for app in group]

APP_RISK_WEIGHT = {
    "Instagram": 1.5, "Facebook": 1.6, "TikTok": 1.7, "Snapchat": 1.4,
    "Twitter / X": 1.3, "YouTube": 1.2, "LinkedIn": 1.1,
    "WhatsApp": 1.2, "Telegram": 1.1, "Zoom": 1.0, "Google Meet": 0.9, "Microsoft Teams": 0.9,
    "ChatGPT": 1.0, "Claude": 0.8, "Google Gemini": 1.0,
    "Amazon / Flipkart": 1.2, "Other Shopping Apps": 1.2, "Banking / Payment Apps": 1.3,
    "Netflix / Streaming": 0.8, "Gaming Apps": 1.1,
    "Google Drive / Cloud Storage": 1.0, "Email Apps": 0.9,
}

PERMISSION_BASE_POINTS = {
    "Camera": 1.5,
    "Microphone": 1.5,
    "Location": 2.0,
    "Contacts": 2.0,
    "Storage / Photos": 1.0,
    "SMS": 2.0,
    "Calendar": 1.0,
    "File Access": 1.2,
    "Ads / Tracking ID": 1.8,
}


def app_group_of(app_name):
    for group, apps in APP_CATALOG.items():
        if app_name in apps:
            return group
    return "Other"


# ==========================================================
# SIDEBAR — DATA COLLECTION
# ==========================================================
with st.sidebar:
    st.markdown("## 👤 Your Digital Information")
    st.caption("Answer honestly for a more meaningful analysis.")

    st.markdown("**📋 Basic Information**")
    name = st.text_input("Name", key="name")
    age = st.number_input("Age", min_value=1, max_value=100, value=18, step=1, key="age")
    screen_time = st.number_input("Total screen time (hrs/day)", 0.0, 24.0, 4.0, 0.5, key="screen_time")

    st.markdown("**📱 Which apps / platforms do you actively use?**")
    used_apps = []
    for group_name, apps in APP_CATALOG.items():
        with st.expander(group_name, expanded=False):
            for app in apps:
                if st.checkbox(app, key=f"use_{app}"):
                    used_apps.append(app)

    st.markdown("**🔐 App Permissions**")
    st.caption("For each permission — camera, mic, location, contacts, storage, SMS, calendar, files, ad/tracking ID — select which of your apps currently have it enabled.")
    if used_apps:
        camera_apps = st.multiselect("📷 Camera access granted to:", used_apps, key="camera_apps")
        mic_apps = st.multiselect("🎤 Microphone access granted to:", used_apps, key="mic_apps")
        location_apps = st.multiselect("📍 Location access granted to:", used_apps, key="location_apps")
        contacts_apps = st.multiselect("👥 Contacts access granted to:", used_apps, key="contacts_apps")
        storage_apps = st.multiselect("🗂 Storage / photos access granted to:", used_apps, key="storage_apps")
        sms_apps = st.multiselect("✉️ SMS / text message access granted to:", used_apps, key="sms_apps")
        calendar_apps = st.multiselect("📅 Calendar access granted to:", used_apps, key="calendar_apps")
        file_apps = st.multiselect("📁 File / document access granted to:", used_apps, key="file_apps")
        ads_apps = st.multiselect("🎯 Ad / tracking ID access granted to:", used_apps, key="ads_apps")
    else:
        st.info("Select at least one app above to specify its permissions.")
        camera_apps, mic_apps, location_apps, contacts_apps, storage_apps = [], [], [], [], []
        sms_apps, calendar_apps, file_apps, ads_apps = [], [], [], []

    st.markdown("**🌐 Internet & Network**")
    bluetooth = st.checkbox("🔵 Bluetooth frequently enabled", key="bluetooth")
    public_wifi = st.checkbox("📶 Frequently use public Wi-Fi", key="public_wifi")
    vpn = st.checkbox("🛡 Use a VPN", key="vpn")

    st.markdown("**🔒 Account Security**")
    two_factor = st.checkbox("🔑 Two-Factor Authentication", key="two_factor")
    password_reuse = st.checkbox("⚠️ Reuse the same password", key="password_reuse")
    unknown_apps = st.checkbox("❓ Install apps from unknown sources", key="unknown_apps")

    st.markdown("**📊 Digital Activity**")
    installed_apps = st.number_input("Total installed apps", 0, 1000, 20, 1, key="installed_apps")
    notifications = st.number_input("Daily notifications", 0, 5000, 30, 1, key="notifications")
    cloud_storage = st.checkbox("☁️ Use cloud storage / backups", key="cloud_storage")

    if st.button("🚀 Analyze My Digital Footprint", use_container_width=True):
        st.session_state.submitted = True

submitted = st.session_state.get("submitted", False)

# ==========================================================
# PRE-SUBMIT LANDING
# ==========================================================
if not submitted:
    st.markdown("""
    <div class="getstarted-banner">
        👉 <b>Get Started:</b> In the sidebar, pick the apps you use, tell us which
        of them have camera/mic/location/contacts access, then click
        '🚀 Analyze My Digital Footprint'.
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🕸</div>
            <div class="feature-title">App-Level Network</div>
            <div class="feature-desc">See exactly which named apps — Instagram, WhatsApp, Zoom, ChatGPT, Claude — connect to which permissions.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Weighted Risk Score</div>
            <div class="feature-desc">Scoring accounts for each app's typical data-collection footprint, not just the permission itself.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Per-App Recommendations</div>
            <div class="feature-desc">Concrete suggestions naming the exact app and permission to review.</div>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

if name.strip() == "":
    st.warning("⚠️ Please enter your name before starting the analysis.")
    st.stop()

# ==========================================================
# RISK ANALYSIS ENGINE
# ==========================================================
risk_breakdown = {}       # display_label -> points (drives bar chart / top risks)
permission_records = []   # list of dicts: app, permission, points, group

permission_app_map = {
    "Camera": camera_apps,
    "Microphone": mic_apps,
    "Location": location_apps,
    "Contacts": contacts_apps,
    "Storage / Photos": storage_apps,
    "SMS": sms_apps,
    "Calendar": calendar_apps,
    "File Access": file_apps,
    "Ads / Tracking ID": ads_apps,
}

permission_score = 0.0
for permission, apps in permission_app_map.items():
    base = PERMISSION_BASE_POINTS[permission]
    for app in apps:
        weight = APP_RISK_WEIGHT.get(app, 1.0)
        points = round(base * weight, 1)
        risk_breakdown[f"{app} — {permission}"] = points
        permission_score += points
        permission_records.append({
            "app": app, "permission": permission, "points": points, "group": app_group_of(app),
        })

habit_score = 0
if screen_time >= 6:
    habit_score += 2
    risk_breakdown["High Screen Time"] = 2
if len(used_apps) >= 8:
    habit_score += 1
    risk_breakdown["Large Number of Active Apps"] = 1
if public_wifi:
    habit_score += 2
    risk_breakdown["Public Wi-Fi"] = 2
if password_reuse:
    habit_score += 2
    risk_breakdown["Password Reuse"] = 2
if unknown_apps:
    habit_score += 2
    risk_breakdown["Unknown-Source Apps"] = 2
if not two_factor:
    habit_score += 1
    risk_breakdown["No Two-Factor Authentication"] = 1
if bluetooth:
    habit_score += 1
    risk_breakdown["Bluetooth Frequently On"] = 1

score = round(habit_score + permission_score, 1)

GAUGE_MAX = 40
LOW_THRESH = 12
HIGH_THRESH = 24

if score <= LOW_THRESH:
    category, theme_class, gauge_color, emoji = "Low Data Exposure", "theme-low", "#10b981", "🟢"
elif score <= HIGH_THRESH:
    category, theme_class, gauge_color, emoji = "Moderate Data Exposure", "theme-mod", "#f59e0b", "🟡"
else:
    category, theme_class, gauge_color, emoji = "High Data Exposure", "theme-high", "#ef4444", "🔴"

if score <= LOW_THRESH:
    st.balloons()

# ==========================================================
# TABS
# ==========================================================
tab_overview, tab_charts, tab_network, tab_advice, tab_data = st.tabs(
    ["🏠 Overview", "📊 Charts", "🕸 Network", "💡 Advice & Habits", "📋 Raw Data"]
)

# ----------------------------------------------------------
# TAB 1 — OVERVIEW
# ----------------------------------------------------------
with tab_overview:
    st.markdown(f'<div class="dashboard-section">📊 {name}\'s Digital Footprint Analysis</div>', unsafe_allow_html=True)

    col_gauge, col_cards = st.columns([1, 1.3])
    with col_gauge:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=score,
            delta={"reference": GAUGE_MAX * 0.4, "increasing": {"color": "#ef4444"}, "decreasing": {"color": "#10b981"}},
            number={"suffix": f" / {GAUGE_MAX}", "font": {"size": 36, "color": gauge_color}},
            title={"text": "Exposure Surface Score", "font": {"size": 18}},
            gauge={
                "axis": {"range": [0, GAUGE_MAX], "tickwidth": 1, "tickcolor": "#94a3b8"},
                "bar": {"color": gauge_color, "thickness": 0.32},
                "bgcolor": "#f8fafc", "borderwidth": 1, "bordercolor": "#cbd5e1",
                "steps": [
                    {"range": [0, LOW_THRESH], "color": "rgba(16,185,129,0.22)"},
                    {"range": [LOW_THRESH, HIGH_THRESH], "color": "rgba(245,158,11,0.22)"},
                    {"range": [HIGH_THRESH, GAUGE_MAX], "color": "rgba(239,68,68,0.22)"},
                ],
                "threshold": {"line": {"color": "#0f172a", "width": 3.5}, "thickness": 0.8, "value": score},
            },
        ))
        fig_gauge.update_layout(height=280, margin=dict(l=25, r=25, t=40, b=15), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_cards:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
                <div class="stat-card {theme_class}">
                    <div class="stat-title">Exposure Level</div>
                    <div class="stat-number">{emoji}</div>
                    <div class="stat-sub">{category}</div>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
                <div class="stat-card theme-dark">
                    <div class="stat-title">Apps With Sensitive Access</div>
                    <div class="stat-number">{len(permission_records)}</div>
                    <div class="stat-sub">app–permission pairs</div>
                </div>
            """, unsafe_allow_html=True)
        st.write("")
        peer_average = round(GAUGE_MAX * 0.4, 1)
        diff = round(score - peer_average, 1)
        if diff > 0:
            st.markdown(f'<div class="callout-pill pill-danger">📈 Your score is <b>{diff} point(s) above</b> a typical peer average of {peer_average}/{GAUGE_MAX}.</div>', unsafe_allow_html=True)
        elif diff < 0:
            st.markdown(f'<div class="callout-pill pill-success">📉 Your score is <b>{abs(diff)} point(s) below</b> a typical peer average of {peer_average}/{GAUGE_MAX} — nice work.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="callout-pill pill-warning">📊 Your score matches a typical peer average of {peer_average}/{GAUGE_MAX}.</div>', unsafe_allow_html=True)

    st.markdown('<div class="dashboard-section">📱 Apps You Use</div>', unsafe_allow_html=True)
    if used_apps:
        st.markdown("".join(f'<span class="app-tag">{a}</span>' for a in used_apps), unsafe_allow_html=True)
    else:
        st.info("No apps selected yet.")

    st.markdown('<div class="dashboard-section">🧠 Your Digital Profile</div>', unsafe_allow_html=True)
    if category == "Low Data Exposure":
        st.markdown('<div class="callout-pill pill-success">Your current profile shows relatively low exposure. Continue maintaining good privacy and security habits.</div>', unsafe_allow_html=True)
    elif category == "Moderate Data Exposure":
        st.markdown('<div class="callout-pill pill-warning">Your profile shows moderate exposure. Some app permissions and digital habits could be reviewed to improve your privacy.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="callout-pill pill-danger">Your profile shows high exposure according to this educational model. Review the major contributing apps and recommendations below.</div>', unsafe_allow_html=True)

    badges = []
    if two_factor:
        badges.append("🔐 2FA Champion")
    if vpn:
        badges.append("🛡 VPN User")
    if not password_reuse:
        badges.append("🔑 Password Pro")
    if not unknown_apps:
        badges.append("✅ Trusted Sources Only")
    if len(permission_records) <= 2:
        badges.append("🧭 Minimal Permissions")
    if score <= LOW_THRESH:
        badges.append("🌿 Low Footprint")
    if badges:
        st.markdown('<div class="badge-wrap">' + "".join(f'<span class="cyber-badge">{b}</span>' for b in badges) + '</div>', unsafe_allow_html=True)

# ----------------------------------------------------------
# TAB 2 — CHARTS
# ----------------------------------------------------------
with tab_charts:
    st.markdown('<div class="dashboard-section">📊 Top Risk Contributors</div>', unsafe_allow_html=True)
    if risk_breakdown:
        risk_df = pd.DataFrame(list(risk_breakdown.items()), columns=["Factor", "Risk Score"]) \
            .sort_values(by="Risk Score", ascending=True).tail(15)
        fig_bar = px.bar(
            risk_df, x="Risk Score", y="Factor", orientation="h",
            title="Factors Contributing to Your Exposure (top 15)", text="Risk Score",
            color="Risk Score", color_continuous_scale=["#10b981", "#f59e0b", "#ef4444"],
        )
        fig_bar.update_traces(textposition="outside")
        fig_bar.update_layout(xaxis_title="Risk Points", yaxis_title="", height=460, showlegend=False,
                               template="plotly_white", margin=dict(t=60, b=20), coloraxis_showscale=False)
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.markdown('<div class="callout-pill pill-success">🎉 No risk factors were triggered.</div>', unsafe_allow_html=True)

    col_donut, col_radar = st.columns(2)

    exposure_by_permission = {perm: 0.0 for perm in PERMISSION_BASE_POINTS}
    for rec in permission_records:
        exposure_by_permission[rec["permission"]] += rec["points"]
    exposure_by_permission_nonzero = {k: v for k, v in exposure_by_permission.items() if v > 0}

    with col_donut:
        st.markdown("#### 🥧 Exposure by Permission Type")
        if exposure_by_permission_nonzero:
            perm_df = pd.DataFrame(list(exposure_by_permission_nonzero.items()), columns=["Permission", "Score"])
            fig_donut = px.pie(perm_df, names="Permission", values="Score", hole=0.5,
                                color_discrete_sequence=["#38bdf8", "#f59e0b", "#a78bfa", "#ef4444", "#10b981"])
            fig_donut.update_layout(template="plotly_white", margin=dict(t=20, b=20), height=380)
            st.plotly_chart(fig_donut, use_container_width=True)
        else:
            st.info("No permission-based exposure recorded yet.")

    exposure_by_group = {}
    for rec in permission_records:
        exposure_by_group[rec["group"]] = exposure_by_group.get(rec["group"], 0.0) + rec["points"]

    with col_radar:
        st.markdown("#### 🕸 Exposure by App Category")
        if exposure_by_group:
            radar_categories = list(exposure_by_group.keys())
            radar_values = list(exposure_by_group.values())
            fig_radar = go.Figure(data=go.Scatterpolar(
                r=radar_values + [radar_values[0]],
                theta=radar_categories + [radar_categories[0]],
                fill="toself", line_color="#38bdf8", fillcolor="rgba(56,189,248,0.3)",
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, max(radar_values) + 1])),
                showlegend=False, height=380, template="plotly_white", margin=dict(t=20, b=20),
            )
            st.plotly_chart(fig_radar, use_container_width=True)
        else:
            st.info("No app-category exposure recorded yet.")

    st.markdown('<div class="dashboard-section">📈 Top Apps by Risk Contribution</div>', unsafe_allow_html=True)
    if permission_records:
        app_totals = {}
        for rec in permission_records:
            app_totals[rec["app"]] = app_totals.get(rec["app"], 0.0) + rec["points"]
        app_df = pd.DataFrame(list(app_totals.items()), columns=["App", "Risk Score"]).sort_values("Risk Score", ascending=False)
        fig_apps = px.bar(app_df, x="App", y="Risk Score", title="Which Apps Contribute Most to Your Score",
                           text="Risk Score", color="App")
        fig_apps.update_traces(textposition="outside")
        fig_apps.update_layout(template="plotly_white", showlegend=False, margin=dict(t=60, b=20))
        st.plotly_chart(fig_apps, use_container_width=True)
    else:
        st.info("No app permissions recorded yet.")

    st.markdown('<div class="dashboard-section">📈 General Digital Activity</div>', unsafe_allow_html=True)
    activity_df = pd.DataFrame({
        "Category": ["Screen Time (hrs)", "Apps Used", "Installed Apps", "Daily Notifications"],
        "Value": [screen_time, len(used_apps), installed_apps, notifications],
    })
    fig_activity = px.bar(activity_df, x="Category", y="Value", title="Your Digital Activity", color="Category",
                           color_discrete_sequence=["#38bdf8", "#a78bfa", "#f59e0b", "#10b981"], text="Value")
    fig_activity.update_traces(textposition="outside")
    fig_activity.update_layout(template="plotly_white", showlegend=False, margin=dict(t=60, b=20))
    st.plotly_chart(fig_activity, use_container_width=True)

# ----------------------------------------------------------
# TAB 3 — NETWORK GRAPH
# ----------------------------------------------------------
with tab_network:
    st.markdown('<div class="dashboard-section">🕸 Digital Footprint Network</div>', unsafe_allow_html=True)
    st.write("This map shows the specific apps you use and which sensitive permissions each one holds.")

    G = nx.Graph()
    G.add_node("YOU")
    app_layer_nodes = set()
    permission_layer_nodes = set()

    for app in used_apps:
        G.add_edge("YOU", app)
        app_layer_nodes.add(app)

    for rec in permission_records:
        G.add_edge(rec["app"], rec["permission"])
        permission_layer_nodes.add(rec["permission"])

    if len(G.nodes) > 1:
        pos = nx.spring_layout(G, seed=42, k=1.1)
        edge_x, edge_y = [], []
        for u, v in G.edges():
            x0, y0 = pos[u]; x1, y1 = pos[v]
            edge_x += [x0, x1, None]
            edge_y += [y0, y1, None]
        edge_trace = go.Scatter(x=edge_x, y=edge_y, mode="lines", hoverinfo="none", line=dict(width=1.5, color="#bbbbbb"))

        node_x, node_y, node_text, node_color, node_size = [], [], [], [], []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x); node_y.append(y); node_text.append(node)
            if node == "YOU":
                node_color.append("#38bdf8"); node_size.append(40)
            elif node in permission_layer_nodes:
                node_color.append("#ef4444"); node_size.append(30)
            elif node in app_layer_nodes:
                node_color.append("#f59e0b"); node_size.append(26)
            else:
                node_color.append("#a78bfa"); node_size.append(26)

        node_trace = go.Scatter(
            x=node_x, y=node_y, mode="markers+text", text=node_text,
            textposition="top center", hovertext=node_text, hoverinfo="text",
            marker=dict(size=node_size, color=node_color, line=dict(width=1.5, color="white")),
        )
        network_fig = go.Figure(data=[edge_trace, node_trace])
        network_fig.update_layout(
            title="Digital Footprint Connections", showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=620, template="plotly_white", margin=dict(t=60, b=20),
        )
        st.plotly_chart(network_fig, use_container_width=True)
        st.caption("🔵 You  •  🟠 Apps you use  •  🔴 Permissions those apps hold")
    else:
        st.info("Select apps and permissions in the sidebar to build your network map.")

# ----------------------------------------------------------
# TAB 4 — ADVICE, TOP RISKS, GOOD HABITS
# ----------------------------------------------------------
with tab_advice:
    st.markdown('<div class="dashboard-section">🚨 Your Top Risk Factors</div>', unsafe_allow_html=True)
    if risk_breakdown:
        top_risks = sorted(risk_breakdown.items(), key=lambda x: x[1], reverse=True)[:5]
        for index, (factor, points) in enumerate(top_risks, start=1):
            st.markdown(f'<div class="callout-pill pill-danger">🚨 <b>#{index} — {factor}</b> contributes {points} risk point(s).</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="callout-pill pill-success">No major risk factors were identified.</div>', unsafe_allow_html=True)

    st.markdown('<div class="dashboard-section">💡 Personalized Recommendations</div>', unsafe_allow_html=True)
    recommendations = []

    for rec in sorted(permission_records, key=lambda r: r["points"], reverse=True):
        app, permission = rec["app"], rec["permission"]
        if APP_RISK_WEIGHT.get(app, 1.0) >= 1.3:
            recommendations.append(f"⚠️ <b>{app}</b> has {permission.lower()} access — this app is associated with broader data collection, so double-check this permission is actually needed.")
        else:
            recommendations.append(f"🔎 Review whether <b>{app}</b> truly needs {permission.lower()} access, and revoke it if unused.")

    if public_wifi:
        recommendations.append("🌐 Avoid entering sensitive information while connected to untrusted public Wi-Fi.")
    if not two_factor:
        recommendations.append("🔐 Enable Two-Factor Authentication on important accounts whenever available.")
    if password_reuse:
        recommendations.append("🔑 Avoid reusing passwords across accounts. Use unique passwords for important services.")
    if unknown_apps:
        recommendations.append("⚠️ Avoid installing applications from unknown or untrusted sources.")
    if screen_time >= 6:
        recommendations.append("⏱️ Review your screen-time habits and reduce unnecessary digital activity where possible.")
    if installed_apps > 50:
        recommendations.append("📱 Review your installed applications and remove apps you no longer use.")
    if notifications > 100:
        recommendations.append("🔔 Review notification settings and disable unnecessary notifications.")
    if cloud_storage:
        recommendations.append("☁️ Review cloud-storage sharing permissions and avoid unnecessary public sharing.")
    if bluetooth:
        recommendations.append("🔵 Turn off Bluetooth when not actively in use to reduce discoverability.")

    if not recommendations:
        st.markdown('<div class="callout-pill pill-success">🎉 Excellent! No personalized warnings were triggered based on your current responses.</div>', unsafe_allow_html=True)
    else:
        for rec in recommendations[:12]:
            st.markdown(f'<div class="callout-pill pill-warning">{rec}</div>', unsafe_allow_html=True)

    st.markdown('<div class="dashboard-section">🏆 Good Digital Security Habits</div>', unsafe_allow_html=True)
    positive_habits = []
    if two_factor:
        positive_habits.append("🔐 Two-Factor Authentication is enabled.")
    if not password_reuse:
        positive_habits.append("🔑 You are not reusing the same password.")
    if vpn:
        positive_habits.append("🛡 You use a VPN.")
    if not unknown_apps:
        positive_habits.append("✅ You avoid installing apps from unknown sources.")
    if not public_wifi:
        positive_habits.append("🌐 You do not frequently use public Wi-Fi.")
    if len(permission_records) <= 2:
        positive_habits.append("🧭 You keep app permissions minimal.")
    if positive_habits:
        for habit in positive_habits:
            st.markdown(f'<div class="callout-pill pill-success">{habit}</div>', unsafe_allow_html=True)
    else:
        st.info("Build stronger security habits to improve your digital protection.")

    st.markdown('<div class="dashboard-section">🎯 Final Takeaway</div>', unsafe_allow_html=True)
    if score <= LOW_THRESH:
        st.markdown('<div class="callout-pill pill-success">Your digital exposure is relatively low according to this model. Keep following good privacy practices.</div>', unsafe_allow_html=True)
    elif score <= HIGH_THRESH:
        st.markdown('<div class="callout-pill pill-warning">Your digital exposure is moderate. Focus on the recommendations above, especially permissions on higher-weight apps.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="callout-pill pill-danger">Your digital exposure is high according to this model. Prioritize the highest-scoring app permissions first.</div>', unsafe_allow_html=True)

# ----------------------------------------------------------
# TAB 5 — RAW DATA
# ----------------------------------------------------------
with tab_data:
    st.markdown('<div class="dashboard-section">📋 Your Entered Information</div>', unsafe_allow_html=True)
    display_data = {
        "Name": name, "Age": age,
        "Screen Time (hours/day)": screen_time,
        "Apps Used": ", ".join(used_apps) if used_apps else "None",
        "Bluetooth": bluetooth, "Public Wi-Fi": public_wifi, "VPN": vpn,
        "Two-Factor Authentication": two_factor, "Password Reuse": password_reuse,
        "Unknown-Source Apps": unknown_apps, "Installed Apps": installed_apps,
        "Daily Notifications": notifications, "Cloud Storage": cloud_storage,
        "Exposure Score": f"{score} / {GAUGE_MAX}",
    }
    summary_df = pd.DataFrame(list(display_data.items()), columns=["Information", "Value"])
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    st.markdown('<div class="dashboard-section">🔐 Per-App Permission Matrix</div>', unsafe_allow_html=True)
    if used_apps:
        matrix_rows = []
        for app in used_apps:
            matrix_rows.append({
                "App": app,
                "Category": app_group_of(app).split(" ", 1)[-1],
                "Camera": app in camera_apps,
                "Microphone": app in mic_apps,
                "Location": app in location_apps,
                "Contacts": app in contacts_apps,
                "Storage/Photos": app in storage_apps,
                "SMS": app in sms_apps,
                "Calendar": app in calendar_apps,
                "File Access": app in file_apps,
                "Ads/Tracking ID": app in ads_apps,
            })
        matrix_df = pd.DataFrame(matrix_rows)
        st.dataframe(matrix_df, use_container_width=True, hide_index=True)
        csv_data = pd.concat(
            [summary_df.rename(columns={"Information": "Field", "Value": "Value"}), matrix_df],
            axis=0, ignore_index=True
        ).to_csv(index=False).encode("utf-8")
    else:
        st.info("No apps selected.")
        csv_data = summary_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download your data as CSV",
        data=csv_data,
        file_name=f"{name}_digital_footprint.csv",
        mime="text/csv",
    )

# ==========================================================
# DISCLAIMER + FOOTER
# ==========================================================
st.markdown("""
    <div class="disclaimer-card">
    ℹ️ <b>DISCLAIMER:</b> This is an educational risk-awareness model created for academic purposes.
    The score and app risk weights are approximations based on general, publicly known data
    practices, not an audit of any specific app's actual behavior, and do not reflect the
    real-time permissions granted on your device.
    </div>
""", unsafe_allow_html=True)
st.markdown('<div class="footer">🛡 Digital Footprint Visualizer | Educational Awareness Project</div>', unsafe_allow_html=True)


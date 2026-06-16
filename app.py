import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Healthcare Reality vs. Reimbursement Intelligence™",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# BRAND STYLING
# --------------------------------------------------
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    .stApp {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    h1 {
        color: #000000 !important;
        font-size: clamp(2.15rem, 8vw, 4.4rem) !important;
        line-height: 1.05 !important;
        letter-spacing: -0.045em !important;
    }

    h2 {
        color: #000000 !important;
        font-size: clamp(1.75rem, 6.5vw, 3.1rem) !important;
        line-height: 1.08 !important;
        letter-spacing: -0.035em !important;
        margin-top: 2rem !important;
    }

    h3, h4, p, li, span, div {
        color: #000000 !important;
    }

    p, li {
        font-size: 1.05rem;
        line-height: 1.55;
    }

    .brand-subtitle {
        font-size: clamp(1.05rem, 4vw, 1.55rem);
        line-height: 1.38;
        font-weight: 650;
        max-width: 980px;
        margin-bottom: 2rem;
        color: #000000 !important;
    }

    .orange-box {
        border: 2px solid #FF8200;
        padding: 1.25rem;
        border-radius: 16px;
        margin-bottom: 1rem;
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    .risk-box {
        border-left: 7px solid #FF8200;
        padding: 1.25rem;
        background-color: #FFF8F2 !important;
        margin-bottom: 1rem;
        border-radius: 10px;
        color: #000000 !important;
        font-weight: 500;
    }

    .metric-card {
        border: 2px solid #FF8200;
        padding: 1.1rem;
        border-radius: 14px;
        text-align: center;
        background-color: #FFFFFF !important;
        color: #000000 !important;
        min-height: 145px;
        box-shadow: 0 1px 6px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
    }

    .metric-card h3,
    .metric-card h4,
    .metric-card p {
        color: #000000 !important;
    }

    .case-card {
        border: 1.5px solid #FF8200;
        border-radius: 14px;
        padding: 1.1rem;
        margin-bottom: 1rem;
        background-color: #FFFFFF !important;
        box-shadow: 0 1px 6px rgba(0,0,0,0.05);
    }

    .case-card h3 {
        margin-top: 0 !important;
        font-size: 1.28rem !important;
        line-height: 1.2 !important;
    }

    .label {
        font-weight: 800;
        color: #FF8200 !important;
        text-transform: uppercase;
        font-size: 0.78rem;
        letter-spacing: 0.06em;
        margin-top: 0.75rem;
    }

    .value {
        font-size: 1rem;
        line-height: 1.45;
        margin-bottom: 0.45rem;
    }

    .kpi-card {
        border-left: 7px solid #FF8200;
        border-radius: 12px;
        padding: 1rem 1.15rem;
        background-color: #FFF8F2 !important;
        margin-bottom: 1rem;
    }

    .kpi-label {
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .kpi-value {
        font-size: clamp(1.55rem, 7vw, 2.5rem);
        line-height: 1.1;
        font-weight: 800;
    }

    div[data-testid="stAlert"] p {
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SHARED CONTENT
# --------------------------------------------------
APP_TITLE = "Healthcare Reality vs. Reimbursement Intelligence™"

APP_SUBTITLE = (
    "A simulated healthcare operations portfolio project showing how reimbursement systems may capture "
    "the claim while missing the real workflow complexity behind patient access, documentation, prior "
    "authorization, staff workload, and revenue cycle outcomes."
)

DISCLAIMER = (
    "Disclaimer: This is a simulated educational portfolio project created for healthcare operations "
    "learning and career development. It uses synthetic no-PHI examples only and is not intended for "
    "clinical, coding, billing, legal, reimbursement, or patient-care decision-making."
)

case_rows = [
    {
        "Scenario": "Prior authorization not verified before service",
        "System": "Authorization status marked as pending",
        "Reality": "Authorization responsibility was unclear between scheduling and patient access.",
        "Risk": "Authorization delay"
    },
    {
        "Scenario": "Documentation missing operational context",
        "System": "Clinical documentation appears incomplete",
        "Reality": "Provider note did not capture payer-required elements because requirements were not visible upstream.",
        "Risk": "Documentation risk"
    },
    {
        "Scenario": "Patient access notes incomplete",
        "System": "Registration record completed",
        "Reality": "Patient gave updated coverage information, but it was not fully reconciled.",
        "Risk": "Eligibility mismatch"
    },
    {
        "Scenario": "Claim submitted with limited workflow visibility",
        "System": "Claim generated and submitted",
        "Reality": "The claim moved forward even though workflow risk existed earlier.",
        "Risk": "Clean claim risk"
    },
    {
        "Scenario": "Staff rework required after downstream issue",
        "System": "Denial or delay appears at back-end",
        "Reality": "Multiple teams had to correct an issue that started before the visit.",
        "Risk": "Staff workload increase"
    }
]

metrics_rows = [
    {"Metric": "Clean Claim Rate", "Affected": "Claims may leave the front end with unresolved defects.", "Signal": "Claim edits, payer rejections, denial trends."},
    {"Metric": "Authorization Turnaround Time", "Affected": "Unclear ownership may extend authorization aging.", "Signal": "Pending authorization workqueues."},
    {"Metric": "Registration Accuracy", "Affected": "Coverage or demographic errors may require correction.", "Signal": "Registration correction reports."},
    {"Metric": "Denial Rate", "Affected": "Preventable denials may increase.", "Signal": "Denial category analysis."},
    {"Metric": "A/R Days", "Affected": "Payment delays may extend accounts receivable timelines.", "Signal": "Aging reports."},
    {"Metric": "Staff Rework Volume", "Affected": "Staff may spend extra time correcting avoidable issues.", "Signal": "Rework logs or task volume."},
    {"Metric": "Patient Call Volume", "Affected": "Patients may call repeatedly for status updates.", "Signal": "Call center trends."},
    {"Metric": "Documentation Completeness", "Affected": "Missing payer-required details may delay reimbursement.", "Signal": "Documentation query patterns."}
]

oversight_rows = [
    {"Area": "Patient Access Review", "Question": "Does the registration record match the actual patient situation?", "Why": "Prevents front-end errors from traveling downstream."},
    {"Area": "Authorization Review", "Question": "Was authorization required, obtained, pending, or missed?", "Why": "Reduces authorization-related delays and denials."},
    {"Area": "Documentation Review", "Question": "Does the documentation support the service and payer requirements?", "Why": "Improves claim readiness and documentation quality."},
    {"Area": "Revenue Cycle Review", "Question": "Could this become a denial, delay, rework item, or patient billing issue?", "Why": "Protects revenue cycle performance and patient experience."},
    {"Area": "Quality / Operations Review", "Question": "Where did the workflow first lose control?", "Why": "Supports process improvement and denial prevention."}
]

workflow_steps = [
    "Scheduling",
    "Registration",
    "Eligibility Verification",
    "Prior Authorization",
    "Documentation",
    "Claim Submission",
    "Denial / Delay / Rework"
]

distortion_rows = [
    {"Point": "Scheduling", "Distortion": "Appointment reason does not fully match payer requirements.", "Risk": "Wrong service path."},
    {"Point": "Registration", "Distortion": "Patient information appears complete but contains outdated coverage.", "Risk": "Eligibility-related denial."},
    {"Point": "Eligibility", "Distortion": "Coverage is active but benefits or service rules are unclear.", "Risk": "Patient balance confusion."},
    {"Point": "Prior Authorization", "Distortion": "Authorization is pending but ownership is not clearly assigned.", "Risk": "Delayed care or delayed payment."},
    {"Point": "Documentation", "Distortion": "Documentation exists but does not answer payer-specific requirements.", "Risk": "Documentation-related denial."},
    {"Point": "Claim Submission", "Distortion": "Claim is created even though upstream workflow risk remains.", "Risk": "Rework, appeal, or payment delay."}
]

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def render_case_cards(rows):
    for row in rows:
        st.markdown(
            f"""
            <div class="case-card">
                <h3>{row.get('Scenario') or row.get('Metric') or row.get('Area') or row.get('Point')}</h3>
                {''.join([f'<div class="label">{key}</div><div class="value">{value}</div>' for key, value in row.items() if key not in ['Scenario', 'Metric', 'Area', 'Point']])}
            </div>
            """,
            unsafe_allow_html=True
        )


def render_kpi(label, value):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# PAGE FUNCTIONS
# --------------------------------------------------
def home_page():
    st.title(APP_TITLE)
    st.markdown(f'<div class="brand-subtitle">{APP_SUBTITLE}</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        """
        <div class="orange-box">
            <h3>Portfolio Purpose</h3>
            <p>This demo explains a healthcare operations problem: reimbursement systems may show the claim,
            authorization status, documentation status, or denial outcome, but they may not fully show the
            operational reality that created the risk.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    for title, body in [
        ("Patient Access", "Where demographic, eligibility, and authorization issues often begin."),
        ("Workflow Reality", "What staff, patients, and departments experience before the claim outcome appears."),
        ("Revenue Cycle Risk", "How upstream workflow gaps become denials, delays, rework, and patient friction.")
    ]:
        st.markdown(f"""<div class="metric-card"><h3>{title}</h3><p>{body}</p></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.info("Use the sidebar to move through the demo: System View vs Reality, Workflow Distortion Map, Simulated Case Study, Metrics Affected, Human Oversight, Executive Summary, and Disclaimer.")


def system_view_vs_reality_page():
    st.title("System View vs Reality")
    st.write("This page compares what a reimbursement or revenue cycle system may record against what may actually happen operationally before, during, and after the patient encounter.")
    render_case_cards(case_rows)
    st.markdown("## Key Insight")
    st.markdown("""<div class="risk-box">The system may capture the final claim status, but the operational cause may have started earlier in scheduling, eligibility verification, prior authorization, documentation preparation, or handoff communication.</div>""", unsafe_allow_html=True)


def workflow_distortion_map_page():
    st.title("Workflow Distortion Map")
    st.write("Workflow distortion happens when the system record looks stable, but the real operational process is fragmented, delayed, unclear, or dependent on manual follow-up.")

    for index, step in enumerate(workflow_steps, start=1):
        st.markdown(f"""<div class="metric-card"><h4>{index}</h4><p>{step}</p></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Where Distortion Occurs")
    render_case_cards(distortion_rows)


def simulated_case_study_page():
    st.title("Simulated Case Study")
    st.markdown(
        """
        <div class="orange-box">
            <h3>Simulated Scenario</h3>
            <p>A patient is scheduled for a service that requires prior authorization. The appointment is completed,
            documentation is entered, and the claim is submitted. Later, the account is delayed because the
            authorization record was incomplete and documentation did not clearly support payer requirements.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## What the Revenue Cycle System Sees")
    st.write("- Patient registered\n- Service completed\n- Documentation entered\n- Claim submitted\n- Authorization status issue appears later\n- Account delayed or denied")

    st.markdown("## What Actually Happened Operationally")
    st.write("- Authorization ownership was unclear before the visit\n- Eligibility was checked, but service-specific requirements were not fully validated\n- Staff had to rely on manual follow-up\n- Documentation did not clearly connect the service to payer expectations\n- The issue was discovered after the patient encounter instead of before it\n- Multiple teams became involved after the workflow had already moved downstream")

    st.markdown("## Workflow Distortion")
    st.warning("The workflow looked complete inside the system, but key operational questions were unresolved before the claim moved forward.")


def metrics_affected_page():
    st.title("Metrics Affected")
    st.write("A workflow issue may look small at the front end, but it can affect multiple healthcare operations and revenue cycle metrics downstream.")
    render_case_cards(metrics_rows)

    st.markdown("## Metrics Recruiters Should Notice")
    render_kpi("Clean Claim Risk", "High")
    render_kpi("Patient Friction", "Increased")
    render_kpi("Staff Rework", "Increased")
    render_kpi("Denial Prevention", "Needs Earlier Review")


def human_oversight_page():
    st.title("Human Oversight")
    st.write("This demo does not argue that systems are useless. It shows that healthcare systems still require human review because operational context may not be fully visible in structured claim, authorization, or documentation fields.")
    render_case_cards(oversight_rows)
    st.markdown("""<div class="risk-box">Human oversight is required because operational reality often lives between system fields, staff handoffs, payer rules, patient communication, and documentation quality.</div>""", unsafe_allow_html=True)


def executive_summary_page():
    st.title("Executive Summary")
    st.markdown(
        """
        ## Healthcare Operations Finding
        Reimbursement systems may accurately show that a claim was created, submitted, delayed, denied,
        corrected, or paid. However, those system events do not always explain the operational reality that
        created the outcome.

        ## Main Risk
        The main risk is that healthcare leaders may see the financial result without seeing the workflow
        breakdown that caused it.

        ## Operational Impact
        When patient access, prior authorization, documentation, and handoff processes are unclear, the
        downstream impact can include increased denials, delayed reimbursement, higher staff rework,
        patient confusion, more status calls, documentation corrections, and avoidable workflow friction.

        ## Career-Relevant Explanation
        This portfolio project demonstrates healthcare operations thinking by showing how upstream workflow
        issues can create downstream revenue cycle risk. It connects patient access, prior authorization,
        documentation quality, staff workload, denial prevention, and human oversight into one practical
        operations intelligence framework.
        """
    )
    st.success("Recruiter explanation: This project shows that I understand how healthcare workflow issues can begin before the claim, before the denial, and before the dashboard shows a problem.")


def disclaimer_page():
    st.title("Disclaimer")
    st.markdown(f"""<div class="orange-box"><p>{DISCLAIMER}</p></div>""", unsafe_allow_html=True)
    st.markdown("## Important Boundaries")
    st.write("- No real patient data\n- No PHI\n- No real payer data\n- No real claim data\n- No clinical decision-making\n- No billing, coding, legal, or reimbursement advice\n- Simulated educational examples only")

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
pages = [
    st.Page(home_page, title="Home", icon="🏠"),
    st.Page(system_view_vs_reality_page, title="System View vs Reality", icon="🔍"),
    st.Page(workflow_distortion_map_page, title="Workflow Distortion Map", icon="🧭"),
    st.Page(simulated_case_study_page, title="Simulated Case Study", icon="📄"),
    st.Page(metrics_affected_page, title="Metrics Affected", icon="📊"),
    st.Page(human_oversight_page, title="Human Oversight", icon="👁️"),
    st.Page(executive_summary_page, title="Executive Summary", icon="🧾"),
    st.Page(disclaimer_page, title="Disclaimer", icon="⚠️"),
]

pg = st.navigation(pages)
pg.run()

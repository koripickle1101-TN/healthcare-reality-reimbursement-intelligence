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
        font-size: clamp(2.1rem, 7vw, 4.5rem) !important;
        line-height: 1.05 !important;
        letter-spacing: -0.04em !important;
    }

    h2, h3, h4, p, li, span, div {
        color: #000000 !important;
    }

    .brand-subtitle {
        font-size: clamp(1.05rem, 4vw, 1.7rem);
        line-height: 1.35;
        font-weight: 600;
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

    .orange-box h3,
    .orange-box p,
    .orange-box li {
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
        min-height: 150px;
        box-shadow: 0 1px 6px rgba(0,0,0,0.06);
    }

    .metric-card h3,
    .metric-card h4,
    .metric-card p {
        color: #000000 !important;
    }

    .small-note {
        font-size: 0.9rem;
        color: #000000 !important;
    }

    div[data-testid="stAlert"] {
        color: #000000 !important;
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

case_df = pd.DataFrame(
    {
        "Scenario": [
            "Prior authorization not verified before service",
            "Documentation missing operational context",
            "Patient access notes incomplete",
            "Claim submitted with limited workflow visibility",
            "Staff rework required after downstream issue"
        ],
        "What the System Sees": [
            "Authorization status marked as pending",
            "Clinical documentation appears incomplete",
            "Registration record completed",
            "Claim generated and submitted",
            "Denial or delay appears at back-end"
        ],
        "What Actually Happened": [
            "Authorization responsibility was unclear between scheduling and patient access",
            "Provider note did not capture payer-required elements because requirements were not visible upstream",
            "Patient gave updated coverage information, but it was not fully reconciled",
            "The claim moved forward even though workflow risk existed earlier",
            "Multiple teams had to correct an issue that started before the visit"
        ],
        "Workflow Risk": [
            "Authorization delay",
            "Documentation risk",
            "Eligibility mismatch",
            "Clean claim risk",
            "Staff workload increase"
        ]
    }
)

metrics_df = pd.DataFrame(
    {
        "Metric": [
            "Clean Claim Rate",
            "Authorization Turnaround Time",
            "Registration Accuracy",
            "Denial Rate",
            "A/R Days",
            "Staff Rework Volume",
            "Patient Call Volume",
            "Documentation Completeness"
        ],
        "How It Can Be Affected": [
            "Claims may leave the front end with unresolved defects",
            "Unclear ownership may extend authorization aging",
            "Coverage or demographic errors may require correction",
            "Preventable denials may increase",
            "Payment delays may extend accounts receivable timelines",
            "Staff may spend extra time correcting avoidable issues",
            "Patients may call repeatedly for status updates",
            "Missing payer-required details may delay reimbursement"
        ],
        "Operational Signal": [
            "Claim edits, payer rejections, denial trends",
            "Pending authorization workqueues",
            "Registration correction reports",
            "Denial category analysis",
            "Aging reports",
            "Rework logs or task volume",
            "Call center trends",
            "Documentation query patterns"
        ]
    }
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

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="metric-card"><h3>Patient Access</h3><p>Where demographic, eligibility, and authorization issues often begin.</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="metric-card"><h3>Workflow Reality</h3><p>What staff, patients, and departments experience before the claim outcome appears.</p></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="metric-card"><h3>Revenue Cycle Risk</h3><p>How upstream workflow gaps become denials, delays, rework, and patient friction.</p></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.info("Use the sidebar to move through the demo: System View vs Reality, Workflow Distortion Map, Simulated Case Study, Metrics Affected, Human Oversight, Executive Summary, and Disclaimer.")


def system_view_vs_reality_page():
    st.title("System View vs Reality")
    st.write("This page compares what a reimbursement or revenue cycle system may record against what may actually happen operationally before, during, and after the patient encounter.")
    st.dataframe(case_df, use_container_width=True)
    st.markdown("### Key Insight")
    st.markdown("""<div class="risk-box">The system may capture the final claim status, but the operational cause may have started earlier in scheduling, eligibility verification, prior authorization, documentation preparation, or handoff communication.</div>""", unsafe_allow_html=True)


def workflow_distortion_map_page():
    st.title("Workflow Distortion Map")
    st.write("Workflow distortion happens when the system record looks stable, but the real operational process is fragmented, delayed, unclear, or dependent on manual follow-up.")

    workflow_steps = [
        "Scheduling",
        "Registration",
        "Eligibility Verification",
        "Prior Authorization",
        "Documentation",
        "Claim Submission",
        "Denial / Delay / Rework"
    ]

    cols = st.columns(2)
    for index, step in enumerate(workflow_steps):
        with cols[index % 2]:
            st.markdown(f"""<div class="metric-card"><h4>{index + 1}</h4><p>{step}</p></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Where Distortion Occurs")

    distortion_df = pd.DataFrame(
        {
            "Workflow Point": ["Scheduling", "Registration", "Eligibility", "Prior Authorization", "Documentation", "Claim Submission"],
            "Possible Distortion": [
                "Appointment reason does not fully match payer requirements",
                "Patient information appears complete but contains outdated coverage",
                "Coverage is active but benefits or service rules are unclear",
                "Authorization is pending but ownership is not clearly assigned",
                "Documentation exists but does not answer payer-specific requirements",
                "Claim is created even though upstream workflow risk remains"
            ],
            "Downstream Risk": [
                "Wrong service path",
                "Eligibility-related denial",
                "Patient balance confusion",
                "Delayed care or delayed payment",
                "Documentation-related denial",
                "Rework, appeal, or payment delay"
            ]
        }
    )
    st.dataframe(distortion_df, use_container_width=True)


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

    st.markdown("### What the Revenue Cycle System Sees")
    st.write("- Patient registered\n- Service completed\n- Documentation entered\n- Claim submitted\n- Authorization status issue appears later\n- Account delayed or denied")

    st.markdown("### What Actually Happened Operationally")
    st.write("- Authorization ownership was unclear before the visit\n- Eligibility was checked, but service-specific requirements were not fully validated\n- Staff had to rely on manual follow-up\n- Documentation did not clearly connect the service to payer expectations\n- The issue was discovered after the patient encounter instead of before it\n- Multiple teams became involved after the workflow had already moved downstream")

    st.markdown("### Workflow Distortion")
    st.warning("The workflow looked complete inside the system, but key operational questions were unresolved before the claim moved forward.")


def metrics_affected_page():
    st.title("Metrics Affected")
    st.write("A workflow issue may look small at the front end, but it can affect multiple healthcare operations and revenue cycle metrics downstream.")
    st.dataframe(metrics_df, use_container_width=True)

    st.markdown("### Metrics Recruiters Should Notice")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Clean Claim Risk", "High")
        st.metric("Patient Friction", "Increased")
    with col2:
        st.metric("Staff Rework", "Increased")
        st.metric("Denial Prevention", "Needs Earlier Review")


def human_oversight_page():
    st.title("Human Oversight")
    st.write("This demo does not argue that systems are useless. It shows that healthcare systems still require human review because operational context may not be fully visible in structured claim, authorization, or documentation fields.")

    oversight_df = pd.DataFrame(
        {
            "Review Area": ["Patient Access Review", "Authorization Review", "Documentation Review", "Revenue Cycle Review", "Quality / Operations Review"],
            "Human Question": [
                "Does the registration record match the actual patient situation?",
                "Was authorization required, obtained, pending, or missed?",
                "Does the documentation support the service and payer requirements?",
                "Could this become a denial, delay, rework item, or patient billing issue?",
                "Where did the workflow first lose control?"
            ],
            "Why It Matters": [
                "Prevents front-end errors from traveling downstream",
                "Reduces authorization-related delays and denials",
                "Improves claim readiness and documentation quality",
                "Protects revenue cycle performance and patient experience",
                "Supports process improvement and denial prevention"
            ]
        }
    )
    st.dataframe(oversight_df, use_container_width=True)
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
    st.markdown("### Important Boundaries")
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

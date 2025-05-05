import streamlit as st

st.set_page_config(page_title="AutoFlow Lite", layout="centered")

# --- Title ---
st.title("⚙️ AutoFlow Lite – Free Business Automation Starter")
st.markdown("Welcome! Fill in a few quick details below and see how AutoFlow can start removing busy work from your business today.")

# --- Form ---
with st.form("automation_form"):
    business_type = st.text_input("1. What type of business do you run? (e.g. agency, ecommerce, roofing)")
    task_description = st.text_area("2. What's one repetitive task that eats up your time?")
    team_size = st.slider("3. How many people are on your team?", 1, 20, 3)
    submitted = st.form_submit_button("🔍 Analyze My Workflow")

# --- Logic Output ---
if submitted:
    st.markdown("---")
    st.subheader("🧠 AutoFlow Analysis")
    st.write(f"**Business Type:** {business_type}")
    st.write(f"**Task to Automate:** {task_description}")
    st.write(f"**Team Size:** {team_size}")
    
    # Simple keyword logic for task categories
    task_lower = task_description.lower()

    if any(kw in task_lower for kw in ["email", "follow", "reminder", "onboard"]):
        st.markdown("### 💡 Suggested Automation: Client Communication & Follow-Up")
        st.markdown("- Auto-send welcome and onboarding emails")
        st.markdown("- Schedule reminders using Calendly + Google Calendar")
        st.markdown("- Add new leads to your CRM or Google Sheet")
        st.markdown("- Send follow-ups automatically if no reply")
        st.metric("⏱️ Estimated Time Saved", f"{team_size * 1.5} hours/week")

    elif any(kw in task_lower for kw in ["invoice", "payment", "billing"]):
        st.markdown("### 💡 Suggested Automation: Invoicing & Payment Reminders")
        st.markdown("- Auto-generate and send invoices")
        st.markdown("- Trigger payment reminders after X days")
        st.markdown("- Log payment status in your KPI tracker")
        st.metric("💸 Revenue Recovered", "$500+/month (avg)")

    elif any(kw in task_lower for kw in ["leads", "prospect", "crm", "form"]):
        st.markdown("### 💡 Suggested Automation: Lead Capture & Qualification")
        st.markdown("- Auto-capture leads from forms or ads")
        st.markdown("- Qualify leads based on preset questions")
        st.markdown("- Send lead data to your CRM or Google Sheet")
        st.metric("🚀 Leads Managed Weekly", f"{team_size * 10} leads")

    else:
        st.markdown("### 💡 Suggested Automation: Admin Tasks & Internal Ops")
        st.markdown("- Route tasks to one given page")
        st.markdown("- Track progress inside shared dashboards")
        st.markdown("- Trigger alerts when actions are due")
        st.metric("⏱️ Time Saved", f"{team_size * 2} hours/week")
if submitted:
    st.markdown("---")
    st.markdown("### 🧪 What You Just Saw is Just a Glimpse")

    st.info("""
    These suggestions are **starter-level ideas** based on your inputs.  
    With AutoFlow Pro, we go way deeper: pre-built automation systems, real workflow templates, and tools tailored to your specific business — no guesswork.

    We know your business is important, and trust isn’t built in a click — that’s why this tool exists. Let me earn it.
    """)

    # Ask for feedback
    feedback = st.text_area("🗣️ Could AutoFlow Lite help your business?")
    ideas = st.text_area("💡 What features or automations would you like to see added?")

    if feedback or ideas:
        st.success("Thanks for your input. We're building based on real feedback like yours.")

    # 🔥 CTA: Low-ticket upsell to scorecard
    st.markdown("---")
    st.info("""
    ### 📊 Unlock Your Automation Potential  
    Want to know exactly **what you should automate first**?

    ✅ Use the **AutoFlow Scorecard** to:
    - Log your most repetitive tasks  
    - Score them based on effort, time, and impact  
    - Discover your #1 time-waster worth automating

    👉 [Get the Scorecard for $5 on Whop](https://whop.com/checkout/plan_p1mhDbpHswfAE/)  
    """)


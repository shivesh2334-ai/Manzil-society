import streamlit as st
import pandas as pd
from utils.style import apply_custom_css

# Set page configuration
st.set_page_config(
    page_title="Manzil C G H Society",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Sidebar navigation
st.sidebar.title("🏠 Manzil Society")
st.sidebar.markdown("---")

# Main page selection in sidebar
page_options = {
    "🏠 Home": "Home",
    "👥 Members Directory": "Members", 
    "💰 Financial Statements": "Finance",
    "📅 AGM Updates": "AGM",
    "📞 Contact Us": "Contact",
    "💡 Suggestions": "Suggestions"
}

selection = st.sidebar.radio("Navigation", list(page_options.keys()))

# Info in sidebar
st.sidebar.markdown("---")
st.sidebar.info("**Society Office Hours:**\n\nMonday-Saturday: 9:00 AM - 5:00 PM\nSunday: 10:00 AM - 1:00 PM")

st.sidebar.markdown("---")
st.sidebar.markdown("**Emergency Contacts:**")
st.sidebar.markdown("- Security: +91 98765 43210")
st.sidebar.markdown("- Medical: +91 98765 43211")
st.sidebar.markdown("- Maintenance: +91 98765 43212")

# Login section
st.sidebar.markdown("---")
with st.sidebar.expander("🔐 Member Login"):
    username = st.text_input("Username/Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            st.success("Login successful!")
        else:
            st.warning("Please enter credentials")

# Main content area
st.title(f"Manzil Cooperative Group Housing Society")
st.markdown("---")

if selection == "🏠 Home":
    st.markdown("### Welcome to Manzil Society")
    st.markdown("""
    A community of responsible residents working together to create a harmonious 
    living environment for all members.
    """)
    
    # Create columns for stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Members", "150+", "5 new")
        
    with col2:
        st.metric("Residential Towers", "5", "")
        
    with col3:
        st.metric("Years Established", "16", "")
    
    st.markdown("---")
    
    # Latest announcements
    st.subheader("📢 Latest Announcements")
    
    with st.expander("🚰 Water Tank Cleaning", expanded=True):
        st.markdown("""
        **Date:** 15th-17th November 2023  
        **Details:** Scheduled water tank cleaning. Water supply will be affected during this period.  
        **Action:** Store sufficient water for these days.
        """)
    
    with st.expander("🎉 Diwali Celebration"):
        st.markdown("""
        **Date:** 12th November 2023  
        **Time:** 6:00 PM onwards  
        **Venue:** Community Hall  
        **All members are cordially invited!**
        """)
        
    with st.expander("🔧 Lift Maintenance"):
        st.markdown("""
        **Date:** 8th November 2023  
        **Time:** 9:00 AM - 5:00 PM  
        **Affected:** Tower A & B lifts  
        **Note:** One lift will remain operational during maintenance.
        """)
    
elif selection == "👥 Members Directory":
    st.subheader("👥 Society Members Directory")
    
    # Search functionality
    search_term = st.text_input("🔍 Search members by name, flat number, phone or email", "")
    
    # Load sample data
    from utils.data import members_data
    df = pd.DataFrame(members_data)
    
    # Filter data based on search
    if search_term:
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        df = df[mask]
    
    # Display table
    st.dataframe(
        df,
        column_config={
            "name": "Name",
            "flat_no": "Flat No.",
            "phone": "Phone",
            "email": "Email",
            "type": "Owner/Tenant"
        },
        use_container_width=True,
        hide_index=True
    )
    
    st.info("💡 **Note:** Only showing basic information. For complete member directory, please contact the office.")

elif selection == "💰 Financial Statements":
    st.subheader("💰 Financial Statements")
    
    # Create tabs for different financial statements
    tab1, tab2, tab3 = st.tabs(["📊 Balance Sheet", "📈 Profit & Loss", "💵 Cash Flow"])
    
    with tab1:
        st.markdown("### Balance Sheet as on 30th September 2023")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Assets")
            assets_data = {
                "Particulars": ["Cash & Bank Balance", "Fixed Deposits", "Maintenance Receivables", "Other Receivables", "**Total Assets**"],
                "Amount (₹)": ["12,45,780", "85,00,000", "8,75,430", "2,10,500", "**1,08,31,710**"]
            }
            st.table(pd.DataFrame(assets_data))
        
        with col2:
            st.markdown("#### Liabilities")
            liabilities_data = {
                "Particulars": ["Advance Maintenance", "Security Deposits", "Payables (Vendors)", "Reserve Fund", "**Total Liabilities**"],
                "Amount (₹)": ["5,20,000", "15,00,000", "3,85,200", "84,26,510", "**1,08,31,710**"]
            }
            st.table(pd.DataFrame(liabilities_data))
    
    with tab2:
        st.markdown("### Profit & Loss Statement (Apr 2023 - Sep 2023)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Income")
            income_data = {
                "Particulars": ["Maintenance Charges", "Parking Fees", "Interest Income", "Other Income", "**Total Income**"],
                "Amount (₹)": ["42,85,000", "5,20,000", "2,85,500", "1,25,300", "**52,15,800**"]
            }
            st.table(pd.DataFrame(income_data))
        
        with col2:
            st.markdown("#### Expenses")
            expenses_data = {
                "Particulars": ["Staff Salaries", "Electricity & Water", "Repairs & Maintenance", "Security Services", "Administrative Expenses", "**Total Expenses**", "**Net Profit**"],
                "Amount (₹)": ["18,50,000", "12,75,000", "8,20,500", "6,00,000", "3,85,200", "**49,30,700**", "**2,85,100**"]
            }
            st.table(pd.DataFrame(expenses_data))
    
    with tab3:
        st.markdown("### Cash Flow Statement (Apr 2023 - Sep 2023)")
        
        cashflow_data = {
            "Particulars": [
                "Opening Cash Balance (1 Apr 2023)",
                "**Cash Inflows**",
                "Maintenance Collections",
                "Parking Fees",
                "Interest Received",
                "**Total Inflows**",
                "**Cash Outflows**",
                "Staff Payments",
                "Utility Payments",
                "Repairs & Maintenance",
                "Security Services",
                "Other Expenses",
                "**Total Outflows**",
                "**Net Cash Flow**",
                "**Closing Cash Balance (30 Sep 2023)**"
            ],
            "Amount (₹)": [
                "8,50,000",
                "",
                "42,85,000",
                "5,20,000",
                "2,00,000",
                "**50,05,000**",
                "",
                "18,50,000",
                "12,75,000",
                "8,20,500",
                "6,00,000",
                "3,85,200",
                "**49,30,700**",
                "**74,300**",
                "**9,24,300**"
            ]
        }
        st.table(pd.DataFrame(cashflow_data))
    
    st.info("📄 Detailed financial statements and audit reports are available for members at the society office.")

elif selection == "📅 AGM Updates":
    st.subheader("📅 AGM Updates & Minutes")
    
    # Search by date
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_date = st.date_input("Search AGM by date", value=None)
    
    with col2:
        st.markdown("")
        st.markdown("")
        if st.button("🔍 Search", use_container_width=True):
            pass
    
    # Load AGM data
    from utils.data import agm_data
    
    # Filter if date is selected
    display_data = agm_data
    if search_date:
        search_str = search_date.strftime("%Y-%m-%d")
        display_data = [agm for agm in agm_data if agm["date"] == search_str]
    
    # Display AGM cards
    if not display_data:
        st.warning("No AGM found for the selected date.")
    else:
        for agm in display_data:
            with st.expander(f"📋 {agm['title']} - {agm['date']}", expanded=True):
                st.markdown(f"**Date:** {agm['date']}")
                st.markdown(f"**Details:** {agm['content']}")
                st.markdown(f"**Quorum:** {agm.get('quorum', '65 members present')}")
                st.markdown(f"**Venue:** {agm.get('venue', 'Society Community Hall')}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"📄 Download Minutes", key=f"minutes_{agm['date']}"):
                        st.success(f"Downloading minutes for {agm['title']}")
                with col2:
                    if st.button(f"📊 View Attendance", key=f"attendance_{agm['date']}"):
                        st.info(f"Attendance data for {agm['title']}")

elif selection == "📞 Contact Us":
    st.subheader("📞 Contact Manzil Society")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📍 Office Address")
        st.markdown("""
        **Manzil C G H Society**  
        Sector 22, Dwarka  
        New Delhi - 110077
        """)
        
        st.markdown("### 📱 Contact Details")
        st.markdown("""
        **Phone:** +91 11 2789 4563  
        **Mobile:** +91 9876543210  
        **Email:** office@manzilsociety.com
        """)
        
        st.markdown("### 🕐 Office Hours")
        st.markdown("""
        **Monday-Saturday:** 9:00 AM - 5:00 PM  
        **Sunday:** 10:00 AM - 1:00 PM
        """)
        
        st.markdown("### 👥 Managing Committee")
        st.markdown("""
        **Chairperson:** Mr. Rajesh Kumar  
        **Secretary:** Mrs. Priya Sharma  
        **Treasurer:** Mr. Amit Patel
        """)
    
    with col2:
        st.markdown("### 📝 Send a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            flat_no = st.text_input("Flat Number *")
            phone = st.text_input("Phone Number *")
            email = st.text_input("Email")
            
            subject = st.selectbox(
                "Subject *",
                ["Select a subject", "Maintenance Issue", "Billing Query", 
                 "Complaint", "General Inquiry", "Other"]
            )
            
            message = st.text_area("Message *", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and flat_no and phone and subject != "Select a subject" and message:
                    st.success(f"Thank you {name}! Your message has been submitted. The office will contact you shortly.")
                else:
                    st.error("Please fill all required fields (*)")

elif selection == "💡 Suggestions":
    st.subheader("💡 Suggestions & Feedback")
    
    st.info("Your suggestions help us improve our society. All suggestions are reviewed in monthly committee meetings.")
    
    with st.form("suggestion_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name *")
            flat_no = st.text_input("Flat Number *")
            
        with col2:
            phone = st.text_input("Phone Number")
            email = st.text_input("Email")
        
        suggestion_title = st.text_input("Suggestion Title *")
        
        category = st.selectbox(
            "Category *",
            ["Select category", "Maintenance & Repairs", "Security", 
             "Amenities & Facilities", "Community Events", "Society Policies", "Other"]
        )
        
        priority = st.radio(
            "Priority Level",
            ["Low", "Medium", "High"],
            horizontal=True
        )
        
        details = st.text_area("Detailed Suggestion *", 
                              placeholder="Please provide detailed explanation of your suggestion...",
                              height=200)
        
        submitted = st.form_submit_button("Submit Suggestion")
        
        if submitted:
            if name and flat_no and suggestion_title and category != "Select category" and details:
                st.success(f"Thank you {name}! Your suggestion '{suggestion_title}' has been submitted successfully. It will be reviewed in the next committee meeting.")
                
                # Show suggestion summary
                with st.expander("📋 Your Suggestion Summary", expanded=True):
                    st.markdown(f"**Title:** {suggestion_title}")
                    st.markdown(f"**Category:** {category}")
                    st.markdown(f"**Priority:** {priority}")
                    st.markdown(f"**Submitted by:** {name} (Flat: {flat_no})")
                    st.markdown(f"**Details:** {details}")
            else:
                st.error("Please fill all required fields (*)")
    
    st.markdown("---")
    st.markdown("### 📊 Recent Suggestions Status")
    
    status_data = {
        "Suggestion": ["Install EV Charging Stations", "Weekly Yoga Classes", "Renovate Children's Park"],
        "Category": ["Amenities", "Community Events", "Maintenance"],
        "Status": ["Approved", "Under Review", "Implemented"],
        "Update": ["Will be installed by Dec 2023", "Committee reviewing feasibility", "Completed in Aug 2023"]
    }
    
    st.table(pd.DataFrame(status_data))

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**© 2023 Manzil C G H Society**")
    
with footer_col2:
    st.markdown("**Designed for Community Harmony**")
    
with footer_col3:
    st.markdown("**🏠 Building Community, Creating Home**")

import streamlit as st

def apply_custom_css():
    """Apply custom CSS styles to the Streamlit app"""
    st.markdown("""
    <style>
    /* Main styles */
    .stApp {
        background-color: #f5f7fa;
    }
    
    /* Header styles */
    .main-header {
        color: #2c3e50;
        padding-bottom: 10px;
        border-bottom: 3px solid #3498db;
        margin-bottom: 30px;
    }
    
    /* Card styles */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 4px solid #3498db;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    
    /* Button styles */
    .stButton > button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Table styles */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .dataframe th {
        background-color: #2c3e50 !important;
        color: white !important;
        font-weight: 600 !important;
    }
    
    .dataframe tr:nth-child(even) {
        background-color: #f8f9fa !important;
    }
    
    .dataframe tr:hover {
        background-color: #e8f4fc !important;
    }
    
    /* Form styles */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #2c3e50;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom badge for owner/tenant */
    .owner-badge {
        background-color: #d4edda;
        color: #155724;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8em;
        font-weight: 600;
    }
    
    .tenant-badge {
        background-color: #fff3cd;
        color: #856404;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8em;
        font-weight: 600;
    }
    
    /* Status indicators */
    .status-approved {
        color: #27ae60;
        font-weight: bold;
    }
    
    .status-pending {
        color: #f39c12;
        font-weight: bold;
    }
    
    .status-rejected {
        color: #e74c3c;
        font-weight: bold;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .card {
            padding: 15px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

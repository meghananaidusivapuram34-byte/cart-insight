import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(
    page_title="DropOff Insight AI",
    page_icon="🛒",
    layout="wide"
)

# --------------------
# SESSION VARIABLES
# --------------------

if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if "cart_added" not in st.session_state:
    st.session_state.cart_added = False

if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

# --------------------
# HEADER
# --------------------

st.title("🛒 DropOff Insight AI")
st.caption("Understand why customers leave without purchasing")

# --------------------
# PRODUCT SECTION
# --------------------

col1, col2 = st.columns([2, 1])

with col1:

    st.image(
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=1200",
        use_container_width=True
    )

    st.subheader("Gaming Laptop Pro X")

    st.markdown("### ₹89,999")

    st.write("""
    High-performance gaming laptop with:

    - Intel Core i7
    - RTX Graphics
    - 16GB RAM
    - 1TB SSD
    - 144Hz Display
    """)

    if st.button("Add To Cart"):

        st.session_state.cart_added = True
        st.success("Added to cart successfully!")

with col2:

    st.subheader("User Activity")

    st.session_state.clicks += 1

    duration = (
        datetime.now() -
        st.session_state.start_time
    ).seconds

    st.metric(
        "Time On Page",
        f"{duration} sec"
    )

    st.metric(
        "Interactions",
        st.session_state.clicks
    )

    st.metric(
        "Cart Added",
        "Yes" if st.session_state.cart_added else "No"
    )

# --------------------
# FEEDBACK SECTION
# --------------------

st.divider()

st.header("Customer Feedback")

reason = st.selectbox(
    "What stopped you from purchasing?",
    [
        "Too Expensive",
        "Missing Information",
        "Shipping Concerns",
        "Not Enough Reviews",
        "Found Better Alternative",
        "Just Browsing"
    ]
)

comment = st.text_area(
    "Additional Feedback"
)

if st.button("Submit Feedback"):

    st.session_state.feedbacks.append({
        "Reason": reason,
        "Comment": comment
    })

    st.success("Feedback Submitted")

# --------------------
# AI INSIGHT ENGINE
# --------------------

def generate_insight():

    time_spent = (
        datetime.now() -
        st.session_state.start_time
    ).seconds

    clicks = st.session_state.clicks

    if st.session_state.cart_added:
        return "Customer successfully added product to cart."

    if time_spent > 60:
        return """
        Customer spent considerable time reviewing
        the product but did not convert.
        Consider improving product information.
        """

    if clicks > 10:
        return """
        High engagement detected.
        Customer may have concerns about
        pricing or trust signals.
        """

    return """
    Customer showed interest but left early.
    Improve visuals, reviews and value proposition.
    """

st.divider()

st.header("🤖 AI Insight")

st.info(generate_insight())

# --------------------
# DASHBOARD
# --------------------

st.divider()

st.header("Business Dashboard")

visitors = 1200
cart_adds = 350
dropoffs = visitors - cart_adds

c1, c2, c3 = st.columns(3)

c1.metric("Visitors", visitors)
c2.metric("Cart Adds", cart_adds)
c3.metric("Drop-Offs", dropoffs)

# --------------------
# FEEDBACK ANALYTICS
# --------------------

if len(st.session_state.feedbacks) > 0:

    st.subheader("Feedback Analysis")

    df = pd.DataFrame(
        st.session_state.feedbacks
    )

    reason_count = (
        df["Reason"]
        .value_counts()
        .reset_index()
    )

    reason_count.columns = [
        "Reason",
        "Count"
    ]

    fig = px.pie(
        reason_count,
        names="Reason",
        values="Count",
        title="Drop-Off Reasons"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# --------------------
# RECOMMENDATIONS
# --------------------

st.divider()

st.header("📈 Recommendations")

recommendations = [
    "Add more product reviews",
    "Show shipping cost earlier",
    "Improve product specifications",
    "Add product comparison table",
    "Provide discount offers",
    "Display warranty information prominently"
]

for item in recommendations:
    st.success(item)

# --------------------
# FOOTER
# --------------------

st.divider()

st.caption(
    "DropOff Insight AI | Hackathon MVP"
)
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter")
st.markdown("**Rising Demand + Low Competition Research Tool**")
st.caption("Best free accessible data sources for organic Redbubble success")

# ====================== USEFUL FREE TREND SOURCES ======================
st.subheader("🔗 Best Free Redbubble Trend Sources (2026)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **1. Bubble Trends**  
    [→ Open BubbleTrends](https://www.thebubbletrends.com/)
    
    **2. BubbleSpider**  
    [→ Popular Keywords](https://bubblespider.com/keyword-research/popular-keywords)
    """)

with col2:
    st.markdown("""
    **3. Top Bubble Index**  
    [→ Check Index](https://www.topbubbleindex.com/)
    
    **4. Insight Factory**  
    [→ Daily Trends](https://insightfactory.app/redbubble-trends/)
    """)

st.divider()

# ====================== MAIN KEYWORD ANALYSIS ======================
keyword = st.text_input("Enter your keyword or niche", 
                       placeholder="e.g. pickleball grandma, anxiety cat, booktok girl")

if st.button("🚀 Analyze This Niche", type="primary", use_container_width=True):
    if keyword:
        st.success(f"**Analyzing: {keyword}**")

        st.subheader("Step 1: Check Current Competition")
        st.markdown(f"[🔗 Open Redbubble Search](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
        
        results = st.number_input("Paste number of results from Redbubble", 
                                min_value=0, value=8000, step=500, help="Look for 'X results' or 'of X designs'")

        # Smart Scoring
        if results < 3500:
            opp = 88
            status = "🟢 Excellent Low Competition"
        elif results < 7000:
            opp = 72
            status = "🟡 Good Opportunity"
        elif results < 14000:
            opp = 48
            status = "🟠 Competitive"
        else:
            opp = 28
            status = "🔴 High Competition"

        st.metric("**Opportunity Score**", f"{opp}/100", status)

        # Strategy
        st.subheader("🎯 Recommended Action Plan")
        if opp >= 75:
            st.success("**Strong Green Light** - Create 5-10 designs in this niche")
        elif opp >= 55:
            st.warning("**Worth Testing** - Focus on unique angles")
        else:
            st.error("**High Competition** - Only enter with very strong unique design")

        st.subheader("Best Design Styles for This Niche")
        st.write("• Retro Vintage Style")
        st.write("• Funny / Sarcastic")
        st.write("• Minimal Aesthetic")
        st.write("• Cute Kawaii")
        st.write("• Dark Humor")

        st.subheader("Recommended Title Formula")
        st.code(f"{keyword.title()} Gift | Funny Retro {keyword.title()} T-Shirt Sticker Hoodie")

        st.subheader("High-Performance Tags")
        tags = [keyword.lower(), f"{keyword.lower()} gift", f"funny {keyword.lower()}", 
                f"{keyword.lower()} vintage", f"{keyword.lower()} retro", f"{keyword.lower()} aesthetic"]
        st.code("\n".join(tags))

    else:
        st.warning("Please enter a keyword")

st.info("**Pro Tip**: Best results come from niches with **< 7000 results** + rising interest on BubbleTrends or Google Trends.")

st.caption("Personal Research Tool | Updated for 2026")

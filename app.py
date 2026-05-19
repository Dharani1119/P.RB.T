import streamlit as st
from pytrends.request import TrendReq
import time

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter")
st.markdown("**Rising Demand + Low Competition Niche Finder**")

keyword = st.text_input("Enter your main keyword or niche", 
                       placeholder="e.g. pickleball grandma, anxiety cat, booktok girl")

if st.button("🚀 Analyze This Niche", type="primary", use_container_width=True):
    if keyword:
        with st.spinner("Connecting to Google Trends..."):
            try:
                # More stable connection
                pytrends = TrendReq(hl='en-US', tz=360, retries=3, backoff_factor=0.5)
                
                pytrends.build_payload([keyword], cat=0, timeframe='today 12-m')
                interest = pytrends.interest_over_time()
                
                if interest.empty:
                    st.warning("No trend data found for this keyword. Try a more popular term.")
                else:
                    avg_score = int(interest[keyword].mean())
                    is_rising = interest[keyword].iloc[-3:].mean() > interest[keyword].iloc[:3].mean()

                    st.success("✅ Successfully fetched trend data!")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Demand Score", f"{avg_score}/100", "Rising 🔥" if is_rising else "Stable")
                    with col2:
                        st.metric("Trend", "Strong" if avg_score > 60 else "Medium" if avg_score > 40 else "Low")

                    # Rest of the tool (competition, suggestions, etc.)
                    st.subheader("Redbubble Competition")
                    st.markdown(f"[Check on Redbubble](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
                    results = st.number_input("Paste number of results", min_value=0, value=8000, step=100)

                    score = 85 if results < 5000 else 65 if results < 10000 else 40
                    if avg_score > 60: score += 15
                    score = min(95, score)

                    st.metric("Opportunity Score", f"{score}/100")

                    st.subheader("Recommended Design Styles")
                    st.write("- Retro Vintage")
                    st.write("- Funny / Sarcastic")
                    st.write("- Minimal Aesthetic")
                    st.write("- Cute Kawaii")

            except Exception as e:
                st.error("⚠️ Could not connect to Google Trends.")
                st.info("This usually happens due to temporary blocking. Please wait 1-2 minutes and try again.")
                st.info("Tip: Use more general keywords like 'cat' instead of very specific ones.")

    else:
        st.warning("Please enter a keyword")

st.caption("Personal Tool | Try again if Trends fail")

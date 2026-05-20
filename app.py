import streamlit as st

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter")
st.markdown("**Real & Effective Niche Research Tool**")
st.caption("Updated - Now Properly Calculates Based on Your Input")

keyword = st.text_input("Enter your main keyword or niche", 
                       placeholder="e.g. pickleball grandma, anxiety cat, booktok girl")

if st.button("🚀 Analyze This Niche", type="primary", use_container_width=True):
    if keyword:
        st.success(f"**Analyzing: {keyword.title()}**")

        st.subheader("Redbubble Competition")
        st.markdown(f"[🔗 Open Redbubble Search](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
        
        results = st.number_input("Enter number of results from Redbubble", 
                                min_value=0, value=8000, step=100, 
                                help="Example: 12456 or 6750")

        # === FIXED SCORING LOGIC ===
        if results < 3000:
            score = 90
            rating = "🟢 Excellent Opportunity"
        elif results < 6000:
            score = 78
            rating = "🟢 Very Good"
        elif results < 10000:
            score = 62
            rating = "🟡 Good"
        elif results < 20000:
            score = 45
            rating = "🟠 Competitive"
        else:
            score = 28
            rating = "🔴 Very Tough"

        st.metric("**Opportunity Score**", f"{score}/100", rating)

        # Long-tail & Strategy
        st.subheader("Smart Long-Tail Keywords")
        long_tails = [
            f"{keyword} gift", f"funny {keyword}", f"retro {keyword}", 
            f"vintage {keyword}", f"sarcastic {keyword}", f"cute {keyword}",
            f"{keyword} for women", f"{keyword} for men"
        ]
        for lt in long_tails:
            st.write(f"• **{lt}**")

        st.subheader("Recommended Strategy")
        if score >= 75:
            st.success("**Strong Green Light** - Create multiple designs")
        elif score >= 60:
            st.warning("**Good Chance** - Worth testing")
        else:
            st.error("High competition. Use more specific long-tail versions.")

        st.subheader("Best Title Formula")
        st.code(f"Funny Retro {keyword.title()} Gift | Vintage {keyword.title()} T-Shirt Sticker")

        st.subheader("Best Tags")
        tags = [keyword.lower(), f"funny {keyword.lower()}", f"{keyword.lower()} gift", 
                f"retro {keyword.lower()}", f"vintage {keyword.lower()}", f"{keyword.lower()} shirt"]
        st.code("\n".join(tags))

    else:
        st.warning("Please enter a keyword")

st.info("Tip: Lower the number = Higher opportunity score. Try keywords with under 7000 results for best chance.")
st.caption("Fixed Version | Score now updates based on your input")

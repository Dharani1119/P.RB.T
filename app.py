import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter")
st.markdown("**Best Version** — Rising Demand + Low Competition + Ready-to-Use Strategy")
st.caption("Real data → Actionable strategy for organic sales")

# ====================== INPUT ======================
keyword = st.text_input("Enter your main keyword or niche", 
                       placeholder="e.g. pickleball grandma, anxiety cat, booktok girl, mental health nurse")

analyze = st.button("🚀 Deep Analyze & Generate Strategy", type="primary", use_container_width=True)

if analyze and keyword:
    with st.spinner("Analyzing real trends & competition..."):
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            pytrends.build_payload([keyword], cat=0, timeframe='today 12-m')
            interest = pytrends.interest_over_time()
            
            avg_score = int(interest[keyword].mean()) if not interest.empty else 45
            is_rising = interest[keyword].iloc[-3:].mean() > interest[keyword].iloc[:3].mean() if not interest.empty else False

            # Redbubble Input
            st.subheader("Redbubble Competition")
            st.markdown(f"[🔗 Check Live Results](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
            results_count = st.number_input("Paste number of results from Redbubble", 
                                          min_value=0, value=6500, step=100)

            # Core Scoring
            demand_score = avg_score
            comp_score = 90 if results_count < 3500 else 75 if results_count < 7000 else 50 if results_count < 14000 else 25
            niche_score = int((demand_score * 0.55) + (comp_score * 0.45))

            # Final Verdict
            if niche_score >= 78 and is_rising:
                verdict = "🟢 EXCELLENT - Strong Organic Potential"
            elif niche_score >= 65:
                verdict = "🟡 GOOD - Worth Creating Multiple Designs"
            elif niche_score >= 50:
                verdict = "🟠 Average - Needs Strong Design"
            else:
                verdict = "🔴 Difficult - High Competition"

            # Display Scores
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.metric("Demand (Trends)", f"{demand_score}/100", "Rising" if is_rising else "")
            with c2: st.metric("Competition", f"{results_count:,} designs")
            with c3: st.metric("Niche Score", f"{niche_score}/100")
            with c4: st.metric("Recommendation", verdict.split(" - ")[0])

            st.success(verdict)

            # ====================== LONG-TAIL KEYWORDS ======================
            st.subheader("🎯 High-Potential Long-Tail Keywords")
            long_tails = [
                f"{keyword} gift", f"funny {keyword}", f"{keyword} vintage", 
                f"{keyword} retro", f"{keyword} aesthetic", f"{keyword} lover",
                f"{keyword} 2026", f"sarcastic {keyword}", f"cute {keyword}"
            ]
            for lt in long_tails:
                st.write(f"• **{lt}**")

            # ====================== PRODUCT RECOMMENDATION ======================
            st.subheader("🛍️ Best Products to Upload First")
            st.write("**Priority Order:**")
            products = ["Sticker", "T-Shirt", "Hoodie", "Mug", "Poster", "Phone Case"]
            for i, p in enumerate(products, 1):
                st.write(f"{i}. **{p}**")

            # ====================== DESIGN IDEAS ======================
            st.subheader("🎨 Best Design Styles to Create")
            designs = ["Retro Vintage", "Funny Sarcastic", "Minimal Aesthetic", 
                      "Kawaii/Cute", "Dark Humor", "Watercolor", "Typography Quote"]
            for d in designs:
                st.write(f"• **{d}** version of **{keyword}**")

            # ====================== TITLE & DESCRIPTION ======================
            st.subheader("📝 Ready-to-Use Title Formula")
            st.code(f"{keyword.title()} Gift | Funny Retro Vintage {keyword.title()} T-Shirt Sticker")

            st.subheader("Best Tags (Copy & Paste)")
            tags = [keyword.lower(), f"{keyword.lower()} gift", f"funny {keyword.lower()}", 
                   f"{keyword.lower()} vintage", f"{keyword.lower()} retro", f"{keyword.lower()} aesthetic",
                   f"{keyword.lower()} shirt", f"{keyword.lower()} sticker"]
            st.code("\n".join(tags))

            st.info("**Pro Tip**: Use 2-3 long-tail keywords in title + 10-15 good tags = Best chance for organic traffic.")

        except:
            st.error("Could not fetch trends. Please try again later.")

else:
    st.info("Enter a keyword and click **Deep Analyze** to get full strategy.")

st.caption("Personal Pro Tool | Data-Driven | Focused on Organic Sales")

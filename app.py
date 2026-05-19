import streamlit as st

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter v5")
st.markdown("**Smart Niche Analyzer + Strategy Generator**")
st.caption("Rising Demand • Low Competition • Ready-to-Upload Strategy")

# ====================== GREEN LIGHT NICHES ======================
st.subheader("🌟 Green Light Niches Right Now (Low Comp + Rising)")
green_niches = ["Pickleball Grandma", "Emotional Support Demon", "Anxiety Cat", 
                "Sarcastic Teacher", "Cottagecore Frog", "Booktok Grandma", "Golf Grandpa"]
for niche in green_niches:
    st.markdown(f"• **{niche}**")

st.divider()

keyword = st.text_input("Enter your main keyword or niche", 
                       placeholder="e.g. unicorn, pickleball grandma, anxiety cat")

if st.button("🚀 Deep Analyze & Generate Full Strategy", type="primary", use_container_width=True):
    if keyword:
        st.success(f"**Analyzing: {keyword.title()}**")

        # Competition Input
        st.subheader("Step 1: Redbubble Competition")
        st.markdown(f"[🔗 Search on Redbubble](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
        results = st.number_input("Paste number of results", min_value=0, value=8000, step=500)

        # Smart Scoring
        demand = 65  # Default (you can adjust manually if you checked Trends)
        competition_score = 90 if results < 3500 else 75 if results < 7000 else 50 if results < 14000 else 25
        niche_score = int((demand * 0.5) + (competition_score * 0.5))

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Niche Difficulty", f"{niche_score}/100")
        with col2:
            st.metric("Competition Level", f"{results:,} designs")
        with col3:
            if niche_score >= 78:
                st.success("🟢 EXCELLENT")
            elif niche_score >= 60:
                st.warning("🟡 GOOD")
            else:
                st.error("🔴 TOUGH")

        # ====================== 1. LONG-TAIL KEYWORDS ======================
        st.subheader("🎯 High-Potential Long-Tail Keywords")
        long_tails = [
            f"{keyword} gift", f"funny {keyword}", f"{keyword} vintage", 
            f"{keyword} retro", f"{keyword} aesthetic", f"{keyword} lover",
            f"sarcastic {keyword}", f"cute {keyword}", f"mental health {keyword}",
            f"{keyword} 2026"
        ]
        for lt in long_tails:
            st.write(f"• **{lt}**")

        # ====================== 2. DESIGN RECOMMENDATIONS ======================
        st.subheader("🎨 Best Design Styles to Create")
        designs = ["Retro Vintage", "Funny Sarcastic", "Minimal Aesthetic", 
                  "Cute Kawaii", "Dark Humor", "Watercolor", "Typography"]
        for d in designs:
            st.write(f"• **{d}**")

        # ====================== 3. PRODUCT RECOMMENDATION ======================
        st.subheader("🛍️ Best Products to Upload First")
        st.write("**Priority Order:**")
        st.write("1. **Stickers** (Easiest to rank)")
        st.write("2. **T-Shirts**")
        st.write("3. **Hoodies**")
        st.write("4. **Mugs**")
        st.write("5. **Posters**")

        # ====================== 4. TITLE & TAGS ======================
        st.subheader("📝 Recommended Title")
        st.code(f"{keyword.title()} Gift | Funny Retro Vintage {keyword.title()} T-Shirt Sticker")

        st.subheader("🏷️ Best Tags (Copy & Paste)")
        tags = [keyword.lower(), f"{keyword.lower()} gift", f"funny {keyword.lower()}", 
                f"{keyword.lower()} vintage", f"{keyword.lower()} retro", 
                f"{keyword.lower()} aesthetic", f"{keyword.lower()} shirt"]
        st.code("\n".join(tags))

        # Final Advice
        if niche_score >= 75:
            st.success("**GO FOR IT** - This niche has strong potential!")
        elif niche_score >= 55:
            st.warning("**Test it** with 3-5 designs first.")
        else:
            st.error("Consider more specific long-tail versions of this keyword.")

    else:
        st.warning("Please enter a keyword")

st.caption("Personal Pro Tool | Designed for Organic Redbubble Success")

import streamlit as st

st.set_page_config(page_title="Redbubble Pro Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Pro Hunter")
st.markdown("**Real Organic Winning Niche Finder**")

# 1. TRENDING RISING KEYWORDS SECTION
st.subheader("1. 🔥 Trending & Rising Keywords Right Now")
trending = [
    "Pickleball Grandma", "Anxiety Cat", "Emotional Support Demon", 
    "Booktok Girl", "Sarcastic Teacher", "Cottagecore Frog", 
    "Golf Grandpa", "Plant Lady Era", "Mental Health Nurse"
]
for item in trending:
    st.markdown(f"• **{item}**")

st.divider()

# 2. KEYWORD INPUT
keyword = st.text_input("2. Enter your keyword or niche", 
                       placeholder="e.g. pickleball grandma, anxiety cat")

if st.button("🚀 Analyze This Keyword", type="primary", use_container_width=True):
    if keyword:
        st.success(f"**Analyzing: {keyword.title()}**")

        # 3. Redbubble Results (Manual for now - Automatic is unstable)
        st.subheader("3. Redbubble Competition (Live)")
        st.markdown(f"[Open Redbubble Search →](https://www.redbubble.com/shop/{keyword.replace(' ', '+')})")
        results = st.number_input("Enter number of designs/results you see", 
                                min_value=0, value=8000, step=100)

        # 4. Competition Color
        if results < 4000:
            comp_color = "🟢 Low Competition"
            comp_status = "Green"
        elif results < 9000:
            comp_color = "🟠 Medium Competition"
            comp_status = "Orange"
        else:
            comp_color = "🔴 High Competition"
            comp_status = "Red"

        # 5. Demand Color (Simplified for now)
        demand_color = "🟫 High Demand" if results < 8000 else "🟨 Medium Demand" if results < 15000 else "⚪ Low Demand"

        st.metric("Competition", comp_color)
        st.metric("Demand Level", demand_color)

        # Final Chance
        final_score = 85 if results < 4000 else 65 if results < 9000 else 35
        if final_score >= 75:
            chance = "🟢 **High Chance** of Organic Sales"
        elif final_score >= 55:
            chance = "🟡 **Medium Chance**"
        else:
            chance = "🔴 **Low Chance**"

        st.success(chance)

        # 6. SEO Elements
        st.subheader("6. SEO Optimized Elements")

        st.subheader("Recommended Title")
        st.code(f"Funny Retro {keyword.title()} Gift | Vintage {keyword.title()} T-Shirt Sticker")

        st.subheader("High Performance Tags")
        tags = [
            keyword.lower(),
            f"funny {keyword.lower()}",
            f"{keyword.lower()} gift",
            f"retro {keyword.lower()}",
            f"vintage {keyword.lower()}",
            f"{keyword.lower()} shirt",
            f"sarcastic {keyword.lower()}"
        ]
        st.code("\n".join(tags))

        st.subheader("SEO Description")
        st.code(f"""
{keyword.title()} - Perfect funny retro gift for {keyword} lovers!

This vintage style {keyword} design is great for birthdays, Christmas or everyday wear.
Available on t-shirts, stickers, hoodies and more.
        """.strip())

    else:
        st.warning("Please enter a keyword")

st.caption("Note: Automatic Redbubble count is unstable. Manual input is more accurate for now.")

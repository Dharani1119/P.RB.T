import streamlit as st
import pandas as pd
import time
import re
from pytrends.request import TrendReq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config(page_title="Redbubble Hunter", layout="wide", page_icon="🔥")

st.title("🔥 Redbubble Hunter")
st.markdown("**Find Winning Niches for Redbubble (Organic Traffic Only)**")
st.caption("Google Trends + Real Redbubble Competition Analysis")

keyword = st.text_input("Enter your keyword or niche idea", 
                       placeholder="e.g. pickleball grandma, cat astronaut, booktok girl, mental health nurse")

col1, col2 = st.columns([3,1])
with col1:
    analyze_button = st.button("🚀 Analyze This Niche", type="primary", use_container_width=True)

if analyze_button and keyword:
    with st.spinner("Fetching Google Trends + Scraping Redbubble..."):
        try:
            # Google Trends
            pytrends = TrendReq(hl='en-US', tz=360)
            pytrends.build_payload([keyword], cat=0, timeframe='today 12-m')
            interest = pytrends.interest_over_time()
            
            avg_interest = int(interest[keyword].mean()) if not interest.empty else 0
            trend_status = "Rising 🔥" if avg_interest > 60 else "Stable" if avg_interest > 35 else "Low"

            # Redbubble Scrape
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            search_url = f"https://www.redbubble.com/shop/{keyword.replace(' ', '+')}"
            driver.get(search_url)
            time.sleep(5)
            
            try:
                results_text = driver.find_element("xpath", "//span[contains(text(), 'results')]").text
                results_count = int(re.sub(r'[^0-9]', '', results_text))
            except:
                results_count = "N/A (Try again later)"

            driver.quit()

            # Opportunity Score
            comp = results_count if isinstance(results_count, int) else 15000
            opportunity_score = max(10, min(95, 100 - (comp // 120)))
            if avg_interest > 65:
                opportunity_score += 15
            opportunity_score = min(98, opportunity_score)

            # Verdict
            if opportunity_score >= 75 and avg_interest >= 55:
                verdict = "🟢 EXCELLENT Organic Chance"
            elif opportunity_score >= 55 and avg_interest >= 45:
                verdict = "🟡 Good Chance"
            else:
                verdict = "🔴 High Competition - Tough"

            # Results
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Google Trends Score", f"{avg_interest}/100", trend_status)
            with c2:
                st.metric("Redbubble Designs", f"{results_count:,}" if isinstance(results_count, int) else results_count)
            with c3:
                st.metric("Opportunity Score", f"{opportunity_score}/100", verdict)

            st.success(verdict)

            # Recommended Tags
            st.subheader("Recommended Long-Tail Tags (Copy-Paste)")
            base_tags = [keyword, f"{keyword} gift", f"{keyword} vintage", f"{keyword} aesthetic", 
                        f"{keyword} retro", f"{keyword} funny", f"{keyword} cute", f"{keyword} 2026"]
            st.code("\n".join(base_tags), language=None)

            st.info("**Pro Tip**: Best niches usually have < 8,000 results + Trends score > 55")

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Sometimes Redbubble blocks scraping. Try again in a few minutes.")

else:
    st.info("Enter a keyword above and click Analyze")

st.caption("Personal Tool • Free for your use only")

import streamlit as st
from meta_ai_api import MetaAI

def main():
    # Set up page config
    st.set_page_config(page_title="Weather Information", page_icon="🌤️", layout="centered")
    
    # Custom styling
    st.markdown("""
        <style>
            .main-title { text-align: center; font-size: 2rem; font-weight: bold; }
            .info-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    
    # Title and description
    st.markdown("<h1 class='main-title'>🌍 Global Weather Information</h1>", unsafe_allow_html=True)
    st.markdown(""" 
    Get real-time weather updates for any country around the world. Just enter the country name and hit the button!
    """)
    
    # Initialize MetaAI
    llm = MetaAI()
    
    # Create input field
    user_input = st.text_input("Enter the country name:", placeholder="e.g., pakistan")
    
    # Create button
    if st.button("Get Weather Info", use_container_width=True):
        if user_input:
            # Show loading spinner
            with st.spinner("Fetching weather information..."):
                prompt = f"""
                You are an AI assistant providing weather details for countries and cities. The user asked for {user_input}.
                Provide the weather details in the following format:
                
                - **Temperature:** 20°C
                - **Weather:** Sunny
                - **Wind:** 10 km/h
                - **Humidity:** 50%
                - **Precipitation:** 0 mm
                - **Cloud Cover:** 50%
                - **Wind Direction:** North
                - **Wind Speed:** 10 km/h
                - **Visibility:** 10 km
                - **Pressure:** 1000 hPa
                - **Dew Point:** 10°C
                - **UV Index:** 10
                - **Sunrise:** 06:00
                - **Sunset:** 18:00
                - **Moon Phase:** Full moon
                - **Moon Illumination:** 100%
                
                If the user asks something unrelated, inform them that you can only provide weather information.
                """
                
                response = llm.prompt(prompt)
                
                # Extract temperature from the response
                temperature = response["message"].split("\n")[0].replace("- **Temperature:** ", "")
                
                # Display the response in a structured format
                st.markdown("### 🌤️ Weather Information for " + user_input)
                st.markdown(f"""
                    <div class='info-box'>
                    <h2>Temperature: {temperature}</h2>
                    {response["message"].replace("- ", "<br>✔️ ").replace(f"**Temperature:** {temperature}", "")}
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a country name!")

if __name__ == "__main__":
    main()

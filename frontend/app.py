
import streamlit as st
import requests


ELEVENLABS_API_KEY = "sk_4786f1755ccefcc74c939949e8d72fd67040a0a9ae8e0975"


voice_id = "29vD33N1CtxCmqQRPOHJ"

st.title("🎤 Alisha Agrahari")
st.write("Clone a voice from a 10-second audio sample and generate speech.")

# Input text
text_input = st.text_area("Enter text to be spoken in the cloned voice")

# Generate voice button
if st.button("🔊 Generate Voice"):
    if text_input:
        response = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
            headers={
                "xi-api-key": ELEVENLABS_API_KEY,  # Correct header format
                "Content-Type": "application/json"
            },
            json={
                "text": text_input,
                "model_id": "eleven_monolingual_v1"
            }
        )
        if response.status_code == 200:
            st.audio(response.content, format="audio/mp3")
        else:
            st.error(f"Error: {response.json()}")  # Print exact API error
    else:
        st.error("Please enter text.")

import streamlit as st
import tempfile
import os

global lyrics
lyrics = ""
st.session_state["lyrics"] = '''Versent, the technology company 
                with an eco-friendly bent… 
                with a green intent. 

                Reduce, recycle, reinvent... Versent.'''

def generate_lyrics_from_prompt(prompt):
    # TODO: Use Pynecone or other method to generate lyrics based on the prompt
    lyrics = '''Versent, the technology company 
                with an eco-friendly bent… 
                with a green intent. 

                Reduce, recycle, reinvent... Versent.'''
    return lyrics

def generate_jingle(lyrics, musical_style):
    # TODO: Generate jingle based on lyrics and musical style
    # Return the path to the generated jingle file
    jingle_path = "assets/Lazer-Beam-with-Voicemod-Text-to-Song.mp3"
    return jingle_path

def main():
    global lyrics 
    st.title("Catchy Jingle Generator")

    # Company information
    company_name = st.text_input("Company Name", value="Versent")
    mission_statement = st.text_area("Company Mission Statement", value="We care about sustainability")

    # Prompt
    prompt = st.text_area("Prompt for Lyrics", value="Write a jingle for a professional services technology company called {{company_name}} that {{mission_statement}}. Keep it simple and easy to sing Use figures of speech such as rhyme, alliteration, onomatopoeia, etc. The jingle should be 3 lines long.")

    # Generate Lyrics
    btn_lyrics = st.button("Generate Lyrics")
    ta_lyrics = st.text_area("Lyrics", value=st.session_state["lyrics"], height=200)
    # ta_lyrics = st.text_area("Lyrics", value="", height=200)

    if btn_lyrics:
        lyrics = generate_lyrics_from_prompt(prompt)
        st.session_state["lyrics"] = lyrics
        # ta_lyrics = lyrics
    
    # Musical Style
    musical_style = st.radio("Musical Style", options=["Christmas", "Classical", "Electronic", "Pop", "Urban", "Rock"])

    # Generate Jingle
    if st.button("Generate Jingle"):
        jingle_path = generate_jingle(lyrics, musical_style)
        st.audio(jingle_path)

        # # Download button
        # with st.beta_expander("Download"):
        #     st.audio(jingle_path, format="audio/mp3", start_time=0)

if __name__ == '__main__':
    main()

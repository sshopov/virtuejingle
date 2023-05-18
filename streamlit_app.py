import streamlit as st
#from gtts import gTTS
import os, random


# Step one - Company information
def company_information():
    st.header("Company Information")
    company_name = st.text_input("Company Name", key=random.randint(0, 10000))
    mission_statement = st.text_area("Company Mission Statement", key=random.randint(0, 10000))
    
    if st.button("Next", key=random.randint(0, 10000)):
        return company_name, mission_statement
    return "",""
    

# Step two - Lyrics
def generate_lyrics():
    st.header("Generate Lyrics")
    lyrics = st.text_area("Jingle Lyrics")
    
    if st.button("Previous"):
        return "previous"
    
    if st.button("Regenerate"):
        # Use AI model or algorithm to generate lyrics based on the company's mission statement
        generated_lyrics = generate_lyrics_from_mission_statement('mission_statement')
        lyrics = st.text_area("Jingle Lyrics", value=generated_lyrics)
    
    if st.button("Next"):
        return lyrics
    

# Step three - Musical style
def choose_style():
    st.header("Choose Musical Style")
    musical_styles = ["Christmas", "Classical", "Electronic", "Pop", "Urban", "Rock"]
    selected_style = st.selectbox("Select Musical Style", musical_styles)
    
    if st.button("Previous"):
        return "previous"
    
    if st.button("Next"):
        return selected_style
    

# Step four - Jingle
def generate_jingle():
    st.header("Generated Jingle")
    
#     # Generate jingle based on the selected musical style and lyrics
#     jingle = generate_jingle_with_style(lyrics, selected_style)
    
#     # Save jingle as an mp3 file
#     jingle_file = "generated_jingle.mp3"
#     jingle.save(jingle_file)
    
    jingle_file = "https://us-tuna-sounds-files.voicemod.net/e762cb4c-ea4d-4e23-a430-4deb87d90406-1683925352862.mp3"
    
    # Display audio player for the generated jingle
    st.audio(jingle_file)
    
    if st.button("Previous"):
        return "previous"
    
    if st.button("Download"):
        # Download the generated jingle
        #st.markdown(get_download_link(jingle_file), unsafe_allow_html=True)
        st.markdown(jingle_file, unsafe_allow_html=True)


# Main application flow
def main():
    st.title("Catchy Jingle Generator")
    
    current_step = 0
    companyname = ""
    missionstatement = ""
    lyrics = ""
    selected_style = ""
    
    while current_step < 4:
        if current_step == 0:
            companyname, missionstatement = company_information()
            if companyname and missionstatement:
                current_step += 1
        elif current_step == 1:
            lyrics = generate_lyrics()
            if lyrics == "previous":
                current_step -= 1
            elif lyrics:
                current_step += 1
        elif current_step == 2:
            selected_style = choose_style()
            if selected_style == "previous":
                current_step -= 1
            elif selected_style:
                current_step += 1
        elif current_step == 3:
            generate_jingle()
            if st.button("Previous"):
                current_step -= 1

# Helper function to generate lyrics based on the company's mission statement
def generate_lyrics_from_mission_statement(mission_statement):
    # Use AI model or algorithm to generate lyrics based on the mission statement
    generated_lyrics = "Sample generated lyrics based on the mission statement"
    return generated_lyrics

# Helper function to generate jingle based on the musical style and lyrics
def generate_jingle_with_style(lyrics, selected_style):
    # Generate jingle based on the musical style and lyrics
    # (Replace this with your actual implementation or use a suitable library)
    jingle = f"Generated jingle in {selected_style} style: {lyrics}"
    return jingle

if __name__ == '__main__':
    main()

import streamlit as st
from speech_to_text import transcribe_audio
from semantic_eval import calculate_similarity
from audio_utils import extract_audio_features, create_waveform
from fluency_analysis import count_filler_words
from scoring_engine import calculate_final_score
from report_generator import generate_report
from pydub import AudioSegment
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎙️",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎙️ Voice Based Concept Understanding Analyser")
st.write(
    "Upload your explanation audio and evaluate your conceptual understanding."
)

# -----------------------------
# Topic Selection
# -----------------------------
topics = [
    "Machine Learning",
    "Deep Learning",
    "Cloud Computing",
    "Python Programming",
    "Data Science"
]

selected_topic = st.selectbox(
    "Select Topic",
    topics
)

# -----------------------------
# Audio Upload
# -----------------------------
audio_file = st.file_uploader(
    "Upload Audio File",
    type=["mp3", "wav", "m4a"]
)

# -----------------------------
# Main Processing
# -----------------------------
if audio_file is not None:

    st.audio(audio_file)


    if st.button("Analyze Explanation"):


        with st.spinner("Converting speech to text..."):


            # Save uploaded file temporarily
            suffix = os.path.splitext(audio_file.name)[1]


            os.makedirs("uploads", exist_ok=True)

            upload_path = os.path.join("uploads", audio_file.name)

            with open(upload_path, "wb") as f:
                f.write(audio_file.getbuffer())

            audio_path = upload_path



            # Convert mp3 to wav
            if suffix == ".mp3":

                sound = AudioSegment.from_mp3(audio_path)

                wav_path = audio_path.replace(
                    ".mp3",
                    ".wav"
                )

                sound.export(
                    wav_path,
                    format="wav"
                )

                audio_path = wav_path



            text = transcribe_audio(audio_path)
            



        st.success("Transcription Completed!")

        st.subheader("📝 Transcribed Text")
        st.write(text)

        if not text.startswith("Error"):
            reference_answers = {
                "Machine Learning":
                "Machine learning is a branch of artificial intelligence that enables computers to learn from data without being explicitly programmed. It uses algorithms to identify patterns and make predictions.",

                "Deep Learning":
                "Deep learning is a subset of machine learning that uses neural networks with multiple layers to automatically learn complex patterns from large amounts of data.",

                "Cloud Computing":
                "Cloud computing is the delivery of computing services such as servers, storage, databases, networking and software over the internet to provide faster innovation and flexible resources.",

               "Python Programming":
               "Python is a high-level, interpreted programming language known for its simple syntax. It is widely used in web development, automation, data science, artificial intelligence and machine learning.",

               "Data Science":
               "Data science is the process of collecting, analyzing and interpreting data using statistics, machine learning and visualization techniques to extract meaningful insights and support decision making."
            }
    

            semantic_score = calculate_similarity(
            reference_answers[selected_topic],
            text
            )

            filler_count = count_filler_words(text)

            result = calculate_final_score(
            semantic_score,
            filler_count
            )

            audio_features = extract_audio_features(audio_path)

            st.subheader("📊 Evaluation Result")

            st.metric("Semantic Score", f"{result['semantic_score']}%")
            st.metric("Fluency Score", f"{result['fluency_score']}%")
            st.metric("Final Score", f"{result['final_score']}%")

            st.progress(result["final_score"] / 100)

            st.success(result["feedback"])

            st.subheader("🎧 Audio Analysis")
            st.write(f"Duration : {audio_features['duration']} sec")
            st.write(f"Average RMS : {audio_features['average_rms']}")

            os.makedirs("waveforms", exist_ok=True)

            fig = create_waveform(audio_path)

            waveform_path = os.path.join(
                "waveforms",
                os.path.splitext(audio_file.name)[0] + ".png"
            )

            fig.savefig(waveform_path)

            st.pyplot(fig)
            import matplotlib.pyplot as plt
            plt.close(fig)

            report = generate_report(result)
            os.makedirs("reports", exist_ok=True)

            report_path = os.path.join(
                "reports",
                os.path.splitext(audio_file.name)[0] + "_report.txt"
            )

            with open(report_path, "w") as f:
                f.write(report)

            st.download_button(
                "📄 Download Report",
                report,
                file_name=os.path.splitext(audio_file.name)[0] + "_report.txt"
            )

            st.subheader("Topic")
            st.write(selected_topic)

        else:
           st.error(text)



# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    ---
    Developed for Voice Based Concept Understanding Analyser (VBCUA)
    """
)
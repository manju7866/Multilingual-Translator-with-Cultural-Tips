
import streamlit as st
from translate import Translator
from culture_tips import tips

languages = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Chinese (Simplified)": "zh",
    "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Filipino (Tagalog)": "tl",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Nepali": "ne",
    "Norwegian": "no",
    "Persian (Farsi)": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi"
}

st.set_page_config(page_title="🌍 50+ Language Translator with Culture Tips", layout="centered")

st.title("🌐 Multilingual Translator with Cultural Tips (50+ Languages)")
st.write("🔤 Translate text + 🧠 get cultural guidance for major languages!")

text_input = st.text_area("Enter your text here:", "", height=150)
from_lang = st.selectbox("Translate from:", list(languages.keys()), index=10)
to_lang = st.selectbox("Translate to:", list(languages.keys()), index=20)

if st.button("Translate"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            translator = Translator(from_lang=languages[from_lang], to_lang=languages[to_lang])
            translated = translator.translate(text_input)

            st.success("✅ Translation Result:")
            st.text_area("Translated Text:", translated, height=150)

            st.markdown("---")
            st.markdown("📌 **Cultural Tip for Target Language:**")
            target_code = languages[to_lang]
            if target_code in tips:
                st.markdown(tips[target_code])
            else:
                st.info("ℹ️ No cultural tips available for this language yet.")
        except Exception as e:
            st.error(f"❌ Translation failed: {e}")

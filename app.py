import streamlit as st
from PIL import Image
import pytesseract

st.title("Скенер на хранителни етикети")

uploaded_file = st.file_uploader(
    "Качи снимка на етикет",
    type=["jpg", "jpeg", "png"]
)

ingredients_db = {
    "нитрит": {
        "status": "⚠️ Потенциално вредна",
        "info": "Може да повиши здравните рискове при честа консумация."
    },
    "дифосфат": {
        "status": "⚠️ Потенциално вредна",
        "info": "Добавка за стабилизиране на продукта."
    },
    "декстроза": {
        "status": "⚠️ Захар",
        "info": "Повишава кръвната захар."
    },
    "аскорбат": {
        "status": "✅ Безопасна",
        "info": "Антиоксидант, свързан с витамин C."
    },
    "свинско месо": {
        "status": "✅ Полезна",
        "info": "Източник на белтъчини."
    }
}

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Качен етикет")

    text = pytesseract.image_to_string(image, lang="bul")

    st.subheader("Разпознат текст")
    st.text(text)

    st.subheader("Открити съставки")

    found = False

    text = text.lower()

    for ingredient in ingredients_db:
        if ingredient in text:
            found = True

            st.write(f"### {ingredient.title()}")
            st.write(ingredients_db[ingredient]["status"])
            st.write(ingredients_db[ingredient]["info"])

    if not found:
        st.warning("Не са открити известни съставки.")

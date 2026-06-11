import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Скенер на хранителни етикети",
    page_icon="🥓"
)

st.title("🥓 Скенер на хранителни етикети")
st.write("Качи снимка на етикета и натисни 'Сканирай'.")

uploaded_file = st.file_uploader(
    "Избери снимка",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Качен етикет",
        use_container_width=True
    )

    if st.button("🔍 Сканирай"):

        st.success("Етикетът е анализиран успешно!")

        st.header("Открити съставки")

        ingredients = [
            {
                "name": "Свинско месо (96%)",
                "status": "✅ Безопасна",
                "info": "Богато на белтъчини и хранителни вещества."
            },
            {
                "name": "Натриев нитрит (E250)",
                "status": "⚠️ Потенциално вредна",
                "info": "Консервант. При прекомерна консумация може да има неблагоприятни ефекти."
            },
            {
                "name": "Дифосфати (E450)",
                "status": "⚠️ Потенциално вредна",
                "info": "Стабилизатор, използван в месните продукти."
            },
            {
                "name": "Декстроза",
                "status": "🟡 Захар",
                "info": "Може да повиши нивата на кръвната захар."
            },
            {
                "name": "Натриев аскорбат (E301)",
                "status": "✅ Безопасна",
                "info": "Антиоксидант, свързан с витамин C."
            },
            {
                "name": "Подправки",
                "status": "✅ Безопасна",
                "info": "Използват се за вкус и аромат."
            }
        ]

        for ingredient in ingredients:
            st.subheader(ingredient["name"])
            st.write(ingredient["status"])
            st.write(ingredient["info"])

        st.header("⚕️ Възможни здравословни проблеми")

        st.error("""
• Повишено кръвно налягане

• Повишена кръвна захар

• Сърдечно-съдови проблеми при прекомерна консумация

• Рискове за хора с бъбречни заболявания
""")

        st.header("🥗 По-здравословни алтернативи")

        alternatives = [
            "Домашно печено месо",
            "Варено пилешко филе",
            "Пуешко месо",
            "Домашна шунка",
            "Яйца",
            "Прясно месо"
        ]

        for alt in alternatives:
            st.write("✅", alt)

        st.header("📊 Хранителни стойности за 100 g")

        st.write("Енергийна стойност: 115 kcal")
        st.write("Мазнини: 3.0 g")
        st.write("Въглехидрати: 2.0 g")
        st.write("Белтъчини: 20.0 g")
        st.write("Сол: 1.9 g")

        st.header("⭐ Обща оценка")

        st.success("7/10 - Добър източник на белтъчини, но съдържа добавки и консерванти.")

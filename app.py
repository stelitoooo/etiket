import streamlit as st

st.set_page_config(page_title="Food Label Scanner", page_icon="🥓")

st.title("🥓 Сканиране на хранителен етикет")
st.subheader("Продукт: PIKOK Пушена шунка")

ingredients = {
    "Свинско месо (96%)": {
        "type": "Безопасна",
        "description": "Богато на белтъчини и витамини."
    },
    "Натриев нитрит (E250)": {
        "type": "Потенциално вредна",
        "description": "Консервант, използван за предпазване от бактерии."
    },
    "Дифосфати (E450)": {
        "type": "Потенциално вредна",
        "description": "Стабилизатор за подобряване структурата на месото."
    },
    "Натриев аскорбат (E301)": {
        "type": "Безопасна",
        "description": "Антиоксидант, производно на витамин C."
    },
    "Декстроза": {
        "type": "Умерена",
        "description": "Проста захар."
    },
    "Подправки": {
        "type": "Безопасна",
        "description": "За вкус и аромат."
    }
}

health_risks = {
    "Натриев нитрит (E250)": [
        "Повишено кръвно налягане",
        "Сърдечно-съдови заболявания",
        "Повишен риск при честа консумация"
    ],
    "Дифосфати (E450)": [
        "Нарушен минерален баланс",
        "Риск за хора с бъбречни заболявания"
    ],
    "Декстроза": [
        "Повишава кръвната захар",
        "Риск за диабетици"
    ]
}

st.header("Съставки")

for ingredient, info in ingredients.items():
    st.write(f"**{ingredient}**")
    st.write(f"Вид: {info['type']}")
    st.write(f"Описание: {info['description']}")
    st.divider()

st.header("Провери съставка")

selected = st.selectbox(
    "Избери съставка",
    list(ingredients.keys())
)

if st.button("Покажи информация"):
    st.success(ingredients[selected]["description"])

    if selected in health_risks:
        st.error("Възможни здравословни проблеми:")
        for risk in health_risks[selected]:
            st.write("•", risk)
    else:
        st.info("Няма известни сериозни рискове.")

st.header("По-здравословни алтернативи")

alternatives = [
    "Домашно печено месо",
    "Варено пилешко филе",
    "Пуешко филе",
    "Домашна шунка",
    "Яйца",
    "Прясно месо"
]

for alt in alternatives:
    st.write("✅", alt)

st.header("Хранителни стойности (100 g)")
st.write("Енергийна стойност: 115 kcal")
st.write("Белтъчини: 20 g")
st.write("Мазнини: 3 g")
st.write("Въглехидрати: 2 g")
st.write("Сол: 1.9 g")

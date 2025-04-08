import streamlit as st
import utils, os

st.title('Rätsel für Scotland Yard')

mapping = {"1. Hansemuseum": "hansemuseum",
            "2. Burgtor": "burgtor",
            "3. Museumshafen": "museumshafen",
            "4. Heiligen-Geist-Hospital": "heiligengeist",
            "5. St. Jakobi": "jakobi",
            "6. MUK": "muk",
            "7. Theater": "theater",
            "8. Günter-Grass-Haus": "guenter",
            "9. Klughafen": "klughafen",
            "10. Buddenbrookhaus": "buddenbrook",
            "11. St. Marien": "marien",
            "12. Holstentor": "holstentor",
            "13. Niederegger": "niederegger",
            "14. St. Petri": "petri",
            "15. St. Aegidien": "aegidien",   
        }

ort = st.selectbox('Ort', mapping.keys())


st.markdown(utils.read_markdown_file(f"pages/{mapping[ort]}.md"), unsafe_allow_html=True)

# Stadtkarte in zwei Spalten
col1, col2 = st.columns(2)
with col1:
    st.image("stadtkarte.png", caption="Stadtkarte")


nachfolger_fuss = {"1. Hansemuseum": ["2. Burgtor", "3. Museumshafen"],
            "2. Burgtor": ["1. Hansemuseum", "4. Heiligen-Geist-Hospital"],
            "3. Museumshafen": ["1. Hansemuseum", "6. MUK", "7. Theater"],
            "4. Heiligen-Geist-Hospital": ["2. Burgtor", "5. St. Jakobi", "8. Günter-Grass-Haus"],
            "5. St. Jakobi": ["4. Heiligen-Geist-Hospital", "7. Theater"],
            "6. MUK": ["3. Museumshafen", "7. Theater", "12. Holstentor"],
            "7. Theater": ["3. Museumshafen", "5. St. Jakobi", "6. MUK", "8. Günter-Grass-Haus", "10. Buddenbrookhaus", "11. St. Marien"],
            "8. Günter-Grass-Haus": ["4. Heiligen-Geist-Hospital", "7. Theater", "9. Klughafen", "15. St. Aegidien"],
            "9. Klughafen": ["8. Günter-Grass-Haus", "15. St. Aegidien"],
            "10. Buddenbrookhaus": ["7. Theater", "11. St. Marien", "13. Niederegger"],
            "11. St. Marien": ["7. Theater", "10. Buddenbrookhaus", "13. Niederegger", "14. St. Petri"],
            "12. Holstentor": ["6. MUK", "14. St. Petri"],
            "13. Niederegger": ["10. Buddenbrookhaus", "11. St. Marien", "14. St. Petri", "15. St. Aegidien"],
            "14. St. Petri": ["11. St. Marien", "12. Holstentor", "13. Niederegger", "15. St. Aegidien"],
            "15. St. Aegidien": ["8. Günter-Grass-Haus", "9. Klughafen", "13. Niederegger", "14. St. Petri"],   
        }
nachfolger_bus = {
            "2. Burgtor": ["7. Theater"],
            "7. Theater": ["2. Burgtor", "12. Holstentor", "13. Niederegger"],
            "12. Holstentor": ["7. Theater"],
            "13. Niederegger": ["7. Theater"],
            }
with col2:
    nachfolgetext = "##### Mögliche Nachfolgerorte (zu Fuß) \n"
    for nachfolger in nachfolger_fuss[ort]:
        nachfolgetext += f"- {nachfolger} \n"
    if ort in nachfolger_bus.keys():
        nachfolgetext += "\n##### Mögliche Nachfolgerorte (Bus) \n"
        for nachfolger in nachfolger_bus[ort]:
            nachfolgetext += f"- {nachfolger} \n"
    st.markdown(nachfolgetext)
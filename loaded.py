# Show text for food choices
import streamlit
streamlit.title('Loaded')

streamlit.header('Proper Dirty, Proper Epic')

streamlit.text('🐖 Pulled Pork, Caramelised Onions, Cayenne Pepper and Tabasco Sauce')
streamlit.text('🍗 Chicken, Chicken Skins, Cheddar Cheese and Barbeque Sauce')
streamlit.text('🥑 Avocado, Free-From Cheese, Lettuce and Vegan Sauce')
streamlit.text('🦆 Duck, Mushrooms, Bean Sprouts and Hoisin Sauce')

streamlit.header('🏗️ Build your own Dirty Fries')

# Import Food list
import pandas
foods = pandas.read_csv("https://drive.google.com/file/d/1yQv4h4yg3A01K9UjWbvsrFCHDbk39Isc/view?usp=sharing")
foods = foods.set_index('Name')

# Pick Food
foods_selected = streamlit.multiselect("Pick some foods:", list(foods.index),['Skinny Fries','Chicken'])
foods_to_show = foods.loc[foods_selected]

# Display list of fruits
streamlit.dataframe(foods_to_show)

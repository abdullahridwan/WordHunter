from graph import Graph
from helper import addEdges
import nltk
import streamlit as st
from nltk.corpus import words
import pandas as pd
import altair as alt
from PIL import Image


nltk.download('words')

# Helper Functions
def check_if_word(word):
    if word in checked_words:
        return checked_words[word]
    checked_words[word] = word in word_dict
    return checked_words[word]





checked_words = {}


def make_word(letters: list[str]):
  word_lst = []
  for l in letters:
    word_lst.append(l.split(" ")[0])
  word = "".join(word_lst)
  return word
  

# Make the Grid
def make_grid(l: str):
  """
  Given a string of letters, l, then return a 4x4 grid
  """
  lst = list(l)
  grid = []
  row = []
  for i in range(0,len(lst)):
    if (i+1) % 4 != 0:
      row.append(lst[i])
    else:
      row.append(lst[i])
      grid.append(row)
      row = []
  return grid


# Process grid to make letters unique
def process_grid(grid: list[list]):
  print(grid)
  for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
        ltr = grid[r][c]
        ltr = f"{ltr} ({r}, {c})"
        grid[r][c] = ltr
  print("After processing")
  print(grid)
  return grid

# Add Edges
def make_graph(grid):
  graph = Graph()
  for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
      addEdges(grid, graph, r, c)
  return graph


# Get words
word_dict = set(words.words())


# Run dfs from a start letter
def run_algo(l: str):
  grid = make_grid(l)
  grid = process_grid(grid)
  graph = make_graph(grid)


  words_l = []
  paths_l = []
  for r in range(len(grid)):
      for c in range(len(grid[r])):
        path = []
        paths = []
        start_letter = grid[r][c]
        # print(r,c, start_letter)
        graph.DFS(start_letter, path, paths)

        # Check what are words
        for p in paths:
            word = make_word(p)
            #print(f"Word: {word}")
            if len(word) >= 4 and check_if_word(word):
              words_l.append(word)
              paths_l.append(p)

  words_to_use = set(words_l)
  ordered_strings = sorted(words_to_use, key=lambda x: len(x), reverse=True)


  words_id_to_use = set([" | ".join(p) for p in paths_l])
  ordered_paths = sorted(words_id_to_use, key=lambda x: len(x), reverse=True)
  return ordered_strings, ordered_paths






st.title('Word Hunter 🏹')
st.markdown("This is a small website I made to help beat my friends in wordhunt because I keep losing (I'm really bad). Put in your letters for word hunt going left to right, starting from the top row")



# image = Image.open('graph.png')
# st.image(image, caption='How you should put in the letters', width=400)


l = st.text_input('Your letters', 'lasdashjtkemdjaa', max_chars=16)

if len(l) < 16:
   st.warning('Put in 16 letters', icon="⚠️")
elif len(l) == 16:
  st.success('Ready to go!', icon="✅")
else:
  st.warning("Woah! That's too many letters", icon="⚠️")



words = run_algo(l)
st.write(words[0])
# st.write(words[1])
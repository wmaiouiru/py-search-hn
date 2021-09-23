


from bs4 import BeautifulSoup
def clean_comment(text):
  # gets all (really the first 1000) of a user's comments (nicolashahn here)
  # outputs the cleaned comments to a text file, one comment per line

  return BeautifulSoup(text.replace("<p>", " ")).get_text().replace("\n", " ")


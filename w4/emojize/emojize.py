import emoji

em = (input("Input: ")).strip("_")
print("Output: ", emoji.emojize(em, language="alias"))

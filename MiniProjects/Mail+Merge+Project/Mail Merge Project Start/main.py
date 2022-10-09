# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt


with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

for name in name_list:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter_content = letter_file.read()
    striped_name = name.strip("\n")

    x = letter_content.replace("[name]", striped_name)
    letter_file_name = f"letter_for_{striped_name}"
    with open(f"./Output/ReadyToSend/{letter_file_name}", mode="w") as file:
        file.write(x)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# jewish-codenames
This repository helps create custom codenames with a menorah icon. The input to the software is a text file listing the words to include. The output is a LibreOffice Draw document in letter sized paper with the icons.

# requirements

The general requirements of this software are:

* Python 3 with re package
* Libreoffice Draw

This was tested specifically with:

* Python 3.9.12 with re version 2.2.1
* Libreoffice Draw version 7.3.7.2 on Ubuntu 22.04
* Latin letters

# Use

1. Modify `words.txt` with the words you want to be on codename cards.
2. Run `python generate_document.py` in the terminal.
3. Open `codenames_cards.fodg` in LibreOffice Draw.
4. Check the file for long words, such as 'Congregation', which might be on the next line. Reduce the font size of these words. If you save the file after making changes, saving as an `odf` file will take up less space.
5. Export the file as a PDF

# Files

* `words.txt`: A text file with a word on each new line. Each word will be converted into a card.
* `generate_document.py`: A python script to convert the words in `words.txt` into a Libreoffice Draw file `codenames_cards.fodg`
* `codenames_cards.fodg`: The output from `generate_document.py` which is a LibreOffice Draw file using letter-sized paper.
* `codenames_cards.pdf`: The cards in pdf form

# Help

If you have any questions, feel free to post in the github issues page. I'd be happy to help troubleshoot anything.

def word_replace():
    string = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque accumsan facilisis luctus. Proin laoreet posuere velit nec ornare. Vivamus erat ligula, dictum nec nulla quis, faucibus feugiat nunc.'
    choose_word = input('Which word would you like to replace: ')
    replace = input('Write the replacement word: ') 
    print(string.replace(choose_word, replace))

word_replace()
menu = True

while menu:
    print("\nWord Positioner Functions Include:  \n\n1. View the positions of the words in a predefined sentence. \n2. View the positions of the words in your own custom sentence. \n3. Exit.")
    menu = input("\nPick one of the functions above ^^^ :  ")

    if menu == "1":
        premade = "\nThe premade sentence of the day is: "
        sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
        sentence_uppercase = sentence.upper()
        sentence_list = sentence_uppercase.split()
        print (premade+sentence)

        def predef_word_pos():
            word_position = [sentence_list.index(x)+1 for x in sentence_list]
            sentence_no_repetition = [sentence_list[x-1] for x in word_position]
            print (word_position)

        user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
        user_input_lower = user_input.lower()

        if user_input_lower == "yes":
            print ("\nHere you go, this is the position of each word in the sentence:")
            predef_word_pos()

            write_input = input("\nWould you like to write this to an external file? [Yes/No] ")
            write_input_lower = write_input.lower()

            if write_input_lower == "yes":
                filename_input = input("What would you like the file name to be:  ")

                word_position = [sentence_list.index(i)+1 for i in sentence_list]
                word_position_str = str(word_position)
    
                sentence_no_repetition = [sentence_list[i-1] for i in word_position]
                sentence_no_repetition_str = str(sentence_no_repetition)

                filewrite = open(filename_input, "a")
                filewrite = filewrite.write("Predefined Sentence (" + username + "): " + "This is the sentence '" + sentence + "' and this is the word positions:  " +word_position_str + "\n")

                print("\nCongratulations " + username + "!!! You have wrote the sentence list and the position list to the file: " + filename_input)

                input("\nPress Enter to continue...")
                print("\nTo remind you:")
            
            if write_input_lower == "no":
                input("\nPress Enter to continue...")
                print("\nTo remind you:")

        if user_input_lower == "no":
            input("\nPress Enter to continue...")
            print("\nTo remind you:")

    if menu == "2":
        user_sentence = input("\nPlease enter a sentence that you would like to see the position of the words:  ")
        user_sentence_lower = user_sentence.lower()
        user_sentence_list = user_sentence_lower.split()

        def predef_custom_word_pos():
            user_word_position = [user_sentence_list.index(i)+1 for i in user_sentence_list]
            user_sentence_no_repetition = [user_sentence_list[i-1] for i in user_word_position]
            print (user_word_position)

        user_input = input("\nWould you like to see the positions of the words [Yes/No]:  ")
        user_input_lower = user_input.lower()

        if user_input_lower == "yes":
            print ("\nHere you go, this is the position of each word in the sentence:")
            predef_custom_word_pos()

            write_input = input("\nWould you like to write this to an external file? [Yes/No] ")
            write_input_lower = write_input.lower()

            if write_input_lower == "yes":
            
                user_filename_input = input("What would you like the file name to be:  ")

                user_word_position = [user_sentence_list.index(i)+1 for i in user_sentence_list]
                user_word_position_str = str(user_word_position)
    
                user_sentence_no_repetition = [user_sentence_list[i-1] for i in user_word_position]
                user_sentence_no_repetition_str = str(user_sentence_no_repetition)

                filewrite = open(user_filename_input, "a")
                filewrite = filewrite.write("Custom Sentence (" + username + "): " + "This is the sentence:  '" + user_sentence + "' and this is the word positions:  " +user_word_position_str + "\n")

                print("\nCongratulations " + username + "!!! you have wrote the sentence list and the position list to the file: " + user_filename_input)

                input("\nPress Enter to continue...")
                print("\nTo remind you:")

            if write_input_lower == "no":
                input("\nPress Enter to continue...")
                print("\nTo remind you:")

        if user_input_lower == "no":
            input("\nPress Enter to continue...")
            print("\nTo remind you:")

    if menu == "3":
        print ("\nGoodbye, hope we see you again.")
        import sys
        sys.exit()

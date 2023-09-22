    # YOUR PROJECT TITLE
    #### Video Demo:  <https://www.loom.com/share/f9de7551c9af42e7a5b122bc1bb4e9bb>
    #### Description:
    My final project is a 21 card game you are playing against the computer. It is stored in project.py file.
    Idea is you receive 2 random cards, and you need to decide wherther you want or not to get another card. Cards are added according to their value so their sum should be as close to 21 as possible. cards are also represented as emojis to make this game a little more cute.
    So the rules are: If you get 21, you won. If you got more than 21, you lost (shouldn't have taken last card!). If you got 20 or less, your result is compared to the computer's result. I decided to add comparison to computer last moment, to make the game more interactive. If fact, computer just calls random function to get its score.
    There are 4 sub-functions created for this game, some of them quite simple, and some - containing almost all of the game logic.
    I also created a test for all of 4 functions as required, it is in test_project.py file.
    My biggers struggle was writing a test function, because in one of my sub-functions we are calling for user input and I didnt know how to test that. I finally managed it using MagicMock in unittest library. But because of that, to call pytest function not we are obliged to ass -s in the end of the calling function and "mock" user imput manually.
    As I needed to use some extra libraries ,specifically to conduct testing, they are listed in requirements.txt
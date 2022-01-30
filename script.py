import random


acoustic_guitar = {'Beginner': ['\"Wonderwall\" by Oasis', '\"What\'s Up\" by 4 Non Blondes', '\"I Walk the Line\" by Johnny Cash', '\"Free Fallin\'\" by Tom Petty', '\"Used to Love Her\" by Guns \'n\' Roses'], 'Intermediate': ['\"Wanted Dead or Alive\" by Bon Jovi', '\"Layla (Unplugged)\" by Eric Clapton', '\"Tears in Heaven\" by Eric Clapton', '\"Stairway to Heaven\" by Led Zeppelin', '\"To Be With You\" by Mr. Big'], 'Advanced': ['\"Classical Gas\" by Tommy Emmanuel (Mason Williams)', '\"Angelina\" by Tommy Emmanuel', '\"Jolene\" by Dolly Parton', '\"Neon\" by John Mayer', '\"Mister Sandman\" by Chet Atkins']}
electric_guitar = {'Beginner': ['\"Back in Black\" by AC/DC', '\"Whole Lotta Love\" by Led Zeppelin', '\"Blitzkrieg Bop\" by Ramones', '\"I Can\'t Get No (Satisfaction)\" by The Rolling Stones', '\"Smoke on the Water\" by Deep Purple'], 'Intermediate': ['\"Walk this Way\" by Aerosmith', '\"Wonderful Tonight\" by Eric Clapton', '\"Waiting on the World to Change\" by John Mayer', '\"Black Dog\" by Led Zeppelin', '\"Enter Sandman\" by Metallica'], 'Advanced': ['\"Sultans of Swing\" by Dire Straits', '\"Mr. Crowley\" by Ozzy Osbourne', '\"Hotel California\" by The Eagles', '\"Cliffs of Dover\" by Eric Johnson', '\"For the Love of God\" by Steve Vai']}
bass = {'Beginner': ['\"Comfortably Numb\" by Pink Floyd', '\"She Loves You\" by The Beatles', '\"Another One Bites the Dust\" by Queen', '\"Seven Nation Army\" by The White Stripes', '\"Message in a Bottle\" by The Police'], 'Intermediate': ['\"Money\" by Pink Floyd', '\"YYZ\" by Rush', '\"London Calling\" by The Clash', '\"Detroit Rock City\" by Kiss', '\"Holiday in Cambodia\" by Dead Kennedys'], 'Advanced': ['\"Hysteria\" by Muse', '\"(Anesthesia) Pulling Teeth\" by Metallica', '\"Teen Town\" by Weather Report', '\"Nobody Weird Like Me\" by Red Hot Chili Peppers', '\"Victor Wooten\" by More Love']}
drums = {'Beginner': ['\"Billie Jean\" by Michael Jackson', '\"You Shook Me All Night Long\" by AC/DC', '\"Run to the Hills\" by Iron Maiden', '\"Come as You Are\" by Nirvana', '\"Feel Good Inc\" by Gorillaz'], 'Intermediate': ['\"No One Knows\" by Queens of the Stone Age', '\"Immigrant Song\" by Led Zeppelin', '\"Get Lucky\" by Daft Punk', '\"Master of Puppets\" by Metallica', '\"Uptown Funk\" by Mark Ronson ft. Bruno Mars'], 'Advanced': ['\"La Villa Strangiato\" by Rush', '\"The Dance of Eternity\" by Dream Theater', '\"Moby Dick\" by Led Zeppelin', '\"Goliath\" by The Mars Volta', '\"A Night in Tunisia\" by Art Blakey and The Jazz Messengers']}
piano = {'Beginner': ['\"Let it Be\" by The Beatles', '\"Yesterday\" by The Beatles', '\"Lean on Me\" by Bill Withers', '\"Where the Streets Have No Name\" by U2', '\"All Of Me\" by John Legend'], 'Intermediate': ['\"Fantasie-Impromptu (Op. 66)\" by Frédéric Chopin', '\"Elégie\" by Sergei Rachmaninoff', '\"Un Sospiro\" by Franz Liszt', '\"Je Te Veux\" by Erik Satie', '\"November from The Seasons (Op. 37a)\" by Pyotr Ilyich Tchaikovsky'], 'Advanced': ['\"Intermezzo (Op. 118 No. 2)\" by Johannes Brahms', '\"Serenade for the Doll, No. 2 from Children\'s Corner\" by Claude Debussy', '\"Song Without Words in F#minor (Op. 67 No. 2)\" by Felix Mendelssohn', '\"Prelude (Op. 3 No. 2)\" by Sergei Rachmaninoff', '\"Idyll\" by Mihály Zichy']}


def run_program():
    print()
    print('Welcome to the Song Recommendation Engine!')
    print()
    print('In here, depending on the instrument you play and your level of expertise, i will recommend a song for you to play and develop your skill in said instrument. Are you ready?')
    print()
    print()
    instrument = input('What instrument do you feel like playing today? Acoustic Guitar, Electric Guitar, Bass, Drums or Piano? ')
    print()
    expertise = input('Which would you say is your level of expertise in said instrument? Beginner, Intermediate or Advanced? ')

    def get_acoustic_song():
        if expertise.title() == 'Beginner':
            acoustic_songs = list(acoustic_guitar['Beginner'])
            random_song = random.choice(acoustic_songs)
            print()
            print('As a beginner you should try learning: ' + random_song + '.')
        
        elif expertise.title() == 'Intermediate':
            acoustic_songs = list(acoustic_guitar['Intermediate'])
            random_song = random.choice(acoustic_songs)
            print()
            print('As an intermediate player you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Advanced':
            acoustic_songs = list(acoustic_guitar['Advanced'])
            random_song = random.choice(acoustic_songs)
            print()
            print('As an advanced player you should try learning: ' + random_song + '.')
    

    def get_electric_song():
        if expertise.title() == 'Beginner':
            electric_songs = list(electric_guitar['Beginner'])
            random_song = random.choice(electric_songs)
            print()
            print('As a beginner you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Intermediate':
            electric_songs = list(electric_guitar['Intermediate'])
            random_song = random.choice(electric_songs)
            print()
            print('As an intermediate player you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Advanced':
            electric_songs = list(electric_guitar['Advanced'])
            random_song = random.choice(electric_songs)
            print()
            print('As an advanced player you should try learning: ' + random_song + '.')
    
    def get_bass_song():
        if expertise.title() == 'Beginner':
            bass_songs = list(bass['Beginner'])
            random_song = random.choice(bass_songs)
            print()
            print('As a beginner you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Intermediate':
            bass_songs = list(bass['Intermediate'])
            random_song = random.choice(bass_songs)
            print()
            print('As an intermediate player you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Advanced':
            bass_songs = list(bass['Advanced'])
            random_song = random.choice(bass_songs)
            print()
            print('As an advanced player you should try learning: ' + random_song + '.')
    
    def get_drums_song():
        if expertise.title() == 'Beginner':
            drums_songs = list(drums['Beginner'])
            random_song = random.choice(drums_songs)
            print()
            print('As a beginner you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Intermediate':
            drums_songs = list(drums['Intermediate'])
            random_song = random.choice(drums_songs)
            print()
            print('As an intermediate player you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Advanced':
            drums_songs = list(drums['Advanced'])
            random_song = random.choice(drums_songs)
            print()
            print('As an advanced player you should try learning: ' + random_song + '.')
    
    def get_piano_song():
        if expertise.title() == 'Beginner':
            piano_songs = list(piano['Beginner'])
            random_song = random.choice(piano_songs)
            print()
            print('As a beginner you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Intermediate':
            piano_songs = list(piano['Intermediate'])
            random_song = random.choice(piano_songs)
            print()
            print('As an intermediate player you should try learning: ' + random_song + '.')
        elif expertise.title() == 'Advanced':
            piano_songs = list(piano['Advanced'])
            random_song = random.choice(piano_songs)
            print()
            print('As an advanced player you should try learning: ' + random_song + '.')

    if instrument.title() == 'Acoustic Guitar':
        get_acoustic_song()
        run_again()
    elif instrument.title() == 'Electric Guitar':
        get_electric_song()
        run_again()
    elif instrument.title() == 'Bass':
        get_bass_song()
        run_again()
    elif instrument.title() == 'Drums':
        get_drums_song()
        run_again()
    elif instrument.title() == 'Piano':
        get_piano_song()
        run_again()

def run_again():
    print()
    restart = input('Would you like to get another song? Yes or No? ')
    if restart.title() == 'Yes' or restart.title() == 'Y':
        run_program()
    elif restart.title() == 'No' or restart.title() == 'N':
        print()
        print('Thank you for using my program! Have a nice day!')
    


 
run_program()







        

    





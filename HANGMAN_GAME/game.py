import random
word_list = ['space','table','early','trees','short','hands','state','black','shown','stood','front','voice','kinds','makes','comes','close','power','lived','vowel','taken','built','heart','ready','quite','class','bring','round','horse','shows','piece','green','stand','birds','start','river','tried','least','field','whose','girls','leave','added','color','third','hours','moved','plant','doing','names','forms','heavy','ideas','cried','check','floor','begin','woman','alone','plane','spell','watch','carry','wrote','clear','named','books','child','glass','human','takes','party','build','seems','blood','sides','seven','mouth','solve','north','value','death','maybe','happy','tells','gives','looks','shape','lives','steps','areas','sense','speak','force','ocean','speed','women','metal','south','grass','scale','cells','lower','sleep','wrong','pages','ships','needs','rocks','eight','major','level','total','ahead','reach','stars','store','sight','terms','catch','works','board','cover','songs','equal','stone','waves','guess','dance','spoke','break','cause','radio','weeks','lands','basic','liked','trade','fresh','final','fight','meant','drive','spent','local','waxes','knows','train','bread','homes','teeth','coast','thick','brown','clean','quiet','sugar','facts','steel','forth','rules','notes','units','peace','month','verbs','seeds','helps','sharp','visit','woods','chief','walls','cross','wings','grown','cases','foods','crops','fruit','stick','wants','stage','sheep','nouns','plain','drink','bones','apart','turns','moves','touch','angle','based','range','marks','tired','older','farms','spend','shoes','goods','chair','twice','cents','empty','alike','style','broke','pairs','count','enjoy','score','shore','roots','paint','heads','shook','serve','angry','crowd','wheel','quick','dress','share','alive','noise','solid','cloth','signs','hills','types','drawn','worth','truck','piano','upper','loved','usual','faces','drove','cabin','boats','towns','proud','court','model','prime','fifty','plans','yards','prove','tools','price','sheet','smell','boxes','raise','match','truth','roads','threw','enemy','lunch','chart','scene','graph','doubt','guide','winds','block','grain','smoke','mixed','games','wagon','sweet','topic','extra','plate','title','knife','fence','falls','cloud','wheat','plays','enter','broad','steam','atoms','press','lying','basis','clock','taste','grows','thank','storm','agree','brain','track','smile','funny','beach','stock','hurry','saved','sorry','giant','trail','offer','ought','rough','daily','avoid','keeps','throw','allow','cream','laugh','edges','teach','frame','bells','dream','magic','occur','ended','chord','false','skill','holes','dozen','brave','apple','climb','outer','pitch','ruler','holds','fixed','costs','calls','blank','staff','labor','eaten','youth','tones','honor','globe','gases','doors','poles','loose','apply','tears','exact','brush','chest','layer','whale','minor','faith','tests','judge','items','worry','waste','hoped','strip','begun','aside','lakes','bound','depth','candy','event','worse','aware','shell','rooms','ranch','image','snake','aloud','dried','likes','motor','pound','knees','refer','fully','chain','shirt','flour','drops','spite','orbit','banks','shoot','curve','tribe','tight','blind','slept','shade','claim','flies','theme','queen','fifth','union','hence','straw','entry','issue','birth','feels','anger','brief','rhyme','glory','guard','flows','flesh','owned','trick','yours','sizes','noted','width','burst','route','lungs','uncle','bears','royal','kings','forty','trial','cards','brass','opera','chose','owner','vapor','beats','mouse','tough','wires','meter','tower','finds','inner','stuck','arrow','poems','label','swing','solar','truly','tense','beans','split','rises','weigh','hotel','stems','pride','swung','grade','digit','badly','boots','pilot','sales','swept','lucky','prize','stove','tubes','acres','wound','steep','slide','trunk','error','porch','slave','exist','faced','mines','marry','juice','raced','waved','goose','trust','fewer','favor','mills','views','joint','eager','spots','blend','rings','adult','index','nails','horns','balls','flame','rates','drill','trace','skins','waxed','seats','stuff','ratio','minds','dirty','silly','coins','hello','trips','leads','rifle','hopes','bases','shine','bench','moral','fires','meals','shake','shops','cycle','movie','slope','canoe','teams','folks','fired','bands','thumb','shout','canal','habit','reply','ruled','fever','crust','shelf','walks','midst','crack','print','tales','coach','stiff','flood','verse','awake','rocky','march','fault','swift','faint','civil','ghost','feast','blade','limit','germs','reads','ducks','dairy','worst','gifts','lists','stops','rapid','brick','claws','beads','beast','skirt','cakes','lions','frogs','tries','nerve','grand','armed','treat','honey','moist','legal','penny','crown','shock','taxes','sixty','altar','pulls','sport','drums','talks','dying','dates','drank','blows','lever','wages','proof','drugs','tanks','sings','tails','pause','herds','arose','hated','clues','novel','shame','burnt','races','flash','weary','heels','token','coats','spare','shiny','alarm','dimes','sixth','clerk','mercy','sunny','guest','float','shone','pipes','worms','bills','sweat','suits','smart','upset','rains','sandy','rainy','parks','sadly','fancy','rider','unity','bunch','rolls','crash','craft','newly','gates','hatch','paths','funds','wider','grace','grave','tides','admit','shift','sails','pupil','tiger','angel','cruel','agent','drama','urged','patch','nests','vital','sword','blame','weeds','screw','vocal','bacon','chalk','cargo','crazy','acted','goats','arise','witch','loves','queer','dwell','backs','ropes','shots','merry','phone','cheek','peaks','ideal','beard','eagle','creek','cries','ashes','stall','yield','mayor','opens','input','fleet','tooth','cubic','wives','burns','poets','apron','spear','organ','cliff','stamp','paste','rural','baked','chase','slice','slant','knock','noisy','sorts','stays','wiped','blown','piled','clubs','cheer','widow','twist','tenth','hides','comma','sweep','spoon','stern','crept','maple','deeds','rides','muddy','crime','jelly','ridge','drift','dusty','devil','tempo','humor','sends','steal','tents','waist','roses','reign','noble','cheap','dense','linen','geese','woven','posts','hired','wrath','salad','bowed','tires','shark','belts','grasp','blast','polar','fungi','tends','pearl','loads','jokes','veins','frost','hears','loses','hosts','diver','phase','toads','alert','tasks','seams','coral','focus','naked','puppy','jumps','spoil','quart','macro','fears','flung','spark','vivid','brook','steer','spray','decay','ports','socks','urban','goals','grant','minus','films','tunes','shaft','firms','skies','bride','wreck','flock','stare','hobby','bonds','dared','faded','thief','crude','pants','flute','votes','tonal','radar','wells','skull','hairs','argue','wears','dolls','voted','caves','cared','broom','scent','panel','fairy','olive','bends','prism','lamps','cable','peach','ruins','rally','schwa','lambs','sells','cools','draft','charm','limbs','brake','gazed','cubes','delay','beams','fetch','ranks','array','harsh','camel','vines','picks','naval','purse','rigid','crawl','toast','soils','sauce','basin','ponds','twins','wrist','fluid','pools','brand','stalk','robot','reeds','hoofs','buses','sheer','grief','bloom','dwelt','melts','risen','flags','knelt']

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name1 = input("Enter your Name:")
    print("Welcome to Hangman game!",name1)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed", guess, "!")
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed ", guess, "!")
            elif guess != word:
                print(guess, " is not in the Word :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid Input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of tries. The word is " + word + ". Good luck next time!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()

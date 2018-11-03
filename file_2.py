def sayhi(name,Age):                            # remember, def of a func is never EXECUTED untill it is CALLED !
    print("hi, " + name )
    x = 18 - Age;
    if Age > 18:
        print(name + " you are eligible for this test as you're" + str(Age) + " y/o" )
    else:
        print(" Sorry, " + name + " you are too young for this test. Please apply a/f " + str(x) + " years")

name = input(" Type in your name :  ")
age  = input(" Type in Your age : ")       # age is an INTEGER !
Age = int(age)
sayhi(name,Age)

# dictionaries ! {}
# it stores a KEY ( like a word in a dic ) and a Value ( like DEF in a dic) ,both in pairs name:value
# Key values should be unique !

Months_Abbr = {
              "Jan" : "January"   ,
              "Feb" : "February"  ,
              "MAr" :  "March"    ,
              "April":  "April"
    }

print(Months_Abbr.get("Jan"))

input_user = input(" enter a month like Jan/Feb: ")

for index_value in Months_Abbr:
    if input_user == index_value:
        print(index_value)
        break      # print the found element just 1 time
    else:
        print(Months_Abbr.get(input_user, " Not Found"))
        break     # print Not Found 1 time not 3 times!


for index_value in Months_Abbr.items():
    print(index_value)

secret_word = "selfish"
guess_limit = 3
guess_count = 0
out_of_guesses = False
user_guess = ""

while (secret_word != user_guess and not( out_of_guesses)  ):
    if guess_count < guess_limit:
        user_guess = input(" Enter the secret word ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose ")
else:
    print(" you win !!!")











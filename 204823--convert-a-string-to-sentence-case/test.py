from solution import f

def tee(x):print(x);return x

# Given test cases
assert tee(f("hello world.")) == "Hello world."
assert tee(f("CODEGOLF IS FUN.")) == "Codegolf is fun."
assert tee(f("no period")) == "No period"
assert tee(f("the ball was red. so was the balloon.")) == "The ball was red. So was the balloon."
assert tee(f("I love codegolf.stackexchange.com")) == "I love codegolf.Stackexchange.Com"
assert tee(f("heLLo! hOW are yOU toDay? hOpEfulLy yOu are okay!")) == "Hello! How are you today? Hopefully you are okay!"

# Extra test cases
assert tee(f("a.b.c")) == "A.B.C"
assert tee(f("hello.  goodbye")) == "Hello.  Goodbye"
assert tee(f("I'M A ROBOT")) == "I'm a robot"

print('\nPassed all test cases.')

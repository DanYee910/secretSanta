from random import shuffle

class Person():
  def __init__(self, name, email):
    self.name = name
    self.email = email

# create a person object for each participant
helloWorld = Person("helloWorld", "example@stuff.com")
kid = Person("kid", "person@stuff.com")
dude = Person("dude", "iam@someone.com")
clown = Person("Krusty", "the@clown.com")
# add that person obj into the names list
names = [helloWorld, kid, dude, clown]

shuffle(names)

if(len(names) < 3):
  print "Too few people in this secret santa, stay indoors and play DotA2 instead."
else:
  for idx in range(len(names)):
    me = names[idx]
    recipient = ""
    if(idx + 1 > (len(names) - 1)):
      recipient = names[0]
    else:
      recipient = names[idx + 1]
    print "%s is buying a shitty present for %s because he/she/it/thing is a cheapass.  If you want to ask %s on a hot date, email them at: %s" % (me.name, recipient.name, recipient.name, recipient.email)

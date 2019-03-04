
from .models import *


def populate():
    u1 = User(name='austen')
    t1 = Tweet(text='Lambda School Rocks!')
    t2 = Tweet(text='vote for me in the neoliberal shill contest!')
    t3 = Tweet(text='our students are the best')
    austen_tweets = [t1, t2, t3]

    ud = User(name='dril')

    d1 = Tweet(text='volunteering at the Daniel Kahneman museum, visitors keep asking me if they can \'update the counterfactual\'. Buddy, they won\'t even let me update it')
    d2 = Tweet(
        text='who is scraeming "CROSS VALIDATE" at my house. show yourself, coward. i will never cross validate')
    dril_tweets = [d1, d2]

    for t in austen_tweets:
        u1.tweets.append(t)

    for t in dril_tweets:
        ud.tweets.append(t)

    all_stuff = [u1, ud] + austen_tweets + dril_tweets

    DB.drop_all()
    DB.create_all()

    for item in all_stuff:
        DB.session.add(item)

    DB.session.commit()


'''
if __name__=="__main__":
    populate()
    pass'''

#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    ''' Bob is a lackadaisical teenager. In conversation, his responses are very
        limited.

        Bob answers 'Sure.' if you ask him a question.

        He answers 'Whoa, chill out!' if you yell at him.

        He says 'Fine. Be that way!' if you address him without actually saying
        anything.

        He answers 'Whatever.' to anything else.

    '''

    what = what.strip()

    if not len(what[:-1]):
        return 'Fine. Be that way!'
    elif what[:-1].isupper():
        return 'Whoa, chill out!'
    elif what.strip().endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'

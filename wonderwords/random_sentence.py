import random


class random_sentence:
    def __init__(self):
        from importlib_resources import files
        noun_file_path = files('wonderwords').joinpath('nounlist.txt')
        adjective_file_path = files('wonderwords').joinpath('adjectivelist.txt')
        verb_file_path = files('wonderwords').joinpath('verblist.txt')

        noun_file = open(noun_file_path, 'r')
        adjective_file = open(adjective_file_path, 'r')
        verb_file = open(verb_file_path, 'r')

        nouns = noun_file.readlines()
        adjectives = adjective_file.readlines()
        verbs = verb_file.readlines()

        def strip_newline(words):
            words_newline_stripped = []
            for w in words:
                words_newline_stripped.append(w.rstrip())
            return words_newline_stripped

        self.noun = strip_newline(nouns)
        self.verb = strip_newline(verbs)
        self.adjective = strip_newline(adjectives)

    def bare_bone_sentence(self):
        the_noun = random.choice(self.noun)
        the_verb = random.choice(self.verb)

        if the_verb[-1] == 'h' and (the_verb[-2] == 's' or the_verb[-2] == 'c'):
            return 'The %s %ses.' % (the_noun, the_verb)

        elif the_verb[-1] == 'y':
            the_verb_list = list(the_verb)
            del the_verb_list[-1]
            the_new_verb = ''.join(the_verb_list)
            return 'The %s %sies.' % (the_noun, the_new_verb)

        elif the_verb[-1] == 's' and the_verb[-2] == 's':
            return 'The %s %ses.' % (the_noun, the_verb)

        else:
            return 'The %s %ss.' % (the_noun, the_verb)

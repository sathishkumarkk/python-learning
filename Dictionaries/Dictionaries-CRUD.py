def display_facts(facts):
    #"""Displays facts"""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
        print()
facts = {
'Jason': 'Can fly an airplane.',
'Jeff': 'Is afraid of clowns.',
'David': 'Plays the piano.'
}
display_facts(facts)
facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'
print()
display_facts(facts)
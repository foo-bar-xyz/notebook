import datetime

last_id = 0

class Note(object):
    '''
    Represents a note in a notebook. Match against a string in searches
    and store tags for each note.
    '''
    def __init__(self, memo, tags=''):
        '''Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter text.
        Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and tags.
        '''
        return filter in self.memo or filter in self.tags

class Notebook(object):
    '''
    Represents a collection of Notes that can be tagged, modified and searched
    '''
    def __init__(self):
        '''Initialize a notebook with an emty list'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list'''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        ''' Find the note with a given id and
            change its memo to the given value'''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        ''' Find the note with the given id and
            change its tags to the given value'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''Find all notes that match the given filter string'''
        return [note for note in self.notes if note.match(filter)]

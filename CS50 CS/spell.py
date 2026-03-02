words = set()

def check(word):
    """Returns True if word is in dictionary, else False."""
    return word.lower() in words

def load(dictionary):
    with open(dictionary, 'r') as f:
        words.update(f.read().splitlines())
    return True

def size():
    """Returns number of words in dictionary if loaded, else 0 if not yet loaded."""
    return len(words)

def unload():    """Unloads dictionary from memory.  Returns True if successful, else False."""
    words.clear()
    return True
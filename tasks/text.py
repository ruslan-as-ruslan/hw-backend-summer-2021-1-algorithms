from posixpath import split
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    
    splitted = text.split()

    if not splitted:
        return None, None

    return min(splitted, key=len), max(splitted, key=len)
        

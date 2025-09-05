from django.core.exceptions import ValidationError

BLOCKED_WORDS = [
    "barato",
    "malo"
]

def validate_bloqued_words(value):
    init_string = f"{value}".lower()
    unique_words = set(init_string.split())
    bloqued_words = set(BLOCKED_WORDS)
    invalid_words = (unique_words & bloqued_words)
    has_error = len(invalid_words) > 0
    if has_error:
        errors = []
        for invalid_word in invalid_words:
            msg = "{} es una palabra no permitida".format(invalid_word)
            errors.append(msg)
        raise ValidationError(errors)
    return value
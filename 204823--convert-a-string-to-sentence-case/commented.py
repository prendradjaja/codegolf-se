f = (
  lambda string:
    ''.join(map(

      # Capitalize first letter in part
      lambda part: re.sub(
        r'[a-z]',
        lambda match: match[0].upper(),
        part.lower(),
        1
      ),

      # Split on punctuation
      re.split(r'([.?!])',string)

    ))
)

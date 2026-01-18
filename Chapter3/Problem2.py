# Wap to fill in a letter template given below with name and date:
"""
letter = 
        Dear <|Name|>,
        You are selected!
        <|Date|>
        """

letter = f"""
        Dear <|Name|>, 
        You are selected!
        <|Date|>"""
print(letter.replace("<|Name|>","Dua Rajat").replace("<|Date|>","9th July,2026"))
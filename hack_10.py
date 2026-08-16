"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.replace("f", "F")
    result = result.replace("o", "0")
    result = result.replace("z", "Z")
    result = result.replace("i", "1")
    result = result.replace("m", "M")
    result = result.replace("a", "@")
    result = result.replace("n", "N")
    return list(result)
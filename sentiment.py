def sentiment(tweet):
    if "rõõmus" in tweet:
        a = "hea tuju"
    elif "kurb" in tweet:
        a = "halb tuju"

    return a
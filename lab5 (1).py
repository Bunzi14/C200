
def findLetters(tweets, keyLetters):
    """
    Parameters:
    - tweets: dictionary with {username: ListOfTweets} where each 
        username is a string, and the ListOfTweets  is a list 
        of strings representing tweets
    - keyLetters: list of letters 

    Returns: A dictionary

    Function counts the number of occurences of a letter in all the tweets
    """
    results = {}
    count = 0
    
        

    

def findWords(tweets, keyWords):
    """
    Parameters:
    - tweets: dictionary with {username: ListOfTweets} where each 
        username is a string, and the ListOfTweets  is a list 
        of strings representing tweets
    - keyLetters: list of words 

    Returns: A dictionary

    Function counts the number of occurences of a word in all the tweets

    Assume there are repeats of words, so just using **in** will not work. You will have to check if the word is within a word

    You will have to use the function split, which is done on a string. 
    Do not worry about special characters, ".", "'", "," and such. 
    """
    results = {}
    pass 
    # TODO: Finish this
    


# Most of these sentences are from: https://randomwordgenerator.com/sentence.php 
coll = {
    "friendlyCats": ["It didn't make sense unless you had the power to eat colors. Check back tomorrow; I will see if the book has arrived.",
                     "Look on top of the refrigerator for the key. The old apple revels in its authority. ", 
                     "He went back to the video to see what had been recorded and was shocked at what he saw.",
                     "When nobody is around, the trees gossip about the people who have walked under them."],
    "IndianaUniversity": [
        "Lightning Paradise was the local hangout joint where the group usually ended up spending the night.",
        "This made him feel like an old-style rootbeer float smells. Be careful with that butter knife.",
        "The snow-covered path was no help in finding his way out of the backcountry. I am out of paper for the printer."],
    "cowboy_from_rdr2": [
        "Her hair was windswept as she rode in the black convertible.",
        "Oh, how I'd love to go!",
        "We had a three-course meal."],
    "Staples": [
        "Like ultra fine? Dig a bold tip? No matter how you like to write, we’ve got your favorite from TRU RED. Discover The Loop to see them all",
        "Want some future-thinking inspiration for your business? In this bunker office, sci-fi meets server space. Take the tour inside",
        "New Winter issue, new business insights."
    ],
    "twitter": [
        "This is a Japanese doll.",
        "I love eating toasted cheese and tuna sandwiches.",
        "He learned the hardest lesson of his life and had the scars"
    ]
}


if __name__ == "__main__":
    print(findLetters(coll, ["a", "b", "c"])) # Results: {'a': 67, 'b': 15, 'c': 21}
    # TODO: Add more tests
    #print(findWords(coll, ["cat", "go", "where", "out"])) # Results: {'cat': 0, 'go': 4, 'where': 1, 'out': 4}
    # TODO: Add more tests
    #print(coll['friendlyCats'][1])


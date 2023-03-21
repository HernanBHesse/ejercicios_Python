text = "Lorem ipsum dolor, sit amet, consectetur adipiscing ; elit. Praesent ut vulputate ante. Integer sodales massa nunc, in fermentum lacus viverra a. Suspendisse et nisl tempor elit mattis condimentum iaculis eu ipsum. Etiam non lacinia urna. Nulla non sem et nunc molestie aliquam at et leo. Ut quam arcu, maximus et justo sit amet, sodales porttitor nibh. Mauris faucibus dolor in libero congue vehicula. Nunc interdum nisl at ex suscipit, quis luctus tellus venenatis. Vivamus at lacus nec odio scelerisque lobortis a vel neque. Donec non magna ac lectus facilisis fermentum. Aliquam pulvinar est vitae vulputate lacinia. Curabitur auctor finibus purus, sit amet rhoncus tortor euismod id. Nulla elementum quis diam ut iaculis."

#Ej 3
def words(text):
    dictionary = text.split()
    wordsFrequency = {}
    for word in dictionary:
        if word.lower() in wordsFrequency:
            wordsFrequency[word.lower()] += 1
        else:
            wordsFrequency[word.lower()] = 1
    print(f"Diccionario:\n {wordsFrequency}")
    return wordsFrequency

#Ej 4
def mostUseWords (allWords):
    mostUse = max(allWords, key=allWords.get)
    return (mostUse, allWords[mostUse])

allWords = words(text)
mostUseWords = mostUseWords(allWords)
print(f"\n Palabra más usada fue\n {mostUseWords}")

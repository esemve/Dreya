from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class Classify:

    def __init__(self):
        pass

    def check(self, normalized):
        sentences = []
        labels = []

        #Betoltjuk az adatokat labels filebol
        for line in open('labels.txt'):
          fields = line.split('|')
          sentences.append(fields[0].strip())
          labels.append(fields[1].strip())

        #Az 1 az 1ben talalatokat visszaadjuk
        if normalized in sentences:
            i = 0
            for sent in sentences:
                if sent == normalized:
                    return labels[i]
                i += 1

        #Elmentjuk ha meg nem lattuk ezt a mondatot
        saveSentence = True
        if normalized not in sentences:
            for line in open('newlabel.txt'):
                fields = line.split('|')
                if (fields[0]==normalized):
                    saveSentence = False
                    break
        else:
            saveSentence = False

        if (saveSentence):
            with open("newlabel.txt", "a") as newlabels:
                newlabels.write(normalized+"|\n")


        #Haladunk tova
        tfv = TfidfVectorizer()

        # Fit TFIDF
        tfv.fit(sentences)
        X =  tfv.transform(sentences)

        lbl = LabelEncoder()
        y = lbl.fit_transform(labels)

        xtrain, xtest, ytrain, ytest = train_test_split(X, y, stratify=y, random_state=42)

        clf = LogisticRegression()
        clf.fit(xtrain, ytrain)
        predictions = clf.predict(xtest)


        #Szuksegunk lesz a labelek egyedi szamara
        labelNumberArray = []
        for i in range(0,len(set(labels))):
            labelNumberArray.append(i)

        new_sentence = [normalized]
        X_Test = tfv.transform(new_sentence)
        predlabels = lbl.inverse_transform(labelNumberArray)


        proba = clf.predict_proba(X_Test)
        thedict = {}
        firstbig = 0
        secbig = 0

        #Kiirathatnank, hogy melyik labelre mennyi az egyezes
        #print(proba[0])

        for pred in proba[0]:
            if firstbig<pred:
                secbig = firstbig
                firstbig = pred
            elif secbig<pred:
                secbig = pred


        # Ha az elso es a masodik label kozotti kulonbseg
        # megfelelo akkor felismertnek tekintjuk a mondatot


        if firstbig>secbig*1.005:
            th = 0
            for pred in proba[0]:
                if pred == firstbig:
                    return predlabels[th]
                th = th+1

        return ""
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations=set()
        to_morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        word=[]
        for w in words:
            for c in w:
                word.append(to_morse[ord(c)-97])
            transformations.add("".join(word))
            word=[]
        return len(transformations)
            

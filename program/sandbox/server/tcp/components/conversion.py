import re
class conversion:
    def __init__(self):

        self.morseto = {'a':'.-','b':'-...','c':'-.-.','d':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
                   'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
                   's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
                   'y':'-.--', 'z':'--..', ' ':' '}

        self.morsefrom = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
                     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
                     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
                     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
                     '-.--':'y','--..':'z', ' ':' '}


    def mto(self, sentence):
        resultlst = []
        for char in sentence:
            #print(self.morseto[char], end='_')
            resultlst.append(self.morseto[char])
        joined = '_'.join(resultlst) + '_'
        return joined
    

    def mfrom(self, code):                                                                  # this might be the most awful function ever
        i = 0
        templist = []
        templist2 = []
        for test in re.finditer('_', code):
            spaces = 'space found',test.start(), test.end()                                 # finds spaces used for separation
            #print(spaces)
            templist.append(test.start())
        templist2.append(code[0:templist[0]])
        while i < len(templist)+1:

            try:                                                                            # error supression
                templist2.append(code[templist[i]+1:templist[i+1]])
            except:
                pass
            i += 1


        x = 0
        while x < len(templist2):

            tmpcode = templist2[x]
            print(self.morsefrom[(tmpcode)], end='')
                                                                                            # prints newline

            x +=1
        print(' ')


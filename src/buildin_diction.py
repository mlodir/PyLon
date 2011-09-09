class Diction():

    def RetDictBuild(self):
        d = ["while", "for", "in", "if", "else", "elif","abs","divmod","input","open","staticmethod","all","enumerate","int","ord","str","any","eval","isinstance","pow","sum","basestring","execfile","issubclass","print","super","bin","file","iter","property","tuple","bool","filter","len","range","type","bytearray","float","list","raw_input","unichr","callable","format","locals","reduce","unicode","chr","frozenset","long","reload","vars","classmethod","getattr","map","repr","xrange","cmp","globals","max","reversed","zip","compile","hasattr","memoryview","round","__import__","complex","hash","min","set","apply","delattr","help","next","setattr","buffer","dict","hex","object","slice","coerce","dir","id","oct","sorted","intern", ]
        return d

    def RetDictDefClass(self):
        d = ["def", "class"]
        return d
    
    def RetDictBraces(self):
        d = ["\(", "\)", "\{", "\}", "\[", "\]"]
        return d
    
    def RetDictMath(self):
        d = ["\+", "-", "=", "\/", ">", "<", "\!", "\*", "\&", "\|", "\^"]
        return d
    
    def RetDictNumbers(self):
        d = ['[+-]?[0-9]+[lL]?','[+-]?0[xX][0-9A-Fa-f]+[lL]?','[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?']
        return d

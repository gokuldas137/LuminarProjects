class Editor:
    def functionalities(self):
        self.funcs=["createnewfile","execute","save"]
        return self.funcs

class Pycharm(Editor):
    def functionalities(self):
        funcs=super().functionalities()                                     # use of super()
        funcs.append(["debug","versioncontrolling"])
        return funcs

class Vscode(Editor):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append(["more extension support"])
        return funcs

# pyc=Pycharm()
# print(pyc.functionalities())

vsc=Vscode()
print(vsc.functionalities())
import os, json, subprocess

class SolParse():
    def __init__(self, fname):
        self.text = self._load(str(fname))
        self.title = self._getVal(self.text, "title")
        self.desc = self._getVal(self.text, "desc")
        self.jsontext = self._remVars(self.text)
        self.args = json.loads(self.jsontext)

    def _getVal(self, text, val):

        "Gets $val from solution file"

        value = self._verstr(val)

        fvalue = f"${value}"

        text = text.split("\n")

        for _ in text:

            if _.startswith(fvalue):

                return eval(_.strip()[len(fvalue) + 1:])

    def _remVars(self, text):

        started = False

        output = []

        for line in text.split("\n"):

            if line.startswith("{") or started:
                started = True
                output.append(line)
        
        return "\n".join(output)

    def _verstr(self, var):

        filename = str(var)

        return filename

    def _load(self, fname):

        filename = self._verstr(fname)

        if os.path.exists(filename):

            with open(filename) as f:

                text = f.read()

                if text.strip().replace('\n', '') == "":

                    raise IOError("File cannot be empty")
                
                else:

                    return text

        else:

            raise IOError(f"File {filename} does not exist")

    def getFormatted(self):

        return self.title + ": " + self.desc

    def _exec(self, com):

        process = subprocess.Popen(
                            com.split(), 
                            stdout = subprocess.PIPE, 
                            stderr = subprocess.PIPE
                            )

        pstdout, pstderr = process.communicate()

        return pstdout.decode() + pstderr.decode()

    def exec(self):

        args = self.args

        if 'if' in args and 'then' in args:

            find, com = args['if'].split(' in ')

            if find in self._exec(com):

                os.system(args['then'])
            
            else:

                os.system(args['else'])
    
    def __str__(self):
        return self.title + "\n" + self.desc
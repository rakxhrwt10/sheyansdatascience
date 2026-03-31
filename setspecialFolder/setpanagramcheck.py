def checkIfPangram(self, sentence: str) -> bool:


        alphabet="abcdefghijklmnopqrstuvwxyz"


        for a in alphabet:

            if a in sentence:

                continue
            else:
                
                return False
                break
        return True
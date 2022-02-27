import random
import json
import torch
import opener
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Noobpro"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    ls404 = ["I do not understand...","Sorry I didn't get it :(","I wish I could answer it for you :(","Sorry for dissapointing, I can't help you with this :("]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return [random.choice(intent['responses']),intent["tag"]]
    
    return [random.choice(ls404), "404"]

class opencls:
    def _init_(self,appnm):
        self.appnm = appnm[0].lower()
        self.loca = [r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs',r'C:\Users\Dharma\AppData\Roaming\Microsoft\Windows\Start Menu\Programs']
        # os.startfile(r'shell:AppsFolder')
        self.cd = 0
        self.applist = self.loca[self.cd]
        self.apps = {}
        self.uninstallers = {}
        self.open()

    def refetch(self):
        for pathh,sub,files in os.walk(self.applist):
            for i in files:
                if 'ninstall' not in i:
                    self.apps[i] = os.path.join(pathh,i)
                else:
                    self.uninstallers[i] = os.path.join(pathh, i)
    def open(self):
        self.refetch()
        self.appnm.lower()
        temp = {}
        for i in self.apps:
            k = i.lower()
            if self.appnm in k:
                temp[i] = self.apps.get(i)
        l = sorted(temp)
        if len(temp) == 1:
            pass
            os.startfile(self.apps.get(l[0]))
        elif len(temp) == 0:
            try:
                self.cd +=1
                self.applist = self.loca[self.cd]
                self.open()
            except:
                print('Not found')
        else:
            print('Which file do you need to open ?')
            d = 0
            for i in l:
                print(f'{d} . {i}')
                d += 1
            t = int(input('Enter '))
            os.startfile(self.apps.get(l[t]))
    def paral(self):
        l = ['appname']
        return l



if __name__ == "__main__":
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break
        resp = get_response(sentence)
        print(resp[0])
        if resp[-1] == "open":
            appnm = str(sentence.split(" ")[-1])
            op = opener.opener([appnm])        


# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random



play_order5=[{
      "RRRPR": 0, "RRPPR": 0, "RRSPR": 0,
      "RPRPR": 0, "RPPPR": 0, "RPSPR": 0,
      "RSRPR": 0, "RSPPR": 0, "RSSPR": 0,
      "PRRPR": 0, "PRPPR": 0, "PRSPR": 0,
      "PPRPR": 0, "PPPPR": 0, "PPSPR": 0,
      "PSRPR": 0, "PSPPR": 0, "PSSPR": 0,
      "SRRPR": 0, "SRPPR": 0, "SRSPR": 0,
      "SPRPR": 0, "SPPPR": 0, "SPSPR": 0,
      "SSRPR": 0, "SSPPR": 0, "SSSPR": 0,

      "RRRRR": 0, "RRPRR": 0, "RRSRR": 0,
      "RPRRR": 0, "RPPRR": 0, "RPSRR": 0,
      "RSRRR": 0, "RSPRR": 0, "RSSRR": 0,
      "PRRRR": 0, "PRPRR": 0, "PRSRR": 0,
      "PPRRR": 0, "PPPRR": 0, "PPSRR": 0,
      "PSRRR": 0, "PSPRR": 0, "PSSRR": 0,
      "SRRRR": 0, "SRPRR": 0, "SRSRR": 0,
      "SPRRR": 0, "SPPRR": 0, "SPSRR": 0,
      "SSRRR": 0, "SSPRR": 0, "SSSRR": 0,

      "RRRSR": 0, "RRPSR": 0, "RRSSR": 0,
      "RPRSR": 0, "RPPSR": 0, "RPSSR": 0,
      "RSRSR": 0, "RSPSR": 0, "RSSSR": 0,
      "PRRSR": 0, "PRPSR": 0, "PRSSR": 0,
      "PPRSR": 0, "PPPSR": 0, "PPSSR": 0,
      "PSRSR": 0, "PSPSR": 0, "PSSSR": 0,
      "SRRSR": 0, "SRPSR": 0, "SRSSR": 0,
      "SPRSR": 0, "SPPSR": 0, "SPSSR": 0,
      "SSRSR": 0, "SSPSR": 0, "SSSSR": 0,


      "RRRPP": 0, "RRPPP": 0, "RRSPP": 0,
      "RPRPP": 0, "RPPPP": 0, "RPSPP": 0,
      "RSRPP": 0, "RSPPP": 0, "RSSPP": 0,
      "PRRPP": 0, "PRPPP": 0, "PRSPP": 0,
      "PPRPP": 0, "PPPPP": 0, "PPSPP": 0,
      "PSRPP": 0, "PSPPP": 0, "PSSPP": 0,
      "SRRPP": 0, "SRPPP": 0, "SRSPP": 0,
      "SPRPP": 0, "SPPPP": 0, "SPSPP": 0,
      "SSRPP": 0, "SSPPP": 0, "SSSPP": 0,

      "RRRRP": 0, "RRPRP": 0, "RRSRP": 0,
      "RPRRP": 0, "RPPRP": 0, "RPSRP": 0,
      "RSRRP": 0, "RSPRP": 0, "RSSRP": 0,
      "PRRRP": 0, "PRPRP": 0, "PRSRP": 0,
      "PPRRP": 0, "PPPRP": 0, "PPSRP": 0,
      "PSRRP": 0, "PSPRP": 0, "PSSRP": 0,
      "SRRRP": 0, "SRPRP": 0, "SRSRP": 0,
      "SPRRP": 0, "SPPRP": 0, "SPSRP": 0,
      "SSRRP": 0, "SSPRP": 0, "SSSRP": 0,

      "RRRSP": 0, "RRPSP": 0, "RRSSP": 0,
      "RPRSP": 0, "RPPSP": 0, "RPSSP": 0,
      "RSRSP": 0, "RSPSP": 0, "RSSSP": 0,
      "PRRSP": 0, "PRPSP": 0, "PRSSP": 0,
      "PPRSP": 0, "PPPSP": 0, "PPSSP": 0,
      "PSRSP": 0, "PSPSP": 0, "PSSSP": 0,
      "SRRSP": 0, "SRPSP": 0, "SRSSP": 0,
      "SPRSP": 0, "SPPSP": 0, "SPSSP": 0,
      "SSRSP": 0, "SSPSP": 0, "SSSSP": 0,


      "RRRPS": 0, "RRPPS": 0, "RRSPS": 0,
      "RPRPS": 0, "RPPPS": 0, "RPSPS": 0,
      "RSRPS": 0, "RSPPS": 0, "RSSPS": 0,
      "PRRPS": 0, "PRPPS": 0, "PRSPS": 0,
      "PPRPS": 0, "PPPPS": 0, "PPSPS": 0,
      "PSRPS": 0, "PSPPS": 0, "PSSPS": 0,
      "SRRPS": 0, "SRPPS": 0, "SRSPS": 0,
      "SPRPS": 0, "SPPPS": 0, "SPSPS": 0,
      "SSRPS": 0, "SSPPS": 0, "SSSPS": 0,

      "RRRRS": 0, "RRPRS": 0, "RRSRS": 0,
      "RPRRS": 0, "RPPRS": 0, "RPSRS": 0,
      "RSRRS": 0, "RSPRS": 0, "RSSRS": 0,
      "PRRRS": 0, "PRPRS": 0, "PRSRS": 0,
      "PPRRS": 0, "PPPRS": 0, "PPSRS": 0,
      "PSRRS": 0, "PSPRS": 0, "PSSRS": 0,
      "SRRRS": 0, "SRPRS": 0, "SRSRS": 0,
      "SPRRS": 0, "SPPRS": 0, "SPSRS": 0,
      "SSRRS": 0, "SSPRS": 0, "SSSRS": 0,

      "RRRSS": 0, "RRPSS": 0, "RRSSS": 0,
      "RPRSS": 0, "RPPSS": 0, "RPSSS": 0,
      "RSRSS": 0, "RSPSS": 0, "RSSSS": 0,
      "PRRSS": 0, "PRPSS": 0, "PRSSS": 0,
      "PPRSS": 0, "PPPSS": 0, "PPSSS": 0,
      "PSRSS": 0, "PSPSS": 0, "PSSSS": 0,
      "SRRSS": 0, "SRPSS": 0, "SRSSS": 0,
      "SPRSS": 0, "SPPSS": 0, "SPSSS": 0,
      "SSRSS": 0, "SSPSS": 0, "SSSSS": 0,
}]

useMarkovChain = True
def player(prev_play, opponent_history=[] ,my_history=[]):
  if useMarkovChain:
        global play_order5
        if not prev_play:
            opponent_history=[]
            my_history=[]
            prev_play = 'S'
            play_order5=[{
                  "RRRPR": 0, "RRPPR": 0, "RRSPR": 0,"RPRPR": 0, "RPPPR": 0, "RPSPR": 0,"RSRPR": 0, "RSPPR": 0, "RSSPR": 0,"PRRPR": 0, "PRPPR": 0, "PRSPR": 0,"PPRPR": 0, "PPPPR": 0, "PPSPR": 0,"PSRPR": 0, "PSPPR": 0, "PSSPR": 0,"SRRPR": 0, "SRPPR": 0, "SRSPR": 0,"SPRPR": 0, "SPPPR": 0, "SPSPR": 0,"SSRPR": 0, "SSPPR": 0, "SSSPR": 0,"RRRRR": 0, "RRPRR": 0, "RRSRR": 0,"RPRRR": 0, "RPPRR": 0, "RPSRR": 0,"RSRRR": 0, "RSPRR": 0, "RSSRR": 0,"PRRRR": 0, "PRPRR": 0, "PRSRR": 0,"PPRRR": 0, "PPPRR": 0, "PPSRR": 0,"PSRRR": 0, "PSPRR": 0, "PSSRR": 0,"SRRRR": 0, "SRPRR": 0, "SRSRR": 0,"SPRRR": 0, "SPPRR": 0, "SPSRR": 0,"SSRRR": 0, "SSPRR": 0, "SSSRR": 0,"RRRSR": 0, "RRPSR": 0, "RRSSR": 0,"RPRSR": 0, "RPPSR": 0, "RPSSR": 0,"RSRSR": 0, "RSPSR": 0, "RSSSR": 0,"PRRSR": 0, "PRPSR": 0, "PRSSR": 0,"PPRSR": 0, "PPPSR": 0, "PPSSR": 0,"PSRSR": 0, "PSPSR": 0, "PSSSR": 0,"SRRSR": 0, "SRPSR": 0, "SRSSR": 0,"SPRSR": 0, "SPPSR": 0, "SPSSR": 0,"SSRSR": 0, "SSPSR": 0, "SSSSR": 0,"RRRPP": 0, "RRPPP": 0, "RRSPP": 0,"RPRPP": 0, "RPPPP": 0, "RPSPP": 0,"RSRPP": 0, "RSPPP": 0, "RSSPP": 0,"PRRPP": 0, "PRPPP": 0, "PRSPP": 0,"PPRPP": 0, "PPPPP": 0, "PPSPP": 0,"PSRPP": 0, "PSPPP": 0, "PSSPP": 0,"SRRPP": 0, "SRPPP": 0, "SRSPP": 0,"SPRPP": 0, "SPPPP": 0, "SPSPP": 0,"SSRPP": 0, "SSPPP": 0, "SSSPP": 0,"RRRRP": 0, "RRPRP": 0, "RRSRP": 0,"RPRRP": 0, "RPPRP": 0, "RPSRP": 0,"RSRRP": 0, "RSPRP": 0, "RSSRP": 0,"PRRRP": 0, "PRPRP": 0, "PRSRP": 0,"PPRRP": 0, "PPPRP": 0, "PPSRP": 0,"PSRRP": 0, "PSPRP": 0, "PSSRP": 0,"SRRRP": 0, "SRPRP": 0, "SRSRP": 0,"SPRRP": 0, "SPPRP": 0, "SPSRP": 0,"SSRRP": 0, "SSPRP": 0, "SSSRP": 0,"RRRSP": 0, "RRPSP": 0, "RRSSP": 0,"RPRSP": 0, "RPPSP": 0, "RPSSP": 0,"RSRSP": 0, "RSPSP": 0, "RSSSP": 0,"PRRSP": 0, "PRPSP": 0, "PRSSP": 0,"PPRSP": 0, "PPPSP": 0, "PPSSP": 0,"PSRSP": 0, "PSPSP": 0, "PSSSP": 0,"SRRSP": 0, "SRPSP": 0, "SRSSP": 0,"SPRSP": 0, "SPPSP": 0, "SPSSP": 0,"SSRSP": 0, "SSPSP": 0, "SSSSP": 0,"RRRPS": 0, "RRPPS": 0, "RRSPS": 0,"RPRPS": 0, "RPPPS": 0, "RPSPS": 0,"RSRPS": 0, "RSPPS": 0, "RSSPS": 0,"PRRPS": 0, "PRPPS": 0, "PRSPS": 0,"PPRPS": 0, "PPPPS": 0, "PPSPS": 0,"PSRPS": 0, "PSPPS": 0, "PSSPS": 0,"SRRPS": 0, "SRPPS": 0, "SRSPS": 0,"SPRPS": 0, "SPPPS": 0, "SPSPS": 0,"SSRPS": 0, "SSPPS": 0, "SSSPS": 0,"RRRRS": 0, "RRPRS": 0, "RRSRS": 0,"RPRRS": 0, "RPPRS": 0, "RPSRS": 0,"RSRRS": 0, "RSPRS": 0, "RSSRS": 0,"PRRRS": 0, "PRPRS": 0, "PRSRS": 0,"PPRRS": 0, "PPPRS": 0, "PPSRS": 0,"PSRRS": 0, "PSPRS": 0, "PSSRS": 0,"SRRRS": 0, "SRPRS": 0, "SRSRS": 0,"SPRRS": 0, "SPPRS": 0, "SPSRS": 0,"SSRRS": 0, "SSPRS": 0, "SSSRS": 0,"RRRSS": 0, "RRPSS": 0, "RRSSS": 0,"RPRSS": 0, "RPPSS": 0, "RPSSS": 0,"RSRSS": 0, "RSPSS": 0, "RSSSS": 0,"PRRSS": 0, "PRPSS": 0, "PRSSS": 0,"PPRSS": 0, "PPPSS": 0, "PPSSS": 0,"PSRSS": 0, "PSPSS": 0, "PSSSS": 0,"SRRSS": 0, "SRPSS": 0, "SRSSS": 0,"SPRSS": 0, "SPPSS": 0, "SPSSS": 0,"SSRSS": 0, "SSPSS": 0, "SSSSS": 0,
              }]
        opponent_history.append(prev_play)
        my_history.append(prev_play)
        if len(opponent_history) > 5:
          last_four = "".join(opponent_history[-4:])
          last_five = "".join(opponent_history[-5:])
          if len(last_five) == 5:
              play_order5[0][last_five] += 1
          potential_plays = [
              last_four + "R",
              last_four + "P",
              last_four + "S",
          ]

          sub_order = {
              k: play_order5[0][k]
              for k in potential_plays if k in play_order5[0]
          }
          # print(sub_order)
          last_2_play = my_history[-1] + opponent_history[-1]

          if max(sub_order, key=sub_order.get)[-2:] != last_2_play:
            prediction = max(sub_order, key=sub_order.get)[-1:]
          else :
            list_exp_max = sub_order.copy()
            list_exp_max[max(sub_order, key=sub_order.get)] = 0
            list_exp_max[min(sub_order, key=sub_order.get)] = 0
            prediction = max(list_exp_max, key=sub_order.get)[-1:]

          ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
          return ideal_response[prediction]
        
        if len(opponent_history) == 1 : return "S"
        if len(opponent_history) == 2 : return "S"
        if len(opponent_history) == 3 : return "S"
        if len(opponent_history) == 4 : return "R"
        if len(opponent_history) == 5 : return "R"

        return "S"
  else:
      ## Nueral 

      from tensorflow import keras
      import numpy as np
      
      model = keras.Sequential([
      keras.layers.Dense(12, activation='relu', input_shape=(5,)),  # input layer (4,)
      keras.layers.Dense(6, activation='relu'),  # output layer (3)
      keras.layers.Dense(6, activation='relu'),  # output layer (3)
      keras.layers.Dense(6, activation='relu'),  # output layer (3)
      keras.layers.Dense(3, activation='softmax')  # output layer (3)
      ])

      model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])


      def guess_fn(opponent_history):
          numbers_Represent = {'R': 0, 'P': 1, 'S': 2}
          beat = {'R': "P", 'P': "S", 'S': "R"}
          data = [numbers_Represent[opponent_history[-1]],
                  numbers_Represent[opponent_history[-2]],
                  numbers_Represent[opponent_history[-3]],
                  numbers_Represent[opponent_history[-4]],
                  numbers_Represent[opponent_history[-5]]]

          data = np.array(data)  # Convert to numpy array

          predictions = model.predict(np.expand_dims(data, axis=0),verbose=0)
          index = np.argmax(predictions[0])
          # print("##################",index)
          guess = ""
          if index == 0:
              guess = "R"
          elif index == 1:
              guess = "P"
          elif index == 2:
              guess = "S"

          return beat[guess]



          
      def guess_plays(opponent_history):
          numbers_Represent = {'R': 0, 'P': 1, 'S': 2}
          y_tr = []
          x_tr = []

          added = []
          v = 0
          for i in range(v, len(opponent_history)):
              added.append(numbers_Represent[opponent_history[i]])
              v += 1
              if len(added) % 5 == 0:
                  try:
                      x_tr.append(numbers_Represent[opponent_history[i + 1]])
                      y_tr.append(added)
                  except:
                      pass
                  added = []

          y_tr = np.array(y_tr)
          x_tr = np.array(x_tr)

          # print(y_tr)
          # print(x_tr)
          model.fit(y_tr, x_tr)


      def player(prev_play, opponent_history=[]):
          if not prev_play:
            
              opponent_history = []        
              guess = random.choice(['R', 'P', 'S'])
          else:
              opponent_history.append(prev_play)

              if len(opponent_history) < 6:
                  guess = random.choice(['R', 'P', 'S'])
              else:
                  guess_plays(opponent_history)
                  guess = guess_fn(opponent_history)

          return guess

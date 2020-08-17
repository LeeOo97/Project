import math

class MS2peak:
    def __init__(self, id1, id2, ms1mz, ms2mz, ms2rt):
        self.id1 = id1 #<ms1_id>
        self.id2 = id2 #<ms2_id>
        self.ms1mz = ms1mz #m/z of the MS1 peak
        self.ms2mz = ms2mz #m/z of the MS2 peak
        self.ms2rt = ms2rt #rt of the MS2 peak 
        self.rootMS2 = math.sqrt(self.ms2rt) #square root of MS2 intensity 

    def __repr__(self):
        return {'id1':self.id1,'id2':self.id2, 'ms1mz':self.ms1mz, 'ms2ms': self.ms2mz, 'ms2rt':self.ms2rt, 'rootMS2': self.rootMS2}
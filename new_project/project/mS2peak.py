import math

class MS2peak:
    def __init__(self, id, ms2mz, ms2rt):
        self.id = id #<ms2_id>
        self.ms2mz = ms2mz #m/z of the MS2 peak
        self.ms2rt = ms2rt #rt of the MS2 peak 
        self.rootMS2 = math.sqrt(self.ms2rt) #square root of MS2 intensity 



        def __repr__(self):
            return {'id':self.id, 'ms2mz': self.ms2mz, 'ms2rt':self.ms2rt, 'rootMS2': self.rootMS2}



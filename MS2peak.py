import math

class MS2peak:
    def __init__(self, identifier, ms1mz, ms2mz, ms2rt):
        self.identifier = identifier #<fragset_id>_<ms1_id>
        self.ms1mz = ms1mz #m/z of the MS1 peak
        self.ms2mz = ms2mz #m/z of the MS2 peak
        self.ms2rt = ms2rt #rt of the MS2 peak 
        self.rootMS2 = math.sqrt(self.ms2rt) #square root of MS2 intensity
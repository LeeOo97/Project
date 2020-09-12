from mS2peak import MS2peak
import numpy

class Spectra:
    def __init__(self, id1, mass):
        self.peaks = [] #list of ms2peaks
        self.id1 = id1 #ms1 id
        self.mass = mass


    def __repr__(self):
        return {'peaks':self.peaks, 'id1':self.id1, 'mass':self.mass}

    def add_peak(self, id, ms2mz, ms2rt):
        self.peaks.append(MS2peak(id, ms2mz, ms2rt))

    def scale_intensity(self):
        intensities = []
        for peak in self.peaks:
            intensities.append(peak.rootMS2)

        norm = numpy.linalg.norm(intensities)

        for peak in self.peaks:
            peak.scaled=(peak.rootMS2)/norm

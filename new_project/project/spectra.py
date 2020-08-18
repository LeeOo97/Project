from .mS2peak import MS2peak
import numpy

class Spectra:
    def __innit__(self, id1):
        self.peaks = [] #list of ms2peaks
        self.id1 = id1 #ms1 id

    def __repr__(self):
        return {'peaks':self.peaks, 'id1':self.id1}

    def add_peak(self, id, ms2mz, ms2rt):
        self.peaks.append(MS2peak(id, ms2mz, ms2rt))

    def intensity_scale(self):
        intensities = []
        for MS2peak in self.peaks:
            intensities.append(MS2peak.rootMS2)

        norm = numpy.linalg.norm(intensities)

        for MS2peak in self.peaks:
            MS2peak.scaled=(MS2peak.rootMS2)/norm

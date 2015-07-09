# A simple python wrapper around odb calls to make initialization easier

import os
from subprocess import call

class ODB:
    def __init__(self, expname):
        self.expname = expname
        with open(os.environ['MIDAS_EXPTAB']) as f:
            exptab = f.read().split('\n')
            for line in exptab:
                if line.find(expname) != -1:
                    midasdir = line.split(' ')[1]
                    self.expdir = midasdir.replace('/resources', '')

    def mkdir(self, dirname):
        cmd = ['odbedit', '-e', self.expname, '-c']
        cmd.append('mkdir "' + dirname + '"')
        return call(cmd)

    def create_key(self, path, typestring, key):
        cmd = ['odbedit', '-e', self.expname, '-c']
        cmd.append('create ' + typestring + ' "' + path + '/' + str(key) + '"')
        return call(cmd)

    def set_value(self, key, val):
        cmd = ['odbedit', '-e', self.expname, '-c']
        cmd.append('set "' + key + '" "' + str(val) + '"')
        return call(cmd)

    def call_cmd(self, cmdstring):
        cmd = ['odbedit', '-e', self.expname, '-c']
        cmd.append(cmdstring)
        return call(cmd)

class ExptList:
    def __init__(self, exptab='/etc/exptab'):
        self.exptab = exptab
        self.expt_names = []
        self.expt_dirs = []

        with open('/etc/exptab', 'r') as f:
            
            lines = f.read()
            lines = lines.split('\n')
            
            for line in lines:
                self.expt_names.append(line.split(' ')[0])
                self.expt_dirs.append(line.split(' ')[1])


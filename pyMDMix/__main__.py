#!/usr/bin/env python3
"""
pyMDMix main entry point - redirects to command interface
"""

import sys
import argparse
import pyMDMix
from pyMDMix import MDMixError

class MDMixClient(object):
    def __init__(self):
        self.actions = {}
        self.parser = self.createParser()

    def createParser(self):
        from pyMDMix.Commands import Create, Info, Add, Remove, Queue, Plot, Analyze, Tools
        parser = argparse.ArgumentParser("mdmix")
        parser.add_argument("--log", action="store", dest="logfile", help="Logging file. Default: output to stdout")
        parser.add_argument("--debug", action="store_true", dest="debug", default=False, help="Print debugging info")
        subparsers = parser.add_subparsers(help='commands', dest='command')
        for action in [
            Create.Create(),
            Info.Info(),
            Add.Add(),
            Remove.Remove(),
            Queue.Queue(),
            Plot.Plot(),
            Analyze.Analyze(),
            Tools.Tools()
        ]:
            self.actions[action.cmdstring] = action
            action.create_parser(subparsers)
        return parser

    def header(self):
        return """
        ==========================================================
        ||              pyMDMix User Interface                  ||
        ==========================================================
        ||  Author: Daniel Alvarez-Garcia                       ||
        ||  Version : %s                                     
        ==========================================================
        
        """%pyMDMix.__version__

    def createRootLogger(self, level, logFile=None):
        pyMDMix.setLogger(level, logFile)

    def run(self):
        print(self.header())
        import time
        t0 = time.time()
        parserargs = self.parser.parse_args()
        command = parserargs.command
        
        # If logging file, redirect stdout and stderr to file
        if parserargs.logfile:
            sys.stderr = open(parserargs.logfile, 'w+')
            sys.stdout = sys.stderr
            print(' '.join(sys.argv))

        if parserargs.debug: level = 'DEBUG'
        else: level = 'INFO'
        self.createRootLogger(level, parserargs.logfile)

        # Study the different actions
        self.actions[command].action(parserargs)

        sys.stdout.flush()
        print("Total execution time: %.3fs"%(time.time()-t0))

def main():
    """Main entry point for pyMDMix command line interface"""
    try:
        client = MDMixClient()
        client.run()
    except KeyboardInterrupt:
        print("\nForcing MDMix UI exit!")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

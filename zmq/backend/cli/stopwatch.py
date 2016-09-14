from zmq.error import ZMQError
import System

class Stopwatch(System.Diagnostics.Stopwatch):
    def __init__(self):
        pass

    def start(self):
        self.Start()

    def stop(self):
        self.Stop();
        return self.Elapsed.TotalMilliseconds * 1000 # ms to us

    def sleep(self, seconds):
        System.Threading.Sleep(seconds * 1000) # s to ms


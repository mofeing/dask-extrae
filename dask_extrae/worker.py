from distributed.diagnostics.plugin import WorkerPlugin
import pyextrae
from enum import Enum, unique


@unique
class Events(Enum):
    TASK = 1000000


@unique
class State(Enum):
    Setup = 1


class ExtraeWorkerPlugin(WorkerPlugin):
    def __init__(self):
        # counters
        self.waiting = 0
        self.ready = 0
        self.executing = 0
        self.error = 0

    def release_key(self, key, state, cause, reason, report):
        pass

    def setup(self, worker):
        self.worker = worker

    def teardown(self, worker):
        pyextrae.sequential.shutdown()

    def transition(self, key, start, finish, **kwargs):
        # Task arrived to scheduler - waiting
        if finish == "waiting":
            pyextrae.sequential.event(..., ...)
            self.waiting += 1

        # Dependencies solved -> task ready for execution
        elif start == "waiting" and finish == "ready":
            self.waiting -= 1
            self.ready += 1

        # Task execution started
        elif start == "ready" and finish == "executing":
            pyextrae.sequential.event(..., ...)
            self.ready -= 1
            self.executing += 1

        # Task execution finished with success
        elif start in ["executing", "long-running"] and finish == "memory":
            pyextrae.sequential.event(..., ...)
            self.executing -= 1

        # Task execution finished with error
        elif start in ["executing", "long-running"] and finish == "error":
            pyextrae.sequential.event(..., ...)
            self.executing -= 1
            self.error += 1

        else:
            raise RuntimeError(
                "Unknown start ({0}) - finish ({1}) combination".format(start, finish)
            )

from distributed.diagnostics.plugin import SchedulerPlugin


class ExtraeSchedulerPlugin(SchedulerPlugin):
    def __init__(self):
        pass

    def add_client(self, scheduler=None, client=None, **kwargs):
        pass

    def add_worker(self, scheduler=None, worker=None, **kwargs):
        pass

    async def close(self):
        pass

    def remove_client(self, scheduler=None, client=None, **kwargs):
        pass

    def remove_worker(self, scheduler=None, worker=None, **kwargs):
        pass

    def restart(self, scheduler, **kwargs):
        pass

    async def start(self, scheduler):
        pass

    def transition(self, key, start, finish, *args, **kwargs):
        pass

    def update_graph(self, scheduler, dsk=None, keys=None, restrictions=None, **kwargs):
        pass

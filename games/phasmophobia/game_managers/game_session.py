class PhasmophobiaGameSession:
    def __init__(self):
        self.players = PlayerManager()
        self.devices = DeviceManager()
        self.score = ScoreManager()
        self.timers = TimerManager()
        self.event_bus = EventBus()
        self.ghost = GhostManager(self.event_bus)
        self.hunt = HuntManager(self.ghost, self.timers, self.event_bus)
        self.haunting = HauntingManager(self.ghost, self.event_bus)
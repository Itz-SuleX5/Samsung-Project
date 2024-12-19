class TeamData:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TeamData, cls).__new__(cls)
            cls._instance.team_id = None
            cls._instance.players_dict = {}
        return cls._instance
    
    @property
    def id(self):
        return self.team_id
    
    @id.setter
    def id(self, value):
        self.team_id = value

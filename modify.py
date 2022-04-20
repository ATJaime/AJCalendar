class Modify:
    def create_task(self, 
        description: str, 
        creation_date: date, 
        relevance_level: int,
        is_done: bool,
        color: str,
        due_date: date
    ) -> None:
        self.tasks.append(Task(
            is_done=is_done, color=color, due_date=due_date, 
            description=description, creation_date=creation_date, 
            relevance_level=relevance_level)
            )

    def create_meeting(self):
        pass
    
    def create_note(self):
        pass
    
    def block_distractions(self):
        pass
    
    def remove_task(self):
        pass
    
    def remove_meeting(self):
        pass
    
    def remove_note(self):
        pass
    
    def unblock_distractions(self):
        pass
    
    def update_preferences(self):
        pass

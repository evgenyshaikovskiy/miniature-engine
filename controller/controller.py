from view.view import ViewComponent


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(controller=self)
        
        # setup observer pattern to manipulate
        self._observers = []
        self.subscribe(self.view)
        
    def get_screen(self):
        return self.view.build()
    
    def subscribe(self, observer):
        self._observers.append(observer)
        
    def unsubscribe(self, observer):
        self._observers.remove(observer)
        
    def notify(self, data):
        for observer in self._observers:
            observer.on_controller_change(data)
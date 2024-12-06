class Observer:
    def update(self, message: str):
        raise NotImplementedError("Subclasses must override this method.")

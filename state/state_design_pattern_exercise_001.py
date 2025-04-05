class Player:
  def __init__(self):
    self.state:State = StoppedState(self)

  def play(self):
    self.state.play()

  def stop(self):
    self.state.stop()

  def pause(self):
    self.state.pause()

  def change_state(self, state):
    self.state = state


class State:
  def __init__(self, player):
    self.player = player
  
  def play(self): pass
  def stop(self): pass  
  def pause(self): pass


class StoppedState(State):
  def __init__(self, player):
    super().__init__(player)
    print('Music stopped')
  
  def play(self):
    # such syntax because constructor takes player object
    self.player.change_state(PlayingState(self.player))
  
  # Already stopped, so these do nothing
  def stop(self): pass
  def pause(self): pass


class PlayingState(State):
  def __init__(self, player):
    super().__init__(player)
    print('Music is playing')
  
  # Already playing, so this does nothing
  def play(self): pass
  
  def stop(self):
    self.player.change_state(StoppedState(self.player))
  
  def pause(self):
    self.player.change_state(PausedState(self.player))


class PausedState(State):
  def __init__(self, player):
    super().__init__(player)
    print('Music is paused')
  
  def play(self):
    self.player.change_state(PlayingState(self.player))
  
  def stop(self):
    self.player.change_state(StoppedState(self.player))
  
  # Already paused, so this does nothing  
  def pause(self): pass


class Bowling:

    def __init__(self):
        self.current_score = 0
        self.previous_skittle_number = None
        self.frames = [[None, None]]

    def roll(self, skittle_number):
        if self.frames[-1][0] is None:
            self.frames[-1][0] = skittle_number
            if skittle_number == 10:
                self.frames[-1][1]=0
            if self.last_was_spare() or self.last_was_strike():
                self.current_score += skittle_number*2
            else:
                self.current_score += skittle_number
        elif self.frames[-1][1] is None:
            self.frames[-1][1] = skittle_number
            if self.last_was_strike():
                self.current_score += skittle_number*2
            else:
                self.current_score += skittle_number
        else:
            self.frames.append([None, None])
            self.roll(skittle_number)


    def score(self):
        return self.current_score

    def last_was_spare(self):
        if len(self.frames) > 1:
            if sum(self.frames[-2]) == 10:
                return True
        return False

    def last_was_strike(self):
        if len(self.frames) > 1:
            if self.frames[-2][0] == 10:
                return True
        return False

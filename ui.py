import panel as pnl
import param as prm


class Bla(prm.Parameterized):
    phase = prm.String('asdf')

    def get_ui(self):
        return pnl.Column(self.bla)


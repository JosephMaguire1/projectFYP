from flask import render_template

class View(object):
    @classmethod
    def render(self):
        return render_template("base.html")

class ViewMicrostrip(object):
    @classmethod
    def render(self, answer):
        return render_template("baseMicrostrip.html", answer1=answer)

class ViewCPW(object):
    @classmethod
    def render(self, answer):
        return render_template("baseCPWNewLayout.html", answer1=answer)

class ViewMicrostripCalculations(object):
    @classmethod
    def render(self):
        return render_template("baseMicrostripCalculations.html")

class ViewCPWCalculations(object):
    @classmethod
    def render(self):
        return render_template("baseCPWCalculations.html")

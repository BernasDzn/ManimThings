from manimlib import *

class Erm(Scene):
    def construct(self):
        text = Text("ginger")
        text.scale(2)
        
        text2 = Text("nigger")
        text2.scale(2)
        
        self.play(Write(text))
        
        self.wait(1)
        
        kw = dict(run_time=1, path_arc=PI/2)
        self.play(TransformMatchingShapes(text, text2, **kw))
        self.play(Indicate(text2, run_time=0.5))
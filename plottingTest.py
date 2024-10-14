from manimlib import *

def equation(x):
    return x**2

class Plot(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"color": BLUE_A},
        )
        axes.add_coordinate_labels(font_size=20)
        
        self.play(Write(axes))
        
        graph = axes.get_graph(equation, color=RED)
        self.play(Write(graph), run_time=3, rate_func=smooth)
            
        self.wait(1)
                
        text = Text("This is a graph of y = x^2")
        text.shift(UP*5)
        text.shift(RIGHT*7)
        text.scale(1.25)
        
        self.play(
                  self.frame.animate.shift(UP*5+RIGHT*7).scale(0.75),
                  Write(text)
                  )
        
        self.wait(3)
        
        self.play(FadeOut(text))
        
        self.wait(1)
        
        text2 = Text("Thank you for watching.")
        text2.shift(UP*5)
        text2.shift(RIGHT*7)
        text2.scale(1.25)
        
        self.play(Write(text2))
        
        self.wait(3)
        
        self.play(FadeOut(text2),
                  FadeOut(axes),
                  FadeOut(graph)
                  )
        
        self.wait(1) 
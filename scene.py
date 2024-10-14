from scipy.integrate import solve_ivp
from manimlib import *

def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function, 
        t_span=(0, time), 
        y0=state0, 
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T

class LorenzAttractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
            width=16,
            height=16,
            depth=8,
        )
        axes.set_width(FRAME_WIDTH)
        axes.center()
        
        title = Text("Lorenz Attractor")
        title.scale(2)
        title.fix_in_frame()
        
        text = Text("Lorenz Attractor")
        text = text.scale(0.75)
        text.fix_in_frame()
        text.to_edge(UL)
        
        self.play(Write(title), run_time=2)
        self.play(FadeTransform(title, text), run_time=1)
        self.frame.reorient(43, 76, 1, IN, 10)
        self.add(axes)
        self.play(Write(axes), run_time=3)
        
        epsilon = 0.05
        evolution_time = 30
        states = [
            [10 + n * epsilon, 10 + n * epsilon, 10 + n * epsilon]
            for n in range(10)
        ]
        colors = color_gradient([BLUE, WHITE], len(states))
        curves = VGroup()
        for state, color in zip(states, colors):
            points = ode_solution_points(lorenz_system, state, 10)    
            points_3d = [axes.c2p(x, y, z) for x, y, z in points]
            curve = VMobject().set_points_as_corners(points_3d)
            curve.make_smooth()
            curve.set_stroke(color, 1)
            curves.add(curve)
           
        """ 
        dots = Group(GlowDot(color=color) for color in colors)
        
        def update_dots(dots):
            for dot, curve in zip(dots, curves):
                dot.move_to(curve.get_end())
                
        dots.add_updater(update_dots)

        self.add(dots)
        """
        
        self.play(*(
            ShowCreation(curve, run_time=evolution_time, rate_func=linear)
            for curve in curves
        ))
        
        self.wait(3)
        
        for curve in curves:
            self.play(
                FadeOut(curve, run_time=0.1)
            )
        
        self.play(
            FadeOut(axes, run_time=1),
            FadeOut(text, run_time=1)
            )
        
        self.wait(1)
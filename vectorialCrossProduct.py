from manimlib import *

class VectorialCrossProduct(ThreeDScene):
    def construct(self):
        axes3D = ThreeDAxes(
            x_range=(-7, 7, 1),
            y_range=(-7, 7, 1),
            z_range=(-7, 7, 1),
            width=20,
            height=20,
            depth=20,
        )
        axes3D.set_width(FRAME_WIDTH)
        axes3D.center()
        
        axes3D.get_x_axis().set_color(RED_A)
        axes3D.get_y_axis().set_color(BLUE_A)
        axes3D.get_z_axis().set_color(GREEN_A)
        axes3D.get_x_axis().set_opacity(0.5)
        axes3D.get_y_axis().set_opacity(0.5)
        axes3D.get_z_axis().set_opacity(0.5)
        
        title = Text("Vectorial Cross Product Formula")
        title.fix_in_frame()
        formula1 = Tex(r"A \times B = \Vert A\Vert \Vert B\Vert \sin\theta\mathbf{n}",
              t2c={"A": RED, "B": BLUE, "theta": YELLOW})
        formula1.fix_in_frame()
        formula2 = Tex(r"\Vert A\Vert=\sqrt{x_{A}^{2}+y_{A}^{2}+z_{A}^{2}}",
                       t2c={"x": RED, "y": BLUE, "z": GREEN})
        formula2.fix_in_frame()
        
        number_plane = NumberPlane(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        number_plane_2 = NumberPlane(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        number_plane_3 = NumberPlane(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        title.to_edge(UL)
        formula1.to_edge(UL)
        formula2.to_edge(UL)
        
        formula1.shift(DOWN)
        formula1.scale(1)
        
        formula2.shift(DOWN*1.75)
        formula2.shift(LEFT*0.5)
        formula2.scale(0.75)
        
        ax = -1
        ay = 0
        az = 0
        bx = 0
        by = -1
        bz = 0
        vectorA = Vector([ax,ay,az], stroke_color=RED,color=RED,fill_color=RED)
        vectorB = Vector([bx,by,bz], stroke_color=BLUE,color=BLUE,fill_color=BLUE)
        
        crossProduct = Vector([ay*bz - az*by,
                        az*bx - ax*bz, 
                        ax*by - ay*bx], 
                        stroke_color=GREEN,
                        color=GREEN,
                        fill_color=GREEN)
        
        normal_vector = np.cross(np.array([ax,ay,az]), np.array([bx,by,bz]))
        normal_vector = normal_vector / np.linalg.norm(normal_vector)

        number_plane.rotate(angle=np.arccos(normal_vector[2]),
                            axis=np.cross([0, 0, 1], normal_vector))
        
        ax_2 = -1
        ay_2 = 0
        az_2 = -1
        bx_2 = -1
        by_2 = -1
        bz_2 = 0
        vectorA_2 = Vector([ax_2,ay_2,az_2], stroke_color=RED,color=RED,fill_color=RED)
        vectorB_2 = Vector([bx_2,by_2,bz_2], stroke_color=BLUE,color=BLUE,fill_color=BLUE)
        
        normal_vector = np.cross(np.array([ax_2,ay_2,az_2]), np.array([bx_2,by_2,bz_2]))
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        number_plane_2.rotate(angle=np.arccos(normal_vector[2]),
                              axis=np.cross([0, 0, 1], normal_vector))  
        
        crossProduct_2 = Vector([ay_2*bz_2 - az_2*by_2,
                                 az_2*bx_2 - ax_2*bz_2, 
                                 ax_2*by_2 - ay_2*bx_2], 
                                stroke_color=GREEN,
                                color=GREEN,
                                fill_color=GREEN)
        
        ax_3 = -1
        ay_3 = -1
        az_3 = 0
        bx_3 = 0
        by_3 = -1
        bz_3 = -1
        vectorA_3 = Vector([ax_3,ay_3,az_3], stroke_color=RED,color=RED,fill_color=RED)
        vectorB_3 = Vector([bx_3,by_3,bz_3], stroke_color=BLUE,color=BLUE,fill_color=BLUE)
        
        normal_vector = np.cross(np.array([ax_3,ay_3,az_3]), np.array([bx_3,by_3,bz_3]))
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        number_plane_3.rotate(angle=np.arccos(normal_vector[2]),
                              axis=np.cross([0, 0, 1], normal_vector))  
        
        crossProduct_3 = Vector([ay_3*bz_3 - az_3*by_3,
                                 az_3*bx_3 - ax_3*bz_3, 
                                 ax_3*by_3 - ay_3*bx_3], 
                                stroke_color=GREEN,
                                color=GREEN,
                                fill_color=GREEN)
        
        self.play(Write(axes3D),
                  self.frame.animate.set_height(5).set_theta(-45 * DEGREES),
                  run_time=3)
        
        self.play(Write(title), run_time=2)
        self.play(Write(formula1), run_time=3)
        
        self.play(FadeIn(vectorA),
                  FadeIn(vectorB),
                  run_time=1)
        
        self.play(Indicate(vectorA),
                  Indicate(formula1.get_part_by_tex("A"),
                           scale_factor=1.5))
        
        self.play(Indicate(vectorB),
                  Indicate(formula1.get_part_by_tex("B"),
                           scale_factor=1.5))
        
        self.play(Write(crossProduct),
                  Write(number_plane),
                  run_time=2)
        
        self.play(Write(formula2), run_time=1)
        
        self.wait(1)
        
        self.play(FadeOut(number_plane),
                  FadeOut(crossProduct),
                  run_time=1)
        
        self.play(Transform(vectorA, vectorA_2),
                  Transform(vectorB, vectorB_2),
                  run_time=2)
        
        self.play(Write(crossProduct_2),
                  Write(number_plane_2),
                  self.frame.animate.set_theta(-80 * DEGREES),
                  run_time=3)
        
        self.wait(1)
        
        self.play(FadeOut(number_plane_2),
                  FadeOut(crossProduct_2),
                  run_time=1)
        
        self.play(Transform(vectorA, vectorA_3),
                  Transform(vectorB, vectorB_3),
                  run_time=2)
        
        self.play(Write(crossProduct_3),
                  Write(number_plane_3),
                  self.frame.animate.set_theta(-10 * DEGREES),
                  run_time=3)
        
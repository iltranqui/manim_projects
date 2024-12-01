from manim import *
import random

class HappyChristmas(Scene):
    def construct(self):
        # Create the "Happy Christmas" text
        text = Text("Happy Christmas", font_size=72, color=GREEN)
        text.to_edge(DOWN)  # Position text at the bottom of the screen


        # Create falling stars (snow effect)
        stars = VGroup(*[Dot(color=random.choice([WHITE, YELLOW])) for _ in range(50)])
        
        # Randomly position stars at the top of the screen
        for star in stars:
            star.move_to([random.uniform(-7, 7), random.uniform(3.5, 5), 0])  # Top positions

        # Animation: stars fall from the top and fade out
        falling_animations = [
            star.animate.move_to([star.get_x(), -4, 0]).set_opacity(0) for star in stars
        ]

        # Add some animations to make it interesting
        # 1. Fade in the text
        self.play(FadeIn(text))

        # 2. Animate stars falling in parallel
        self.play(AnimationGroup(*falling_animations, lag_ratio=0.1), run_time=5)

        # 2. Apply a glowing effect
        self.play(
            text.animate.set_color(RED).scale(1.2),
            rate_func=there_and_back_with_pause,
            run_time=3
        )

        # 3. Hold the "Happy Christmas" text for a moment
        self.wait(2)

        # 3. Rotate the text slightly
        self.play(
            text.animate.rotate(PI / 6).set_color(YELLOW),
            rate_func=there_and_back,
            run_time=2
        )

        # Hold the text on the screen for a moment
        self.wait(2)

        # 4. Fade out the text
        self.play(FadeOut(text))

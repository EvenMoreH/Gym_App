from fasthtml.common import * # type: ignore

# for Docker
# app, rt = fast_app(static_path="static") # type: ignore

# for local
app, rt = fast_app(static_path="app/static") # type: ignore

default_header = Head(
                    Title("Gym App"),
                    Meta(charset="UTF-8"),
                    Meta(name="viewport", content="width=device-width, initial-scale=1"),
                    Meta(name="description", content="insert page description for Search Engines"),
                    Meta(name="author", content="EvenMoreH"),
                    Script(src="https://unpkg.com/htmx.org"),
                    Link(rel="stylesheet", href="css/output.css"),
                    Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
                    Link(rel="icon", href="images/favicon.png", type="image/png"),
                )

@rt("/")
def get():
    return Html(
        default_header,
        Body(
            H1("Gym App", cls="pt-2 pb-2 text-xl text-center text-rose-400 hover:text-rose-700"),
            Div(
                # each navigation button, when clicked will pull contents of the page without full reload
                Button("Home",
                    hx_get="home",
                    hx_trigger="click",
                    hx_target="#content",
                    hx_swap="innerHTML",
                    cls="btn"),
                Button("Workout Plan",
                    hx_get="workout",
                    hx_trigger="click",
                    hx_target="#content",
                    hx_swap="innerHTML",
                    cls="btn"),
                Button("Exercises",
                    hx_get="exercises",
                    hx_trigger="click",
                    hx_target="#content",
                    hx_swap="innerHTML",
                    cls="btn"),
                Button("Start Workout",
                    hx_get="start",
                    hx_trigger="click",
                    hx_target="#content",
                    hx_swap="innerHTML",
                    cls="btn"),
                # nav-button css
                cls="flex justify-center p-2"
            ),
            Div(homepage,
                id="content",
                cls="flex justify-center"),
            # whole body CSS
            cls="body"
        ),
    lang="en",
    )

@rt("/home")
def get():
    return Div(homepage)

@rt("/workout")
def get():
    return Div("Your Workout Plan")

@rt("/exercises")
def get():
    return Div("Exercise Base")

@rt("/start")
def get():
    return Div("Start Your Workout Here!")

homepage = """
Welcome to the Gym App
"""

serve()

# if __name__ == '__main__':
#     # Important: Use host='0.0.0.0' to make the server accessible outside the container
#     serve(host='0.0.0.0', port=5001) # type: ignore
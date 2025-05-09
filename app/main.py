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
                Button("Home", cls="btn"),
                Button("Workout Plan", cls="btn"),
                Button("Exercises", cls="btn"),
                Button("Start Workout", cls="btn"),
                cls="flex justify-center p-2"
            ),
            # whole body CSS
            cls="body"
        ),
    lang="en",
    )

@rt("/home")
def get():
    pass

@rt("/workout")
def get():
    pass

@rt("/exercises")
def get():
    pass

@rt("/start")
def get():
    pass


serve()

# if __name__ == '__main__':
#     # Important: Use host='0.0.0.0' to make the server accessible outside the container
#     serve(host='0.0.0.0', port=5001) # type: ignore